# CLAUDE.md — HypeProof Kids Edu

## 프로젝트 개요
국립암센터 소아암병동 AI 크리에이터 워크샵 (2026.5.5) 및 키즈 에듀케이션 상품 개발.

## 레포 구조

### 루트
- `meeting_notes/` — 회의록, 커리큘럼, 환경 체크리스트, 병원 문의 초안
- `kids_edu_vault/` — **Obsidian Vault (메인)**. 아래 구조 참조
- `src/` — 기술 구현 소스
- `tools/` — 조사·운영 보조 스크립트. `yeep-fetch/` = 국가 창업교육 자료(YEEP) 재수집 도구
- `build_teams.md` — 팀 빌드 관련
- `product-requirements-gap-plan.md` — PR과 구현 갭 분석
- `2026-04-12-mvp-dev-plan.md` — MVP 개발 계획

### kids_edu_vault/ (Obsidian Vault)

**볼트 하나 안에 목적이 다른 위키 트리가 두 개 있다.** 상세 규약은 `kids_edu_vault/CLAUDE.md`.

| 트리 | 목적 | 무엇이 쌓이나 |
|---|---|---|
| **`wiki/`** | **지금 굴러가는 사업을 실행한다** | 미팅·이해관계자·기술 결정·납품물·운영 절차 |
| **`curriculum_wiki/`** | **커리큘럼을 만들 지식을 축적**하고, 그 지식으로 만든 **커리큘럼을 축적한다** | 교수학습법·수업모형·근거 조사 → 활동 원자 → 완성된 트랙·지도안 |

> **어디에 쓸지 판정**: "이걸 3년 뒤 다른 강의를 만들 때도 볼 것인가?"
> 그렇다 → `curriculum_wiki/` · 아니다 → `wiki/` · 애매하면 → `wiki/`

#### `wiki/` — 사업 위키 (Mode C)

| 폴더 | 용도 |
|------|------|
| `wiki/intel/` | 경쟁사, 사례 연구, 병원 환경 조사 |
| `wiki/specs/` | 기술 명세 |
| `wiki/comms/` | 커뮤니케이션 자료 |
| `wiki/runbooks/` | 운영 매뉴얼 |
| `wiki/meta/` | 메타 문서 |
| `wiki/decisions/` | 의사결정 로그 |
| `wiki/stakeholders/` | 이해관계자 프로필 |
| `wiki/components/` | UI/UX 컴포넌트 |
| `wiki/deliverables/` | 납품물 |
| `wiki/concepts/` | 개념 정의 |
| `wiki/projects/` | 비교육 사업 문서 (HYROX 등) |
| `_templates/` | 사업 위키용 템플릿 10종 |

#### `curriculum_wiki/` — 커리큘럼 지식 위키

지식 → 부품 → 산출물이 위로 쌓이는 구조. 진입점: `curriculum_wiki/curriculum-index.md`

| 폴더 | 용도 | 층 |
|------|------|---|
| `methods/` | 교수학습 방법론 카드 + 국내 모형 지도 | 지식 |
| `research/` | 조사·근거 (문헌·통계) | 지식 |
| `gaps/` | 미해결 질문·조사 계획·승격 판정 | 지식 |
| `rules/` | 헌법·금지개입·배치제약·측정축·스키마 | **게이트** |
| `design/` | 지도안 규격·작성법·검증 | 규칙 |
| `activities/` | 활동 원자 (30~60분) | 부품 |
| `assets/` | 사전 생성 데이터셋·카드덱 | 부품 |
| `curricula/` | **완성된 트랙·지도안** | 산출물 |
| `_templates/` | 커리큘럼용 템플릿 4종 | |

라인 구분·`scope` 값·접두사 규칙은 `curriculum_wiki/rules/curriculum-schema.md` 가 정본이다.

`.raw/`(원본 참고 자료, 가공 전)는 **두 트리가 공유**한다.

#### 두 트리를 다룰 때

- 위키링크는 트리를 넘어 작동한다 (같은 볼트, 파일명 기준). 파일명은 볼트 전체에서 고유해야 한다
- **메타 파일은 공유하지 않는다**: `wiki/`는 `index`·`log`·`hot`. `curriculum_wiki/`는 인덱스 하나(`curriculum-index`)를 공유하되 **작업 파일은 라인별** — `curriculum-hot`·`curriculum-log`(11~16세) / `startup-hot`·`startup-log`(창업·IR)
- **`curriculum_wiki/` 안에는 라인이 둘 있고 폴더를 나누지 않는다.** `scope`(`common`|`edu-11-16`|`startup-ir`) + 파일명 접두사(`m-`·`kr-`·`ped-`·`edu-11-16-`·`startup-`·`ruling-`)로 구분한다. 헌법·방법론 카드 등 `common` 26건을 두 라인이 공유하므로 **라인은 축이지 트리가 아니다**
- **기존 스킬은 `wiki/` 경로를 하드코딩**하고 있다. 커리큘럼 작업 시 `kids_edu_vault/CLAUDE.md`의 라우팅 표가 스킬 본문보다 **우선**한다
- 사업 볼트 문서를 커리큘럼 판단으로 고치지 않는다. 차이는 `curriculum_wiki/` 쪽에 명시하고, 조직 문서 개정이 필요하면 `wiki/` 과제로 넘긴다
- **향후 커리큘럼 생성 스킬**은 `curriculum_wiki/`를 입력으로 읽는다. 규칙 문서를 스킬에 복사하지 않는다 — 복사하면 두 진실이 생긴다

