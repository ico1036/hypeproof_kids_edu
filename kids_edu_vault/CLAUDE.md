# HypeProof Kids Edu: LLM Wiki

Owner: JY (신진용)
Created: 2026-04-12

**이 볼트에는 목적이 다른 두 개의 위키 트리가 있다.** 어느 쪽에 쓸지부터 정하고 시작할 것.

---

## 두 트리 — 용도 차이

| | `wiki/` — 사업 위키 | `curriculum_wiki/` — 커리큘럼 지식 위키 |
|---|---|---|
| **모드** | C (Business / Project) | E 변형 (Research + 산출물 축적) |
| **목적** | **지금 굴러가는 사업을 실행**한다 | **커리큘럼을 만들 지식을 축적**하고, 그 지식으로 만든 **커리큘럼을 축적**한다 |
| **시간 축** | 특정 시점의 프로젝트·미팅·결정 | 시점에 덜 매인 지식. 오래 쓴다 |
| **무엇이 쌓이나** | 미팅·이해관계자·기술 결정·납품물·운영 절차 | 교수학습법·수업모형·근거 조사 → 활동 원자 → **완성된 트랙·지도안** |
| **누가 읽나** | JY·Jay·팀. 실행 판단 | 커리큘럼 설계자·강사. 그리고 향후 **커리큘럼 생성 스킬** |
| **폐기 주기** | 프로젝트가 끝나면 아카이브 | 반증되기 전까지 유지. 갱신하며 축적 |

### 한 줄 판정

> **"이걸 3년 뒤 다른 강의를 만들 때도 볼 것인가?"**
> 그렇다 → `curriculum_wiki/` · 아니다 → `wiki/`

### 활용 케이스

| 상황 | 트리 | 위치 |
|---|---|---|
| 교수학습법 논문·문헌을 조사했다 | `curriculum_wiki/` | `research/` |
| 수업 모형을 정리해 재사용 자산으로 만든다 | `curriculum_wiki/` | `methods/` |
| 강의를 만들 때 지켜야 할 규칙을 정한다 | `curriculum_wiki/` | `rules/` `design/` |
| 활동 하나를 원자로 설계한다 | `curriculum_wiki/` | `activities/` |
| **완성된 커리큘럼·지도안을 남긴다** | `curriculum_wiki/` | `curricula/` |
| SK바이오팜 미팅 결과를 정리한다 | `wiki/` | `comms/` |
| 백엔드 아키텍처를 결정했다 | `wiki/` | `decisions/` |
| 파일럿 당일 운영 절차를 쓴다 | `wiki/` | `runbooks/` |
| 병원 현장 환경을 조사했다 | `wiki/` | `intel/` |
| 경쟁사·시장 조사인데 커리큘럼 가격 근거다 | `curriculum_wiki/` | `research/` |
| 파트너 계약 조건을 정리한다 | `wiki/` | `decisions/` |

**애매하면 `wiki/`에 쓴다.** 나중에 지식으로 승격하는 편이, 사업 맥락이 지식 위키를 오염시키는 것보다 낫다.

### 두 트리를 잇는 규칙

- **위키링크는 트리를 넘어 작동한다** (같은 Obsidian 볼트, 파일명 기준). 필요하면 인용한다
- **`.raw/`는 공유한다.** 원자재를 두 곳에 두면 원본이 흐려진다
- **메타 파일은 절대 공유하지 않는다.** `wiki/`는 `index`·`log`·`hot`. `curriculum_wiki/`는 인덱스 하나(`curriculum-index`)를 공유하되 **작업 파일은 라인별**이다 — `curriculum-hot`·`curriculum-log`(11~16세) / `startup-hot`·`startup-log`(창업·IR). 섞으면 한쪽 맥락이 다른 쪽을 밀어낸다
- **사업 볼트 문서를 커리큘럼 판단으로 고치지 않는다.** 차이가 생기면 `curriculum_wiki/` 쪽에 명시하고, 조직 문서 개정이 필요하면 `wiki/` 과제로 넘긴다

---

## Structure

