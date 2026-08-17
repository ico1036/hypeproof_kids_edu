---
type: meta
scope: edu-11-16
title: "Curriculum Log"
created: 2026-08-08
updated: 2026-08-08
tags:
  - meta/log
  - curriculum
---

# Curriculum Log

`curriculum_wiki/` 변경 이력. 최신 항목이 위. **추가 전용 — 과거 엔트리 수정 금지.**

---

## [2026-08-17] rules | scope 값 체계 + 파일명 접두사 정식화
- Pages: `curriculum-schema` (scope 값 체계·접두사 2종·lint 10~12 추가), `curriculum-index`
- 재판정: 28건 → `scope: common` / 작업 파일 라인 분리(`startup-hot`·`startup-log` 신설)
- Key insight: 라인이 하나일 때 붙인 `scope: edu-11-16`이 40건에 그대로 남아 **`edu-constitution`(헌법)조차 형식상 창업·IR 라인에 적용되지 않는 상태**였다. 게이트 문서가 라인 전용으로 잠겨 있으면 게이트가 아니다. 라인을 볼트로 쪼개는 방안도 검토했으나, 두 라인은 `common` 28건을 공유해 결합도가 높다 — 복사하면 두 진실이 생기고 참조하면 이름만 분리다. **라인은 축이지 트리가 아니다.** 경합한 것은 지식이 아니라 작업 상태였으므로 `hot`·`log`만 쪼갰다. `measurement-axes`·`placement-rules` 등 4건은 본문을 읽어야 판정되므로 규칙과 어긋난 상태로 명시해 남겼다.

## [2026-08-08] split | curriculum_wiki 분리 신설
- 이전 위치: `curriculum_wiki/**` (33), `curriculum_wiki/research/ped-*` (10), `wiki/decisions/edu-11-16-*` (4), `_templates/` (4)
- 신설: `curriculum-index`, `curriculum-log`, `curriculum-hot`, 폴더 8종
- 삭제: 오버라이드 3건 + `override-protocol` + `_templates/override`
- Key insight: 위키를 사업 볼트와 지식 볼트로 나눴다. 오버라이드 프로토콜은 "기존 조직 문서와의 관계"를 기록하는 장치였는데, 그 결론(무순위·합성점수 금지·5축)이 이미 헌법과 측정 문서에 흡수되어 있어 삭제해도 지식을 잃지 않는다. 남은 것은 조직 표준 4축 확장 제안 하나이며 사업 볼트 과제로 넘겼다.

## [2026-08-08] asset | 방법론 라이브러리 + 국내 모형 지도
- Pages: `methods/` 15건 (카드 8 + 국내 지도 5 + 선택 가이드 + 근거 기준)
- Key insight: 발견학습 논쟁의 결론은 "발견이냐 설명이냐"가 아니라 "안내가 있느냐"다. 비유도 발견은 명시적 수업보다 나쁘고(d=-0.38) 유도된 발견은 낫다(d=+0.50). 국내 "문제 해결 학습 모형"은 서구 PBL이 아니라 안내된 발견에 가깝다. Builder 트랙은 Problem-Based가 아니라 Project-Based다.

## [2026-08-08] research | L0 사이클 ①·②
- Pages: `research/` 10건
- Key insight: 검증 대상 5건 중 2건 기각, 1건 조건부, 1건이 설계 전제를 뒤집었다. 사이클 ②에서 Lv1 시장 근거를 확보하고 금지 개입 정식화 오류를 발견했다.

## [2026-08-08] scaffold | 자산 레이어 최초 구축
- Pages: 헌법, 금지 개입, 측정 축, 배치 제약, 지도안 규격·작성법·검증, 스키마, 결정 4건
- Key insight: 강의 한 벌을 통짜로 쓰면 재조합이 안 된다. 활동 원자로 쓰고 "강의 한 벌"은 컴파일 인스턴스로 취급한다. 목표는 강의가 아니라 강사가 자기 상황에 맞게 조립할 수 있는 상태다.