## 설치된 Skills (.claude/skills/)

| Skill | 용도 |
|-------|------|
| `wiki` | 위키 페이지 생성/관리 |
| `wiki-query` | 위키 검색 |
| `wiki-ingest` | 외부 소스 ingest |
| `wiki-lint` | 위키 링크/포맷 검증 |
| `obsidian-cli` | Obsidian CLI 연동 |
| `obsidian-markdown` | Obsidian 마크다운 규칙 |
| `obsidian-bases` | Obsidian Bases 템플릿 |
| `save` | 파일 저장 |
| `canvas` / `json-canvas` | 캔버스 작업 |
| `autoresearch` | 자동 리서치 |
| `defuddle` | URL 컨텐츠 추출 |
| `tdd` | 테스트 주도 개발 |
| `worktree-parallel` | git worktree 병렬 작업 |

## Obsidian 마크다운 규칙

- 파일명: `kebab-case.md`
- 위키링크: `[[페이지명]]` 형식 사용
- 프론트매터: YAML 지원
- 태그: `#tag` 형식
- 템플릿: `_templates/` 폴더 참조
- `.raw/` 폴더의 자료는 가공 후 `wiki/` 로 이동
- **외부 저작물 원본은 저장소에 커밋하지 않는다.** 이 저장소는 **공개**다. 국가·기관 공개자료라도 공공누리 표시가 없으면 재배포가 아니라 내부 참조까지만 허용된다. `.raw/yeep/`(1.1GB)는 gitignore이며 **재수집 도구 `tools/yeep-fetch/`로 복원**한다. 볼트에는 우리가 쓴 분석만 남긴다

## Slash Commands
- `/wiki` — 새 위키 페이지 생성
- `/save` — 파일 저장
- `/wiki-query` — 위키 검색
- `/wiki-lint` — 링크/포맷 검증
- `/wiki-ingest` — 외부 소스 ingest
- `/pilot-deploy` — 파일럿 환경 배포 자동화 (의존성 설치 + Cloudflare quick tunnel + 서버 기동)

## 배포 구조 (현재)

**아키텍처**: 운영자 맥북 위에서 백엔드(uvicorn) + 프론트(next dev)를 띄우고, 각각 **Cloudflare Quick Tunnel**로 외부 노출. 별도 클라우드 호스팅 없음.

```
인터넷 ──▶ Cloudflare quick tunnel ──▶ 운영자 맥북
            │
            ├─ <fe-tunnel>.trycloudflare.com ──▶ localhost:3000  (next dev)
            └─ <be-tunnel>.trycloudflare.com ──▶ localhost:8000  (uvicorn)
```

| 컴포넌트 | 포트 | 명령 |
|---|---|---|
| FastAPI 백엔드 | 8000 | `uv run uvicorn main:app --host 0.0.0.0 --port 8000` (`src/backend/`) |
| Next.js 프론트 | 3000 | `npm run dev` (`src/frontend/`) |
| BE tunnel | — | `cloudflared tunnel --url http://localhost:8000` |
| FE tunnel | — | `cloudflared tunnel --url http://localhost:3000` |

### 핵심 파일 (gitignore 됨, 환경별 직접 작성)
- `src/backend/.env.local` — `ZAI_API_KEY`, `GEMINI_API_KEY`, `BACKEND_BASE_URL`, `ADMIN_PASSWORD`
- `src/frontend/.env.local` — `NEXT_PUBLIC_BACKEND_HTTP_URL`, `NEXT_PUBLIC_BACKEND_WS_URL`
- `src/frontend/public/_backend.js` — 런타임 백엔드 URL 오버라이드 (Cloudflare 터널 URL을 직접 박음). `_backend.example.js` 참고.

### 배포 절차
1. **자동**: `/pilot-deploy` 스킬 실행 → 모든 단계 자동.
2. **수동**: `kids_edu_vault/wiki/runbooks/deployment.md` 참조.

### 한계 (현재 운영 리스크)
- **Quick tunnel URL은 cloudflared 재시작마다 바뀜** — `_backend.js` / `BACKEND_BASE_URL` 갱신 필요.
- **맥 절전 들어가면 외부 접속 끊김** — 파일럿 당일은 절전 OFF 필수.
- **어카운트리스 정책** — 트래픽 패턴에 따라 Cloudflare가 차단할 수 있음 (40명 동시 접속은 검증 필요).
- **LLM 동시 처리 한계** — 현재 GLM-5 단독으로는 ~5~10명. 40명 부하 대응 전략은 [[llm-provider-scaling]] (ADR) + [[llm-scaling-test-plan]] (페이즈별 테스트).
- **정식 운영용 권장**: Cloudflare Named Tunnel + 본인 도메인. 파일럿 D-day 전에 전환 검토.