```
kids_edu_vault/
├── .raw/                      # 원본 소스 (immutable). 두 트리 공유. 수정 금지
│   └── yeep/                  # ⛔ gitignore. KOEF·교육부 저작물 → tools/yeep-fetch/ 로 재수집
├── _templates/                # 사업 위키용 템플릿 10종
├── _attachments/  exports/
├── wiki/                      # ── 사업 위키 (Mode C)
│   ├── index.md  log.md  hot.md  overview.md
│   ├── stakeholders/          # 사람·조직·의사결정자
│   ├── decisions/             # 단일 결정 + 근거·날짜 (ADR)
│   ├── deliverables/          # OKR·마일스톤·작업
│   ├── intel/                 # 외부 조사·현장 맥락
│   ├── comms/                 # 미팅·스레드 합성 요약
│   ├── specs/                 # 설계 문서 (복합 결정 묶음)
│   ├── components/            # 기술 스택 컴포넌트별 페이지
│   ├── runbooks/              # 배포·당일 운영 절차
│   ├── concepts/              # 조직 맥락 용어·프레임워크
│   ├── sources/               # wiki-ingest 자동 관리
│   ├── questions/             # wiki-query 자동 파일링
│   ├── validation/            # QA·검증 결과
│   ├── projects/              # 비교육 사업 문서 (HYROX 등)
│   └── assets/                # 디자인·콘텐츠 자산
│
├── curriculum_wiki/           # ── 커리큘럼 지식 위키
│   ├── curriculum-index.md          (공용 카탈로그)
│   ├── curriculum-hot.md  curriculum-log.md   (11~16세 라인)
│   ├── startup-hot.md     startup-log.md      (창업·IR 라인)
│   ├── _templates/            # 커리큘럼용 템플릿 4종
│   ├── methods/               # 교수학습 방법론 카드 + 국내 모형 지도   [지식]
│   ├── research/              # 조사·근거 (ped-*)                      [지식]
│   ├── gaps/                  # 미해결 질문·원문 미확보·승격 판정       [지식]
│   ├── rules/                 # 헌법·금지개입·배치제약·측정축·스키마    [게이트]
│   ├── design/                # 지도안 규격·작성법·검증                [규칙]
│   ├── activities/            # 활동 원자 (30~60분)                    [부품]
│   ├── assets/                # 사전 생성 데이터셋·카드덱              [부품]
│   └── curricula/             # ★ 완성된 트랙·지도안                   [산출물]
└── CLAUDE.md                  # 이 파일
```

### `wiki/` 폴더 선택 가이드

| 기록할 내용 | 폴더 | 예 |
|---|---|---|
| 사람/조직 | `stakeholders/` | JY, Jay, TJ |
| 개별 결정 + 근거 | `decisions/` | 디스코드 사용, 미팅 시간 |
| 여러 결정의 집합 / 설계도 | `specs/` | 파일럿 실행환경 설계 |
| 기술 도구 하나 | `components/` | code-server, Caddy |
| 해야 할 일 / OKR | `deliverables/` | API Key 발급, 리허설 |
| 운영 절차 | `runbooks/` | 당일 배포, 장애 대응 |
| 조직/개발 용어 | `concepts/` | Mission Driven, 트랙 A/B |
| 외부 자료·현장 체크 | `intel/` | 병원 장소 정보 |
| 미팅 합성 요약 | `comms/` | 2026-01-05-meeting |
| 비교육 사업 문서 | `projects/` | HYROX 제안서, 외부 세션 |
| 디자인·콘텐츠 자산 | `assets/` | 16원칙 assets v0.1 |
| QA·검증 테스트 결과 | `validation/` | E2E 결과, 에지케이스 로그 |
| ingest 소스 요약 | `sources/` | wiki-ingest 자동 생성 — 직접 생성 금지 |
| 쿼리 응답 아카이브 | `questions/` | wiki-query 자동 파일링 |

### `curriculum_wiki/` 폴더 선택 가이드

| 기록할 내용 | 폴더 | 예 |
|---|---|---|
| 교수학습 방법론 (재사용 자산) | `methods/` | 안내된 발견, POE, 협동학습 |
| 조사·근거 (문헌·통계) | `research/` | 청소년 인지발달, 국내 AI 사용 실태 |
| 미해결 질문·조사 계획·승격 판정 | `gaps/` | 조사 계획, 원문 미확보 목록 |
| 절대 어기면 안 되는 것 | `rules/` | 헌법, 배치 제약, 측정 축, 스키마 |
| 지도안을 어떻게 쓰나 | `design/` | 작성법, 품질 체크리스트 |
| 30~60분 단위 활동 | `activities/` | 표본 분류, 반박 사다리 |
| 사전 준비물 | `assets/` | 표본 데이터셋, 카드덱 |
| **완성된 강의 한 벌** | `curricula/` | Self Compass 4주 트랙, 지도안 |

---

## `curriculum_wiki/` 필수 규칙

진입점: `curriculum_wiki/curriculum-index.md`

