---
type: override
status: active
kind: scoped-variant
scope: edu-11-16
ip_owner: hypeproof
supersedes: "[[hypeproof-measurement-rubric-from-hyrox-20260515]]"
upstream_reviewed: 2026-08-08
grounds: "교육 라인 헌법 A-1 / A-4 / B-2"
created: 2026-08-08
updated: 2026-08-08
tags:
  - curriculum
  - override
  - measurement
  - edu-11-16
---

# 오버라이드 — 가족 라인에 합성 단일 점수를 만들지 않는다

## 1. 원본이 말하는 것

[[hypeproof-measurement-rubric-from-hyrox-20260515]]은 "HypeProof 측정값은 단일 시간이 아니라 4개 축의 **합성 점수**"라고 정의한다. HYROX가 시간을 재듯 표준화된 하나의 값을 내는 구조다.

## 2. 이 라인에서 적용하는 것

**축별 프로파일만 제시하고, 합성 단일 점수·종합 등급을 산출하지 않는다.**

- 축별 관찰 기록은 남긴다
- 축을 가로질러 합산·가중평균하지 않는다
- 종합 등급·레벨·티어를 부여하지 않는다

## 3. 왜

세 조항이 동시에 걸린다.

- **헌법 B-2** — 합성 점수는 서열을 만들고, 서열은 비교를 만든다
- **헌법 A-4** — 비교는 "뒤처진다"를 생산한다. 부모의 불안을 팔지 않는다
- **헌법 A-1** — 아동에게 부여된 **단일 숫자는 진단으로 읽힌다.** "우리 애가 68점"은 부모에게 성취도가 아니라 판정으로 수신된다. 진단·해석은 외부 전문가의 일이라는 구조가 실질적으로 무너진다

세 번째가 가장 무겁다. 이것은 톤의 문제가 아니라 **무자격 평가의 외양**을 만드는 문제다.

## 4. 원본이 여전히 옳은 범위 ★

**경기·성인 라인에서는 합성 점수가 필수다.**

- Competition / Challenge — 단일 값이 없으면 순위가 성립하지 않는다
- Creator License 시즌권 — 기록 인정의 단위가 필요하다
- 기업 교육 — 성인 대상이며 조직 내 성과 지표와 연동될 수 있다

따라서 **upstream 하지 않는다.**

## kind 판정 근거

`scoped-variant` — 원본이 틀린 것이 아니다. 미성년·가족 맥락에서만 단일 점수가 금지된다. 대상이 바뀌면 원본이 옳다.

## 파생 제약

Sediment 스키마 설계 시:

- 축별 필드는 두되 **총점 필드를 만들지 않는다**
- UI에서 축들을 하나의 게이지·레이더 총합으로 시각화하지 않는다
- 필드명에 `score`, `grade`, `level` 대신 관찰 어휘를 쓴다 (헌법 B-5)

## 관련

- [[measurement-axes]]
- [[ovr-measurement-fifth-axis]]
- [[edu-constitution]]
