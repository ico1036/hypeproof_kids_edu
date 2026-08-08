---
type: meta
title: "Hot"
created: 2026-04-12
updated: 2026-08-08
tags:
  - meta/hot
---

# Hot — 최근 컨텍스트 캐시

> 500단어 이내. 매 세션 끝·ingest 후 완전히 덮어쓴다.

## 지금 하는 일 (2026-08-08)

브랜치 `docs/ai-edu-11-16-materials`. **11~16세 AI 교육 자산 레이어 스캐폴드 완료.**

Jay 개요(AI Compass 가족 라인: Self Compass 11~13세 4주 240만 / Builder Portfolio 14~16세 8주 480만 / Parent AI Dialogue 100만 / Annual Renewal 240만 + 헌법 5조)를 근거로 6개 결정을 내리고 `wiki/curriculum/` 을 세웠다.

## 핵심 설계

**강의 한 벌을 통짜로 쓰지 않는다.** 활동 원자(`activities/`)를 수업모형(`models/`)으로 조립하고, 배치 제약(`constraints/`)이 검증하고, 헌법·금지개입(`guardrails/`)이 게이트를 건다. "강의 한 벌"은 컴파일 인스턴스(`tracks/`)일 뿐이다. 목표는 강의가 아니라 **강사가 자기 상황에 맞게 조립할 수 있는 상태**. → [[curriculum-schema]]

## 내려진 결정

- **트랙 구조** — 긴 시퀀스를 자르지 않고 상품별 독립 완결 트랙. 상품명이 트랙 정체성을 규정하며, 자기 조절은 Self Compass에 속한다 → [[edu-11-16-track-architecture]]
- **부모 트랙 IP** — 파트너 소유. 우리는 접합면만. `ip_owner` 필드로 기계 분리 → [[edu-11-16-parent-track-ip-boundary]]
- **측정** — HYROX 4축 정본 + **5번째 축(거리·자기조절)** 신설. 합성 단일 점수 금지 → [[measurement-axes]]
- **랭킹** — 가족 라인 무순위. 헌법 B-1로 명문화 (경기·성인 라인은 원본 유지)
- **관찰 기록** — Sediment 자동 수집이 정본, 1기는 TA 폴백 → [[edu-11-16-evidence-capture]]
- **회차 포맷** — 잠정 110분 × 2 + 20분. 조사가 확정 (`provisional`) → [[edu-11-16-session-format]]

## 오버라이드 프로토콜 (신설)

기존 위키 문서가 틀리거나 이 라인에서 다를 때 **원본 본문은 안 건드리고** 관계만 선언한다. 3분류: `correction`(원본이 틀림 → upstream) / `scoped-variant`(맥락 차이 → 영구 분기) / `quarantine`(근거 미확인 → 사용 정지). 원본에는 frontmatter `has_overrides: true` 만 부착. → [[override-protocol]]

`.raw` 원자재 승격은 별도 경로(ingest-ruling). 첫 판정: 프로파일 기반 차별화를 **행동 기반**으로 변환 — 헌법 A-1 위반 소지 → [[ruling-profile-based-differentiation]]

## 지도안

작성 순서가 서술 순서와 다르다: **증거 → 성취기준 → 본질적 질문 → 금지 개입 → 활동 → 나머지.** 금지 개입을 활동보다 먼저 쓰는 것이 이 라인 고유. 3관문 검증(헌법 / 구조 / 실행가능성). → [[lesson-plan-authoring-guide]] · [[lesson-plan-quality-checklist]]

## L0 사이클 ① 완료 (2026-08-08) — 5건 중 2건 기각

- ❌ **"형식적 조작기 11~12세 시작"** — CSMS(9~16세 12,000명)로 반증. 16세의 약 30%만 초기 형식적 추론. 투트랙은 유지, 근거는 점진적 발달로 교체. **Lv2를 추상 과제 중심으로 설계하면 다수가 실패한다** → [[ped-adolescent-cognitive-development-verification]]
- ❌ **"5명 중 1명 거의 매일"** — 국내 근거 없음. 해외 수치 혼선(19% 용도 / 11.4% / 30%). 세일즈에서 제거
- ⚠️ **94.4% / 75.3%** — 초록우산, 2026-04, **만 14세 이상** 3,300명. **Lv1(11~13)에 적용 불가.** 75.3%는 "행동으로 옮겼거나 진지하게 고려" → [[ped-youth-ai-chatbot-statistics-verification]]
- ✅ **자기평가 정확도** 지지됨 → 거리 축은 자기보고 단독 지표 금지, 회고형 질문 금지
- ⛔ **Gemini는 Family Link 감독 계정으로 13세 미만도 가능.** `.raw`의 "Lv1 아동 계정 없음" 전제가 뒤집혔다 → [[ped-llm-minor-age-policy-20260808]]

## 다음

사이클 ② 신규 교수법 조사 (역방향 설계, 스캐폴딩·페이딩, 자기조절학습, 블록 스케줄링, 국내·해외 성취기준, 프리미엄 사교육) + 신규 3건: **11~13세 국내 사용 실태**(Lv1 시장 근거 공백), CASE 인지 가속 프로그램, 원문 확보. → [[edu-11-16-research-plan]]

기존 커리큘럼 자산(`wizard-curriculum`, `curriculum-v0.3`, `sk-biopharma-*`)은 **별개 라인, 참조만.**
