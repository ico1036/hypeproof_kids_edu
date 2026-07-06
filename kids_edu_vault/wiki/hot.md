---
type: meta
title: "Hot Cache"
created: 2026-04-12
updated: 2026-07-06
tags:
  - meta/cache
---

# Hot Cache — 2026-07-06

최근 컨텍스트 스냅샷. 세션 시작 시 가장 먼저 읽을 것.

---

## 2026-06-21 — 주인님 확정 우선순위 (보아치과 트랙)

> 6/15 회의록 todo를 AI가 임의 P0~P3로 정렬한 것은 **할루시네이션**으로 기각됨. 아래가 주인님이 직접 지정한 정본 우선순위다.

1. **보아치과 커리큘럼 만들기 (웹사이트 카피 방향으로 전환)**
   - 위키 최신 보아치과 커리큘럼([[dental-website-workshop-detail-v1]])의 **핵심 가치는 복사**하고, **겉껍데기만 "잘 만든 홈페이지 카피하기"로 교체**한다.
   - 산출: [[dental-website-copyclone-v3]] (active). v2는 HypeProof DNA 누락으로 deprecated.
   - **v3 본체 4요소**: ①봉호 5블록+AI지휘관 서사+핵심 장면 ②7에셋 행동신호 관찰표(Q&A 측정 금지) ③오프닝 와우포인트 라이브 데모 ④boaclinic.com급 결과물(네이버예약·카카오·SNS 연동 + Cloudflare Pages 배포).
   - **2026-06-27 정정:** 보아치과 클로징은 부모/아이 강의처럼 성장/검증 대체불가로 끝내면 안 된다. 핵심 레슨은 원장이 자기 치과 홍보를 원하는 대로 직접 바꿀 자유도이며, 이를 가능하게 하는 두 기술이 Context Engineering과 Feedback Loop다.
   - **2026-06-27 포스터 v1 ingest:** 외부 고객용 포스터에서는 내부 용어를 걷어내고 `초반 설명과 재료 정리 → 직접 문구·구성·톤을 깎아가기 → 최종 홈페이지 초안으로 평가`로 표현한다. Source: [[boa-dental-ai-promo-race-poster-v1-20260627]], deliverable: [[boa-dental-ai-promo-race-poster-v1]].
   - **2026-06-29 회의록 ingest:** 수강자 아웃풋은 홈페이지 초안/공개 URL/Before-After/설명 카드/Loop Log/발표 경험이다. 우리만 가능한 것은 7 Assets 체화, [[hypeproof-studio]] 로그와 자동 리포트 seed, 레이스/경쟁/커뮤니티, 보아치과 원장 KOL화, 제품-교육-커뮤니티가 이어지는 디지털 서비스 경험이다. Source: [[2026-06-29-weekly-on-hypeproof]].
   - **2026-06-30 랜딩 메시지 정리:** 첫 화면은 `실제 배포 홈페이지를 가져간다`와 `Claude Code/Codex 등 도구와 무관하게 통하는 두 능력(맥락 설계, 피드백 감각)을 체화한다`를 동시에 보여준다. `HYROX`는 내부 비유로만 두고 외부 표현은 `실전 반복 훈련`, `몸에 익힌다`, `AI를 지휘하는 감각`으로 쓴다. Source: [[boa-dental-landing-message-20260630-source]].
   - **2026-07-06 2시간 큐시트 정본 ingest:** [[boa-dental-ai-homepage-cuesheet-20260706-spec]]는 발표/해커톤 감성을 제거한 외부 공유용 큐시트다. 메인강사는 보아치과 홈페이지를 만든다고 가정하고 스크린을 띄워 단계별로 진행하고, 수강생은 같은 단계에서 자기 병원 홈페이지를 만든다. 최종 결과물은 홈페이지/배포 URL/GitHub 저장소/`agent.md` 4개. Context Engineering은 URL만 넣은 결과와 병원 컨텍스트를 자세히 넣은 결과 차이 체감, Loop Engineering은 루브릭을 만족할 때까지 검사와 수정을 반복시키는 것이 핵심이다. 큐레이션 기준은 `*봉호님 작성 예정`으로 남긴다. Source: [[boa-dental-ai-homepage-cuesheet-20260706]].
