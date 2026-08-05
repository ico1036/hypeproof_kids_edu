---
type: meta
title: "Lint Report 2026-08-05"
created: 2026-08-05
updated: 2026-08-05
tags:
  - meta
  - lint
status: developing
---

# Lint Report: 2026-08-05

PR #12·#13·#14·#16 머지 직후 볼트 헬스체크. 직전 리포트는 [[lint-report-2026-05-21]].

## Summary
- Pages scanned: 223 (`kids_edu_vault/wiki/**/*.md`)
- Issues found: 82 (초기 집계 84 중 2건은 오탐 — 아래 참조)
- Auto-fixed: 82
- Needs review: 0

| 항목 | 건수 | 심각도 | 처리 |
|---|---|---|---|
| 프론트매터 소실 ([[log]]) | 1 | 높음 | ✅ 수정 |
| 데드링크 — 말줄임 링크 | 4곳 | 중간 | ✅ 수정 |
| 고아 페이지 | 2 | 중간 | ✅ 등록 |
| 데드링크 — `.html` 참조 | 1 (4곳 인용) | 중간 | ✅ md 스텁 생성 |
| 파일명 규칙 위반 | 3 | 낮음 | ✅ 리네임 |
| 프론트매터 `title` 누락 | 71 | 낮음 | ✅ H1에서 채움 |
| 중복 파일명 (`skin.md`) | 1쌍 | 낮음 | ✅ 분리 |
| ~~`[[services]]` · `[[mounts]]`~~ | 2 | — | ❌ 오탐 (코드펜스 내 TOML) |

---

## 프론트매터 소실 — 회귀

