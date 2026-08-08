---
type: index
status: navigational
ip_owner: hypeproof
title: "커리큘럼 자산 레이어 — 11~16세 AI 교육"
created: 2026-08-08
updated: 2026-08-08
tags:
  - curriculum
  - edu-11-16
---

# 커리큘럼 자산 레이어

11~16세 대상 AI 교육의 **재사용 가능한 자산 풀**. 특정 상품의 커리큘럼이 아니라, 여러 상품·채널의 커리큘럼을 컴파일해 내기 위한 원재료다.

## 왜 이 레이어가 따로 있나

강의 한 벌을 통짜 문서로 쓰면 재조합이 안 된다. 대상·시간·수준이 바뀔 때마다 처음부터 다시 써야 한다. 그래서 **처음부터 원자 단위로 쓰고, "강의 한 벌"은 그 원자들을 컴파일한 인스턴스**로 취급한다.

목표는 강의 한 벌이 아니라 **강사가 자기 상황에 맞는 강의를 조립할 수 있는 상태**다. → [[edu-11-16-track-architecture]]

## 5 레이어

| 레이어 | 위치 | 내용 |
|---|---|---|
| L0 원전 | `wiki/intel/` | 교수학습법·발달심리 원 조사 |
| L1 설계원리 | `wiki/concepts/` | L0를 우리 설계 규칙으로 번역 |
| **L2 자산** | **`wiki/curriculum/`** | **이 폴더. 원자 블록·모형·루브릭·가드레일** |
| L3 인스턴스 | `wiki/curriculum/tracks/` | 컴파일된 실제 트랙 |
| L4 컴파일러 | `.claude/skills/` | 자산 → 트랙 생성 스킬 (미구현) |

L1 문서는 **근거(L0 링크) → 설계 규칙 → 구현한 자산(L2 링크)** 3단을 반드시 채운다. 안 채워지면 그 조사는 우리 것이 아니다.

## 하위 폴더

| 폴더 | 내용 | 안정성 |
|---|---|---|
| `principles/` | 원리별 이식 판정 (발달구간·부모·강사 4열) | 높음 |
| `models/` | **교수학습 방법론 라이브러리 + 선택 가이드.** 8절 표준 포맷 | 높음 |
| `activities/` | 활동 원자. 30~60분 단위 | 상시 증가 |
| `constraints/` | 배치 규칙. 컴파일러 검증 대상 | 중간 |
| `rubrics/` | 측정 축·수준·수료 요건 | 낮음(신중) |
| `guardrails/` | 헌법·금지 개입·법·안전 | 최고 (변경 시 승인 필요) |
| `assets/` | 사전 생성 데이터셋·카드덱·워크북 양식 | 상시 |
| `tracks/` | 컴파일된 인스턴스 | 기수마다 |
| `lesson-plans/` | 지도안 규격·작성법·검증 체크리스트 | 중간 |
| `overrides/` | 기존 위키 문서와의 관계 선언 | 상시 |
| `_ingest-rulings/` | `.raw` → 자산 승격 시 판정 기록 | 상시 |

## 핵심 문서

- [[curriculum-schema]] — 모든 자산의 프론트매터 스키마
- [[edu-constitution]] — 이 라인에서 절대 하지 않는 것
- [[measurement-axes]] — 5축 측정 체계
- [[lesson-plan-authoring-guide]] — 지도안 작성법
- [[placement-rules]] — 배치 제약
- [[evidence-standards]] — 근거를 다루는 원칙
- 방법론 라이브러리 — `models/_index.md` (선택 가이드)

## 현재 상태

스캐폴드 완료(2026-08-08). 자산은 아직 비어 있다. L0 조사 → 원리·모형 확정 → 활동 원자 작성 순서로 채운다.

**조사 순서**: ① 기존 주장 출처 검증 → ② 신규 교수법 조사. → [[edu-11-16-research-plan]]

## 관련

- [[edu-11-16-track-architecture]]
- [[edu-11-16-parent-track-ip-boundary]]
- [[edu-11-16-evidence-capture]]
- [[edu-11-16-session-format]]
