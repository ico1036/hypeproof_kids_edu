# /// script
# requires-python = ">=3.12"
# dependencies = ["httpx", "beautifulsoup4", "lxml"]
# ///
"""
YEEP(온라인 창업체험교육 플랫폼) 공개 자료실 수집 도구.

교육부·한국청년기업가정신재단(KOEF)이 yeep.go.kr 자료실에 공개한 창업교육
콘텐츠를 목록화하고 내려받는다. 로그인이 필요 없다.

⚠️ 내려받은 원본은 저작권이 KOEF/교육부에 있다. 내부 참조·연구 용도로만 쓰고
   저장소에 커밋하거나 재배포하지 않는다. 자세한 내용은 README.md 참조.

사용법:
    uv run yeep.py scrape   -o manifest.json
    uv run yeep.py download -m manifest.json -o <저장경로> [--all] [--include-elementary]
    uv run yeep.py text     <파일.pdf> [시작쪽] [끝쪽]
"""
import argparse
import json
import pathlib
import re
import sys
import time

import httpx
from bs4 import BeautifulSoup

BASE = "https://yeep.go.kr"
DOWNLOAD_EP = f"{BASE}/file/getFileDownloadAllUser.do"
UA = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
    )
}

# 자료실 게시판 3종. key -> (표시명, 목록 URL, 상세 URL)
BOARDS = {
    "eduExlntCase": ("창업체험교육 콘텐츠", "/noti/eduExlntCaseList.do", "/noti/eduExlntCaseDetail.do"),
    "rschLeadSch":  ("수업·연구자료",      "/noti/rschLeadSchList.do",  "/noti/rschLeadSchDetail.do"),
    "rfrcData":     ("기타자료",           "/noti/rfrcDataList.do",     "/noti/rfrcDataDetail.do"),
}

# 우선순위 게시물 bltnNo -> 저장 하위폴더.
# 창업·IR 라인 조사에서 실제로 쓴 선별 기준 (curriculum_wiki/research/ 참조).
PRIORITY = {
    # 역량 진단 도구·프레임워크 원전 (헌법 충돌 검토 + 국내 준거 차용 판단)
    "33052": "01_역량진단", "35456": "01_역량진단", "16453": "01_역량진단",
    # 교수학습·프로그램 모형
    "33051": "02_교수학습", "25210": "02_교수학습", "38004": "02_교수학습",
    "25217": "02_교수학습", "35373": "02_교수학습",
    # 실패 다루기 (No-Debug 반전 판정 근거)
    "16555": "03_실패경험",
    # 커리큘럼 실물
    "97616": "04_커리큘럼", "32921": "04_커리큘럼", "40430": "04_커리큘럼",
    "40532": "04_커리큘럼", "35357": "04_커리큘럼",
    # 자산·부품 (카드덱·활동지·용어사전)
    "16452": "05_자산", "16451": "05_자산",
    # 정책·현황
    "16235": "06_정책", "35374": "06_정책", "16232": "06_정책", "7171": "06_정책",
}

# 초등용 파일 (고등 라인 대상이 아니므로 기본 제외)
ELEMENTARY_TOKENS = ("_초.", "(초)", "_초등", "(초등학교)")

# 대용량 미디어 (텍스트 분석 불가, 기본 제외 — 총 1.4GB 중 1.3GB를 차지)
HEAVY_TOKENS = ("동영상", "e-book")


def _client() -> httpx.Client:
    return httpx.Client(timeout=180, follow_redirects=True, headers=UA)


# ── scrape ────────────────────────────────────────────────────────────────
def parse_list(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "lxml")
    out = []
    for a in soup.find_all("a", href=re.compile(r"fnDetail\('(\d+)'\)")):
        m = re.search(r"fnDetail\('(\d+)'\)", a["href"])
        out.append({"bltnNo": m.group(1), "title": a.get_text(" ", strip=True)})
    return out


def parse_detail(html: str) -> list[dict]:
    """상세 페이지의 <a name="attFile"> 속성에서 다운로드 파라미터 3개를 뽑는다."""
    soup = BeautifulSoup(html, "lxml")
    files = []
    for a in soup.find_all("a", attrs={"name": "attFile"}):
        files.append({
            # BeautifulSoup은 속성명을 소문자로 정규화한다
            "sysFileName": a.get("filenm"),
            "uploadFileName": a.get("upldfilenm"),
            "filePath": a.get("filepathtext"),
        })
    return files


