# yeep-fetch

**YEEP 공개 자료실 수집 도구.** 교육부·한국청년기업가정신재단(KOEF)이
[yeep.go.kr](https://yeep.go.kr) 자료실에 공개한 창업교육 자료를 목록화하고 내려받는다.

## 왜 있는가

창업·IR 라인([[startup-hot]]) 조사에서 국가가 이미 무료로 제공하는 자료가
**우리 커리큘럼의 하한선이자 비교 기준**임이 확인됐다. 무엇이 이미 있는지 모르고
만들면 중복이 된다.

그런데 **원본 1.1GB는 저장소에 올릴 수 없다**(아래 참조). 그래서 원본 대신
**재수집 수단**을 커밋한다. 어느 환경에서든 두 줄로 자료 전체를 복원할 수 있다.

조사 결과는 볼트에 있다:

| 문서 | 내용 |
|---|---|
| `curriculum_wiki/research/startup-yeep-resource-manifest.md` | 자료실 **전수 203건** 목록 |
| `curriculum_wiki/research/startup-yeep-benchmark-kr.md` | 무엇이 이미 있는가 |
| `curriculum_wiki/research/startup-yeep-deep-read-kr.md` | 본문 정독 4건 |

## 사용법

`uv`만 있으면 된다. 의존성은 스크립트 인라인 메타데이터로 자동 설치된다.

```bash
cd tools/yeep-fetch

# 1) 자료실 전수 크롤링 → 매니페스트 (약 1분, 203건/첨부 272개)
uv run yeep.py scrape -o manifest.json

# 2) 우선순위 자료 다운로드 (약 1.0GB / 42개 파일)
uv run yeep.py download -m manifest.json -o ../../kids_edu_vault/.raw/yeep

# 3) PDF 본문 읽기 (정독용)
uv run --with pypdf yeep.py text "../../kids_edu_vault/.raw/yeep/02_교수학습/[25210] ....pdf" 20 40
```

이미 받은 파일은 건너뛴다. 중단 후 재실행해도 안전하다.

### 다운로드 범위 조절

기본값은 **창업·IR 라인 조사에 실제로 쓴 선별**이다 — 우선순위 게시물 21건,
초등용 제외, 대용량 미디어 제외.

| 옵션 | 효과 |
|---|---|
| (기본) | 42개 파일 / **1.0GB** |
| `--include-elementary` | 초등학교용 3개 추가 (+0.1GB) |
| `--include-heavy` | 동영상·e-book zip 추가 (**+1.3GB**) — 텍스트 분석 불가 |
| `--all` | 우선순위 밖 게시물까지 전부 → `99_기타/` |

우선순위 목록과 폴더 분류는 `yeep.py`의 `PRIORITY` 딕셔너리에 있다.
`bltnNo`(게시물 번호)로 지정하며, 매니페스트나 볼트 문서에서 번호를 확인할 수 있다.

## 저장 위치와 커밋 금지

기본 저장 경로 `kids_edu_vault/.raw/yeep/` 는 **`.gitignore` 되어 있다**
(루트 `.gitignore` 54행). 의도된 것이므로 해제하지 말 것.

> ### ⛔ 내려받은 원본을 저장소에 커밋하지 않는다
>
> **저작권.** 이 저장소는 **공개(public)** 이다. 자료의 저작권은 KOEF·교육부에 있고
> **공공누리(KOGL) 표시가 없다.**
> - 「창업가정신 함양 교육 교수-학습 매뉴얼」 판권지:
>   *"이 책은 저작권법에 의하여 보호를 받는 저작물이므로 무단 전재와 복제를 금합니다."*
> - YEEP 사이트 푸터: *"COPYRIGHT © BY KOREA ENTREPRENEURSHIP FOUNDATION. ALL RIGHTS RESERVED"*
>
> 내려받아 **내부에서 참조·연구·비평**하는 것과, **공개 저장소에 올려 재배포**하는 것은
> 다른 행위다. 후자는 공중송신에 해당한다. 우리는 이 자료를 벤치마크로 삼아
> 경쟁 상품을 만드는 영리 주체이므로 사적 이용 방어도 약하다.
>
> **기술적 제약도 있다.** 100MB를 넘는 파일이 2개 있어(183MB, 115MB) GitHub이
> 푸시를 **거부**한다. 경고가 아니라 차단이다. 저장소는 현재 11MB이며,
> 1.1GB를 넣으면 100배가 되고 나중에 지우려면 히스토리 재작성이 필요하다.
>
> **볼트에 남기는 것은 우리가 쓴 분석뿐이다.** 인용은 출처를 밝히고 필요한 범위로 제한한다.

## 동작 원리

로그인이 필요 없다. 상세 페이지의 `<a name="attFile">` 태그 속성 3개가 그대로
다운로드 파라미터가 된다.

```
목록  POST /noti/{board}List.do          body: currentPage=N
상세  GET  /noti/{board}Detail.do?bltnNo=<번호>
첨부  GET  /file/getFileDownloadAllUser.do
           ?sysFileName=<fileNm>
           &uploadFileName=<URL인코딩된 upldFileNm>
           &filePath=<filePathText>
           &disp=attachment
```

게시판 3종: `eduExlntCase`(창업체험교육 콘텐츠 53건) · `rschLeadSch`(수업·연구자료 30건) ·
`rfrcData`(기타자료 120건 — 첨부 없는 시사 이슈 카드).

⚠️ 사이트 구조가 바뀌면 `parse_list` / `parse_detail`이 깨진다. 그 경우 상세 페이지
HTML을 직접 확인해 셀렉터를 고친다.

## 검증 (2026-08-25)

| 항목 | 결과 |
|---|---|
| 크롤링 | 203건 / 첨부 272개 — 최초 조사와 일치 |
| 다운로드 파라미터 누락 | 0건 |
| 우선순위 21건 목록 확인 | 전부 존재 |
| 다운로드 재현 | 42개 파일 1,081.8MB — 기존 로컬과 파일 트리 동일 (초등 3개 제외분 제외) |