✅ **수정 완료** — [[log]] — YAML 프론트매터가 통째로 사라지고 `## [2026-07-11] ingest ...` 로 시작한다. `b034629` (PR #12) 에서 발생. 로그 항목 자체는 583→717줄로 보존됐고 헤더만 유실됐다.
  - 복구: `type: meta` / `title: "Log"` / `created: 2026-04-12` / `updated: 2026-08-05` / `tags: [meta/log]` + `# Log` 헤딩 재삽입
  - [[hot]], [[index]] 는 정상.

## Dead Links

✅ **수정 완료** — `[[2026-05-12-sk-bio…ting]]`, `[[2026-05-14-sk-bio…owup]]` — 위키링크 이름이 **말줄임표(`…`)로 잘린 채** 저장돼 있다. ingest 도구가 이름을 truncate 한 것으로 보임. 각각 [[2026-05-12-sk-biopharma-meeting]], [[2026-05-14-sk-biopharma-followup]] 로 복구 필요.
  - 출현: `concepts/seven-ai-native-assets-sk-strategy.md` (L15–16), `sources/sk-biopharma-bitree-final-quotation-20260526.md` (L13–14) — 둘 다 프론트매터 `related` 필드
- `[[dental-supersearch-engine-workshop-v2]]` — 실제 파일은 `specs/track-b/dental-supersearch-engine-workshop-v2.**html**` 이라 위키링크로 해석되지 않는다. [[hot]], [[log]], [[index]], `specs/track-b/_index.md` 4곳에서 참조.
  - ✅ **수정 완료** — 같은 폴더에 `dental-supersearch-engine-workshop-v2.md` 스텁을 만들고 HTML을 related artifact로 걸었다. 기존 링크 4곳은 그대로 해석된다. 방식: HTML은 artifact로만 두고 링크 텍스트를 코드/경로 표기로 바꾸거나, 설명용 md 스텁을 만들고 HTML을 related로 건다 ([[hypeproof-hyrox-framework-v1]] 이 쓰는 방식).
❌ **오탐 취소** — `[[services]]`, `[[mounts]]` ([[adr-container-deployment]] L99·L106) 은 위키링크가 아니라 **코드펜스 안 fly.toml의 array-of-table 문법**이다. 스캐너가 ``` 블록을 제외하지 않아 생긴 오탐. 수정하지 않았다. 차기 lint 스크립트는 코드펜스를 건너뛰어야 한다.

> 과거 lint 리포트(`lint-report-2026-05-15`, `-05-21`) 안의 끊긴 링크 12종은 리포트가 인용한 이름이라 집계에서 제외했다.

## Orphan Pages

✅ **수정 완료** — [[sk-biopharma-family-workshop-design-v1]] — inbound 0 + **프론트매터 없음**. PR #12에서 레포 루트 `SKBP-family-workshop-design-v1.md` 를 볼트로 옮기며 들어왔는데 index 등록과 헤더가 빠졌다. `deliverables/_index.md` + [[index]] 등록, 프론트매터 추가 필요.
✅ **수정 완료** — [[sk-biopharma-7assets-proposal-upgrade-20260601]] — inbound 0 이었다. [[index]] + `deliverables/_index.md` 의 새 "Proposals & Design" 구역에 등록.

> [[dashboard]], [[lint-report-2026-05-21]] 도 inbound 0이지만 meta 문서라 의도된 고립으로 판단, 제외.

## 파일명 규칙 위반

프로젝트 규칙은 `kebab-case.md` (CLAUDE.md). 위반 3건:

- `specs/track-b/치과의사-curriculum-v1.md` (status: archive)
- `specs/track-b/치과의사-curriculum-v2.md` (status: archive)
- `specs/track-b/치과의사-curriculum-v3.md` (status: **active**)

v3은 현행 문서라 rename 시 [[index]]·`_index`·본문 링크를 함께 고쳐야 한다. v1은 PR #13에서 kebab 이름으로 바꾸려다 중복 문제로 main 최신본을 유지하기로 정리된 건이라, 리네임한다면 3개를 한 번에 처리하는 게 낫다.

> 스킬 문서의 "Filenames: Title Case with spaces" 표기는 이 볼트에 맞지 않는다 (CLAUDE.md의 kebab-case가 우선). 스킬 쪽 표를 고치는 것도 후속 과제.

## Frontmatter Gaps

- `title` 누락 71개 — 대부분 초기 ingest 시기 페이지(`intel/environ-kukrip-amsenter`, `specs/pilot-env-design`, `specs/production-loop`, `comms/2026-01-26-meeting` 등). `type`/`status`는 있어서 Dataview 동작에는 지장 없지만, 표 뷰에서 제목 컬럼이 비어 보인다.
- `created` 누락 1개.
- 프론트매터 전무 2개 — [[log]](위 회귀), [[sk-biopharma-family-workshop-design-v1]].

## 중복 파일명

- `specs/skins/adult/skin.md` · `specs/skins/kids/skin.md` — 같은 stem. Obsidian에서 `[[skin]]` 이 어느 쪽으로 갈지 불확정. `skin-adult.md` / `skin-kids.md` 로 분리 권장.
- `_index.md` 18개는 폴더 인덱스 규약이라 정상 (참조는 `[[intel/_index|_index]]` 처럼 경로 포함으로 되어 있음).

## Stale Index Entries

[[index]] 에서 실제 파일과 어긋난 항목은 위 `dental-supersearch-engine-workshop-v2` 1건 외에 없음. PR #13·#16 머지 시 Track B / Projects 목록이 양쪽 병합으로 처리되어 누락 없음.


---

## 이번 세션 자동 수정 내역 (7곳 / 5파일)

| 파일 | 수정 |
|---|---|
| `wiki/log.md` | 프론트매터 + `# Log` 헤딩 복구 |
| `wiki/sources/sk-biopharma-bitree-final-quotation-20260526.md` | 말줄임 위키링크 2곳 복구 |
| `wiki/concepts/seven-ai-native-assets-sk-strategy.md` | 말줄임 위키링크 2곳 복구 |
| `wiki/deliverables/sk-biopharma-family-workshop-design-v1.md` | 프론트매터 신규 추가 |
| `wiki/index.md` · `wiki/deliverables/_index.md` | 고아 2건 등록, Deliverables 카운트 13→15 |

재실행 결과: 고아 4→1 (남은 1건은 이 리포트 자신), 실질 데드링크 5→1 (`dental-supersearch-engine-workshop-v2`, 오탐 2건 제외).

## 2차 수정 내역 (후속 과제 전량 처리)

| 항목 | 처리 |
|---|---|
| `.html` 참조 | `specs/track-b/dental-supersearch-engine-workshop-v2.md` 스텁 신규 생성 (HTML은 related artifact) |
| 한글 파일명 3건 | `치과의사-curriculum-v1/v2/v3.md` → `dental-doctor-curriculum-v1/v2/v3.md`, 참조 12파일 갱신 |
| `title` 누락 71건 | 각 페이지 H1 헤딩에서 추출해 `type:` 바로 아래 삽입 (71/71 H1 보유) |
| `skin.md` 중복 | `skin-adult.md` / `skin-kids.md` 로 분리, 경로형 링크 4파일 갱신 |
| `created` 누락 1건 | `sources/boa-dental-ai-homepage-cuesheet-20260706.md` |

## 최종 상태 (재스캔, 코드펜스·첨부 제외 스캐너)

| 지표 | 최초 | 최종 |
|---|---|---|
| 페이지 | 223 | 225 |
| 고아 | 4 | 1 (이 리포트 자신) |
| 실질 데드링크 | 5 | **0** |
| 프론트매터 결함 | 74 | **0** |
| 중복 파일명 | 1쌍 | **0** |

## 남은 후속 과제

- lint 스크립트 자체는 레포에 남기지 않기로 함 (매 실행 시 작성). 다음 실행 시 **코드펜스 제외**와 **`_attachments` 제외**를 반드시 넣을 것 — 이번 오탐 2건(`[[services]]`·`[[mounts]]`)과 첨부 오탐 2건의 원인.
- `wiki-lint` 스킬 문서의 "Filenames: Title Case with spaces" 표기는 이 볼트 규칙(kebab-case)과 충돌 — 스킬 쪽 수정 필요.