2. **HypeProof Studio로 위 커리큘럼 운행 가능한지 기술문제 체크**
   - 블로커 후보: 이미지(타겟 스크린샷) 맥락 주입 UI 지원 여부, 멀티턴 연속성/메모 캐싱(6/15 회의 지적), 라이브 프리뷰·배포 exec.
   - 2026-06-29 회의에서 레드 시그널로 재확인: 리허설 전 [[hypeproof-studio]]와 [[claude-code]] 성능 격차를 테스트하고, 필요하면 Claude Code/스킬 기반 fallback을 준비한다.

---

## 2026-06-08 — SK바이오팜 커리큘럼 v2 재작성
- 제품 은유 업데이트: HypeProof Studio는 “커다란 게임기”, 아이는 그 안에서 “게임을 만드는 게임”을 플레이한다. 7 Assets는 내부 매핑이고, 아이에게는 퀘스트/뱃지/레벨업/출시 보상으로 보이게 한다.
- 정정: 7 Assets를 “평가/점수화”로 설명하면 봉호 커리큘럼을 해칠 수 있음. 봉호님 확인 전까지 외부 표현은 평가가 아니라 관찰 기록/성장 코멘트로 고정. 0/1/2 루브릭은 사용 금지.
- [[sk-biopharma-bongho-curriculum-v2]] 생성. 기준을 바로잡아 봉호 커리큘럼 원형을 최상단 본체로 두고, SK 제약조건과 HypeProof Studio 구현을 그 아래에 배치했다.
- 핵심 구조: 봉호 커리큘럼 = 교육 본체 / SK바이오팜 조건 = 운영 제약 / HypeProof Studio = 실행 OS.
- 한 줄 결론: SK바이오팜 수업은 HypeProof Studio 수업이 아니라, 봉호 커리큘럼을 HypeProof Studio로 구현한 가족 AI 게임 창작 수업이다.

## 2026-06-08 — SK바이오팜은 봉호 커리큘럼을 HypeProof Studio로 구현
- 주인님 결정: SK바이오팜 게임 만들기 수업은 [[hypeproof-studio]]로 해야 한다.
- 이유: 게임 제작에 특화된 스킬·룰·프롬프트를 Studio 안에 미리 깔아야 4시간 안에 완성률과 안전성을 확보할 수 있다.
- 생성: [[hypeproof-studio-game-skillpack-v1]]. 포함 내용은 Game Creation Skill, Rule Pack, Prompt Pack, Grade Mode(A/B), Coach Dashboard, 7 Assets 리포트 데이터.
- 확인: [[sk-biopharma-curriculum-detail-v1]]은 봉호 커리큘럼을 부분 적용한 상태였고, 2026-06-08에 봉호 5블록 코어/AI 지휘관/블록3 핵심/증거 수여 구조를 명시적으로 추가 반영함.
- 정정: 보아치과 성인 웹사이트 강의는 범용툴 중심 가능성이 있으나, SK바이오팜 키즈/가족 게임 랩은 봉호 커리큘럼을 Studio로 구현하는 것이 맞다.

## 2026-06-08 — 커리큘럼 상세 v1 산출
- [[sk-biopharma-curriculum-detail-v1]] 생성. SK바이오팜 20가족/23자녀, A반 초5·6 13명/B반 초3·4 10명 기준 4시간 Family AI Creation Lab 상세안. 핵심은 게임 수업이 아니라 7 AI Native Assets 행동 증거를 남기는 프리미엄 가족 AI 랩.
- [[dental-website-workshop-detail-v1]] 생성. 보아치과/치과 대상 홈페이지 만들기 강의 상세안. 1차는 [[claude-code]] 중심, [[hypeproof-studio]]는 Dental Website Skill Pack/교육 OS로 제품화하는 경로를 권장.
- 우선순위: 1) SK바이오팜 커리큘럼 상세 v1, 2) 보아치과 웹사이트 만들기 상세 v1. 둘 다 draft 상태이며 현장 테스트 필요.