def cmd_scrape(args) -> None:
    manifest = {}
    with _client() as c:
        for key, (label, list_url, detail_url) in BOARDS.items():
            seen, items, page = set(), [], 1
            while page <= args.max_pages:
                try:
                    # 페이징은 POST (currentPage)
                    r = c.post(BASE + list_url, data={"currentPage": str(page)})
                    r.raise_for_status()
                    rows = parse_list(r.text)
                except Exception as e:
                    print(f"  ! {label} p{page}: {e}", file=sys.stderr)
                    break
                new = [r for r in rows if r["bltnNo"] not in seen]
                if not new:
                    break
                seen.update(r["bltnNo"] for r in new)
                items.extend(new)
                page += 1

            print(f"[{label}] 게시물 {len(items)}건", file=sys.stderr)
            for it in items:
                try:
                    d = c.get(BASE + detail_url, params={"bltnNo": it["bltnNo"]})
                    it["files"] = parse_detail(d.text)
                except Exception as e:
                    print(f"  ! 상세 {it['bltnNo']}: {e}", file=sys.stderr)
                    it["files"] = []
                it["board"] = label
                it["detail_url"] = f"{BASE}{detail_url}?bltnNo={it['bltnNo']}"
                time.sleep(args.delay)
            manifest[key] = {"label": label, "items": items}

    out = pathlib.Path(args.output)
    out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    total = sum(len(v["items"]) for v in manifest.values())
    nfile = sum(len(i["files"]) for v in manifest.values() for i in v["items"])
    print(f"\n→ {out}  게시물 {total}건 / 첨부 {nfile}개", file=sys.stderr)


# ── download ──────────────────────────────────────────────────────────────
def cmd_download(args) -> None:
    manifest = json.loads(pathlib.Path(args.manifest).read_text(encoding="utf-8"))
    root = pathlib.Path(args.output)

    jobs = []
    for board in manifest.values():
        for it in board["items"]:
            sub = PRIORITY.get(it["bltnNo"])
            if sub is None:
                if not args.all:
                    continue
                sub = "99_기타"
            for f in it["files"]:
                if not f.get("sysFileName"):
                    continue
                name = f.get("uploadFileName") or f["sysFileName"]
                if not args.include_elementary and any(t in name for t in ELEMENTARY_TOKENS):
                    continue
                if not args.include_heavy and any(t in name for t in HEAVY_TOKENS):
                    continue
                jobs.append((sub, it["bltnNo"], f, name))

    print(f"{len(jobs)}개 파일 대기", file=sys.stderr)
    total = skipped = 0
    with _client() as c:
        for sub, bltn, f, name in jobs:
            d = root / sub
            d.mkdir(parents=True, exist_ok=True)
            dest = d / f"[{bltn}] {name}".replace("/", "-")
            if dest.exists() and dest.stat().st_size > 0:
                total += dest.stat().st_size
                skipped += 1
                continue
            try:
                r = c.get(DOWNLOAD_EP, params={
                    "sysFileName": f["sysFileName"],
                    "uploadFileName": name,
                    "filePath": f["filePath"],
                    "disp": "attachment",
                })
                r.raise_for_status()
                if len(r.content) < 2000:           # 오류 페이지가 200으로 오는 경우
                    print(f"  ! 실패(응답 {len(r.content)}B): {name}", file=sys.stderr)
                    continue
                dest.write_bytes(r.content)
                total += len(r.content)
                print(f"  ok {len(r.content)/1e6:7.1f}MB  {sub}/{name}", file=sys.stderr)
            except Exception as e:
                print(f"  ! {name}: {e}", file=sys.stderr)

    print(f"\n총 {total/1e6:.1f}MB (기존 파일 {skipped}개 건너뜀)", file=sys.stderr)
    print("⚠️  원본은 KOEF/교육부 저작물이다. 저장소에 커밋하지 말 것.", file=sys.stderr)


# ── text ──────────────────────────────────────────────────────────────────
def cmd_text(args) -> None:
    try:
        from pypdf import PdfReader
    except ImportError:
        sys.exit("pypdf 필요:  uv run --with pypdf yeep.py text ...")
    r = PdfReader(args.pdf)
    a = args.start or 1
    b = args.end or len(r.pages)
    print(f"### 전체 {len(r.pages)}쪽", file=sys.stderr)
    for i in range(a - 1, min(b, len(r.pages))):
        t = (r.pages[i].extract_text() or "").strip()
        if t:
            print(f"\n===== p{i+1} =====\n{t}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("scrape", help="자료실 전수 크롤링 → 매니페스트 JSON")
    s.add_argument("-o", "--output", default="manifest.json")
    s.add_argument("--max-pages", type=int, default=12)
    s.add_argument("--delay", type=float, default=0.15, help="상세 페이지 요청 간격(초)")
    s.set_defaults(func=cmd_scrape)

    d = sub.add_parser("download", help="매니페스트 기반 다운로드")
    d.add_argument("-m", "--manifest", default="manifest.json")
    d.add_argument("-o", "--output", required=True, help="저장 루트 (예: kids_edu_vault/.raw/yeep)")
    d.add_argument("--all", action="store_true", help="우선순위 목록 밖 게시물도 전부")
    d.add_argument("--include-elementary", action="store_true", help="초등용 파일 포함")
    d.add_argument("--include-heavy", action="store_true", help="동영상·e-book 포함 (+1.3GB)")
    d.set_defaults(func=cmd_download)

    t = sub.add_parser("text", help="PDF → 텍스트 (정독용)")
    t.add_argument("pdf")
    t.add_argument("start", nargs="?", type=int)
    t.add_argument("end", nargs="?", type=int)
    t.set_defaults(func=cmd_text)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