- **모든 노트에 `ip_owner` 필수.** 기본값 `unverified`. 판정 없이 `hypeproof`로 올리지 않는다 → `rules/curriculum-schema.md`
- **헌법(`rules/edu-constitution.md`)은 참고 지침이 아니라 게이트.** 위반하면 산출물을 폐기한다. 변경은 승인 사안
- **지도안 작성 전 `design/lesson-plan-authoring-guide.md` 필독.** 작성 순서: **증거 → 성취기준 → 본질적 질문 → 금지 개입 → 활동 → 연결**
- **근거를 다룰 때 `methods/evidence-standards.md`를 따른다.** 효과크기로 방법을 서열화하지 않는다. 큰 효과크기는 의심 신호다
- **`.raw` 원자재를 자산으로 승격할 때 `gaps/`에 판정 기록**을 남긴다
- **메타 파일 이름에 접두사를 붙인다.** 위키링크가 파일명 기준이라 `index`·`log`·`hot`은 `wiki/`와 충돌한다
- 지식은 `methods`/`research`, 규칙은 `rules`/`design`, 산출물은 `curricula`. **섞지 않는다**
- **모든 노트에 `scope` 필수**: `common` | `edu-11-16` | `startup-ir`. **파일명 접두사가 `scope`와 모순되면 오류** → `rules/curriculum-schema.md`

### 라인은 폴더를 나누지 않는다 — `scope`로 나눈다

이 트리에는 라인이 둘 있다(11~16세 AI 교육 / 고등학생 창업·IR). **폴더를 쪼개지 않는다.**

| 라인 | `scope` | 접두사 | 작업 파일 |
|---|---|---|---|
| 11~16세 | `edu-11-16` | `edu-11-16-` `ped-` | `curriculum-hot` · `curriculum-log` |
| 창업·IR | `startup-ir` | `startup-` | `startup-hot` · `startup-log` |
| **공유 자산** | **`common`** | `m-` `kr-` 또는 없음 | 라인 로그에 기록 |

> **왜**: 두 라인은 `common` 26건(헌법·금지개입·방법론 카드 8종·국내 모형 5종·지도안 규격·근거 등급)을 **공유한다.** 복사하면 두 진실이 생기고, 참조하면 이름만 분리다. **라인은 축이지 트리가 아니다.**

- **`common` 문서를 한 라인의 필요로 고치려 할 때 멈춘다.** 그건 라인 전용 문서를 새로 만들라는 신호다
- 라인 전용 작업은 **그 라인의 `hot`·`log`에만** 기록한다. `common` 자산 변경은 `curriculum-log`에 남긴다
- 라인이 늘어나면 `scope` 값과 접두사, 그리고 `<line>-hot`·`<line>-log` 한 쌍을 추가한다. **폴더는 그대로 둔다**

---

## Conventions (두 트리 공통)