## 2026-06-08 — SK바이오팜 내부 설문 일정/대상자 업데이트
- [[sk-biopharma-schedule-survey-20260608]] ingested. SK바이오팜 내부 설문 기준 수요는 **20가족 / 자녀 23명**으로 구체화됨.
- 분반안: **A반 5·6학년 13명**, **B반 3·4학년 10명**. 기존 학년별 분리 가정이 실제 인원 기반 운영안으로 이동.
- 일정 선호: **2026년 7월 또는 8월 토요일**, 20명 중 17명 선호. 예시로 7/11(토), 7/18(토) 가능 여부 확인 요청.
- SK바이오팜 요청: 분반 의견, 1st 13명/2nd 10명 기준 2회차 견적, 구성원 공유용 커리큘럼 세부 자료, 7~8월 가능 일정 회신.
- 병목: [[sk-biopharma-bitree-final-quotation-20260526]]는 10가족 1회 기준이므로 2회차/가변 인원 재견적과 커리큘럼 공유 자료가 필요.

## 현재 상태: SK바이오팜 파일럿 진입 + HypeProof Studio 개발 시작

### 가장 최근 작업 (2026-05-15)

**테스트 품질 3-Phase 개선 완료**
- Phase1: sys.path 잔재 삭제, anyio→asyncio 마커, tautology assertion 수정, fixture 중복 제거, 테스트명 수정
- Phase2: `test_card_node.py`·`test_spec_node.py` `_DATA_DIR` monkeypatch 파일시스템 격리
- Phase3: error 이벤트 테스트, 갤러리/rename/save 엔드포인트 커버리지, `backendUrl.test.ts` 신규(8개), `send()` 가드+payload 검증
- 현재 테스트: **111 BE + 19 FE = 130 tests 전체 통과**
- 상세: [[test-quality-review-2026-05-15]] (status: resolved)

**PR#7 `feature/langgraph-gemini` → main 머지 완료 (동일 세션)**
- ico1036 리뷰 3건 반영 + 이미 구현된 항목 코멘트 확인 처리
- 수정: `edit_code_node` 실패 피드백, `sys.path.insert` 7회→1회, [[langfuse-observability]] 시크릿 외부 주입, `.env.example` 추가
- main 현재 커밋: `75159ee`, 워크트리 및 `feature/langgraph-gemini` 브랜치 정리 완료

**[[sk-biopharma]] × [[bitree]] 파일럿 확정 (2026-05-14)**
- 대상: 약 15~20가족, 6~7월 토요일 Biweekly, [[sk-biopharma]] 10층 내부 카페
- 수업 단위: 4시간 × 2그룹/일

**HypeProof Studio v0.1 개발 결정**
- VS Code fork + 자체 chat panel (Track A / Track B 병렬)
- 5/28~30 dry-run이 Go/No-go 게이트

---

## 주요 임박 마일스톤

| 기한 | 내용 |
|---|---|
| 2026-05-15~30 | HypeProof Studio v0.1 빌드 |
| 2026-05-28~30 | 운영진 자녀 dry-run (4시간) — **게이트** |
| 2026-05-말 | [[sk-biopharma]] 수요조사용 제안서 제출 |
| 2026-06-01 | Studio v0.1 release + 가족 안내 메일 |
| 2026-06 (2~3주) | [[sk-biopharma]] 1회차 |

---

## 핵심 페이지

- [[test-quality-review-2026-05-15]] — 테스트 품질 검토 결과 (방금 생성)
- [[kids-edu-backend]] — 백엔드 컴포넌트 (LangGraph 구조 반영 업데이트)
- [[2026-05-12-sk-biopharma-meeting]] · [[2026-05-14-sk-biopharma-followup]]
- [[sk-biopharma]] · [[bitree]] · [[oh-sungeun]]
- [[hypeproof-studio]] · [[adr-hypeproof-studio-v01]] · [[sixteen-essence]]
- [[sk-biopharma-pilot]]

---

## 스택 요약

| 레이어 | 기술 |
|---|---|
| 백엔드 | FastAPI + [[langgraph]] + [[gemini-2-5-flash]] + SQLite |
| 프론트 | Next.js (App Router) |
| 관측성 | [[langfuse-observability]] v2 self-hosted |
| 교육 도구 | [[hypeproof-studio]] v0.1 (예정) / Cline (Plan B) |
| 테스트 | pytest 111개 (백엔드) · Vitest 19개 (프론트, 파일 2개) — 전체 통과 |

## 2026-05-21 — 치과 지식 슈퍼서치엔진 v4
- [[dental-supersearch-curriculum-v4]] — v3의 “원장님은 5분, 직원이 주인공” 구조를 유지하면서, 산출물을 검색 웹앱 + 원장님 검증 로그 + 병원 내부 검색 규칙으로 전환.
- [[dental-supersearch-engine-workshop-v2]] — “원장님을 이겨라” 게임 장치와 7 AI Native Assets를 검색스킬 제작 루프로 엮은 HTML 제안서/목업.


## 2026-06-07 — 치과 AI 홈페이지 만들기 세미나 피드백 ingest
- 주인님 정정 반영: [[dental-homepage-seminar-feedback-20260607]]는 [[boa-dental]] 이후 피드백이다. 사전 기획안이 아니라 현장 이후 개선 의견으로 취급.
- 핵심은 “각자 원하는 것 만들기”가 아니라 특정 샘플 치과 홈페이지를 그대로 따라 만드는 **요리교실식 세미나**.
- 새 스펙 [[dental-homepage-seminar-v1]] 생성. 목표 산출물은 로컬 시연이 아니라 [[vercel]]/[[cloudflare]] 등으로 실제 공개 URL까지 띄우는 것.
- 강사 측이 데모 로고·이미지·콘텐츠 에셋을 미리 준비해야 한다. 참가자 준비물 의존은 초심자 이탈/누락 리스크.
- 기술/가치 제안: [[gabia]] 도메인만 구매 + [[claude-code]] 제작 + 무료/저비용 배포. [[cafe24]]/홈페이지 외주 관리비 구조 대비 수시 수정 가능성을 강조.
- 중간 교육은 토큰/프롬프트/수정 요청법 같은 AI 개념을 “양념”처럼 삽입하고, 본 흐름은 완주 경험 중심으로 유지.

## 2026-06-01 — SK바이오팜 Bitree 최종 견적서
- [[sk-biopharma-bitree-final-quotation-20260526]] ingested. 4시간/10가족 1회차 기준 공급가 920만원, VAT 포함 1,012만원. 가족당 VAT 포함 101.2만원.
- 기존 [[sk-biopharma-pilot]]의 40~60만원/가족 검토가보다 높으므로, 단순 키즈 코딩 수업이 아니라 HypeProof Studio + 부모-자녀 페어 + 7/16 역량 리포트 + high-touch 전문가 코칭으로 포지셔닝해야 한다.

## 2026-06-01 — 7 AI Native Assets 전략 업데이트
- [[seven-ai-native-assets-sk-strategy]] saved. SK바이오팜/Bitree 제안서는 7 AI Native Assets를 새 단일 커리큘럼 기준으로 삼는다. 게임은 목적이 아니라 7 Assets를 훈련하는 프로젝트 매개다.
- 가격 방어의 핵심은 `키즈 코딩 수업`이 아니라 `10가족 한정 premium family AI lab + HypeProof Studio + 7 Assets 성장 리포트`다.
- Assistant Instructor 명칭은 `AI Builder Coach` / `Family Project Coach`로 바꿔야 한다.

- **7 Assets 원본 확인(2026-06-01):** [[seven-ai-native-assets-original]] 기준, Q&A는 교육/경계선 선언용이고 측정은 프롬프트 구조·수정 패턴·검증 행동·회고 언어 등 과정 신호에서 해야 한다. SK바이오팜 게임 랩은 게임 완성보다 7 Assets 행동 증거 수집이 핵심.