- 모든 노트는 YAML frontmatter 필수: `type`, `status`, `created`, `updated`, `tags` (최소)
- Wikilink는 `[[Note Name]]` 형식. **파일명은 볼트 전체에서 고유해야 한다** — 두 트리를 합쳐도
- `.raw/` 안의 원본은 절대 수정 금지
- **외부 저작물 원본은 커밋하지 않는다.** 이 저장소는 **공개**다. 국가·기관 공개자료라도 공공누리(KOGL) 표시가 없으면 내부 참조·연구·비평까지만 허용되고 **공개 저장소 게시는 재배포**다. `.raw/yeep/`(1.1GB, KOEF·교육부 저작물)는 gitignore이며 `tools/yeep-fetch/`로 재수집한다. 볼트에는 **우리가 쓴 분석만** 남기고 인용은 출처를 밝혀 필요한 범위로 제한한다
- 각 트리의 `index`는 마스터 카탈로그: 문서 추가마다 갱신
- 각 트리의 `log`는 추가 전용: 과거 엔트리 수정 금지. 새 로그는 **최상단**
- 각 트리의 `hot`은 500단어 이내 캐시: 작업 끝날 때 **완전히 덮어쓸 것**(저널 아님)
- 날짜는 `YYYY-MM-DD` 만 사용 (ISO datetime 금지)
- YAML 안의 wikilink는 반드시 따옴표: `- "[[Page]]"`
- **파일명**: `kebab-case`. wiki-lint 기본값("Title Case")과 다름 — 의도적 채택. lint의 naming 항목은 false positive로 무시
- **sources/ · questions/**: 스킬이 자동 관리. 직접 생성 금지

---

## 외부 저장소 정본을 인용할 때

`.raw/`에 없는 문서 — 다른 저장소의 정본(`hypeprooflab/MISSION.md` 등) — 을 근거로 쓸 때의 규약이다.

- **인용 전 `git fetch`를 먼저 한다.** 로컬 체크아웃이 낡았는지부터 확인한다.
  > 2026-08-30에 `hypeprooflab`이 **855 커밋 뒤처진** 상태였고 마지막 fetch가 8/2였다. 그 결과 8/29 작업 전체가 **폐기된 7/31판** 위에서 이뤄졌고, 볼트의 정본 미러가 `status: canonical`을 달고 틀린 문장을 싣고 있었다.
  > **오래된 체크아웃은 없는 것보다 나쁘다 — 확신을 주기 때문이다.**
- **읽은 대상을 명시한다.** 로컬이 아니라 `origin/main`을 읽었으면 그렇게 적는다.
- **manifest 키는 `<repo>:<path>` 형식.** 절대경로를 쓰지 않는다 — 머신이 바뀌면 깨진다. `source_ref`에 `origin/main@<short-sha>`를 함께 남긴다.
- **볼트에 만드는 것은 미러다.** 미러에서 먼저 고치지 않는다. 원본이 개정되면 미러를 갱신하고, 개정 사실을 소스 페이지로 남긴다.
- **정본이 개정되면 그것을 인용한 문서를 전수 점검한다.** 낡은 인용이 남으면 정본 규칙("충돌 시 정본이 이긴다")에 의해 그 문서가 스스로 진다.

## Operations

### 스킬 라우팅 — 중요

기존 스킬(`wiki-ingest`, `wiki-query`, `wiki-lint`, `autoresearch`, `save`)은 **`wiki/` 경로를 하드코딩**하고 있다. 즉 기본 동작은 사업 위키를 향한다.

> **커리큘럼 관련 작업일 때는 이 CLAUDE.md의 라우팅이 스킬 본문의 경로 지시보다 우선한다.**

| 작업 | 스킬 기본 | 커리큘럼 작업 시 |
|---|---|---|
| 소스 ingest | `wiki/sources/` + `wiki/concepts/` | **`curriculum_wiki/research/`** (조사) 또는 **`methods/`** (방법론 자산) |
| autoresearch 산출 | `wiki/sources/` + `wiki/concepts/` | **`curriculum_wiki/research/`** |
| 인덱스 갱신 | `wiki/index` | **`curriculum-index`** (라인 무관 공용) |
| 로그·캐시 갱신 | `wiki/log·hot` | **해당 라인의 `hot`·`log`** — 11~16세는 `curriculum-*`, 창업·IR은 `startup-*` |
| query 읽는 순서 | `wiki/hot` → `wiki/index` | **해당 라인 `hot` → `curriculum-index`.** 라인이 불명확하면 두 `hot` 모두 읽는다 |

**lint 한계**: `rules/curriculum-schema.md`의 lint 규칙 12개(`ip_owner`, `guidance` 3필드 등)는 `wiki-lint` 스킬에 구현되어 있지 않다. 규칙 준수는 사람과 CLAUDE.md가 책임지고, **자동 검출은 향후 커리큘럼 스킬에서 구현**한다.

### 명령

- **Ingest**: `.raw/`에 원본 드랍 → "ingest [파일명]"
- **Query**: `/wiki-query` 또는 "what do you know about X"
- **Lint**: `/wiki-lint` → 깨진 링크·고아 페이지·frontmatter 누락
- **Save**: `/save` → 대화/인사이트를 구조화 노트로 저장
- **Archive**: 오래된 원본은 `.archive/`로 이동

---

## 향후 — 커리큘럼 생성 스킬

`curriculum_wiki/`는 **향후 만들 커리큘럼 생성 스킬의 입력**이다. 그 스킬은:

- `methods/`에서 방법을 고르고 (선택 가이드: `methods/methods-index.md`)
- `rules/`를 게이트로 통과시키고 (헌법 · 배치 제약 · 측정 축)
- `activities/`의 원자를 조립해
- `curricula/`에 트랙·지도안을 출력한다

**따라서 규칙 문서를 스킬에 복사하지 않는다.** 스킬은 위키에서 읽는다. 복사하면 두 진실이 생기고, 조사 결과가 규칙을 바꿀 때 한쪽만 갱신된다.

## 입력 자료 (프로젝트 루트)

- `meeting_notes/*` — 주간 미팅·OKR
- `build_teams.md` — subagent 설계 지시서

필요 시 `.raw/`에 복사한 뒤 ingest. 원본은 그대로 둠.
