---
type: spec
status: active
scope: edu-11-16
ip_owner: unverified
title: "오버라이드 프로토콜"
owner: JY
created: 2026-08-08
updated: 2026-08-08
tags:
  - curriculum
  - override
  - meta
  - edu-11-16
---

# 오버라이드 프로토콜

기존 위키 문서에 잘못된 부분이 있거나 이 라인에서 다르게 적용해야 할 때, **원본 본문은 수정하지 않고** 관계만 별도 노트로 선언한다.

## 왜 원본을 안 건드리나

원본은 다른 라인(성인·경기·기업 교육)에서 여전히 사용 중이고, 다른 사람이 작성했으며, 우리가 틀렸을 수도 있다. 원본을 직접 고치면 **왜 달라졌는지가 사라지고**, 다른 라인이 조용히 망가진다.

## 3분류 — 이걸 안 나누면 조직 문서가 죽는다

| kind | 뜻 | 원본은 | 종착지 |
|---|---|---|---|
| `correction` | 원본이 **틀렸다** (사실 오류, 출처 없는 주장, 누락) | 조직 전체에서 틀림 | **upstream 후보.** 원저자에게 올려 원본을 고쳐야 한다 |
| `scoped-variant` | 원본은 맞다. **이 맥락에서만 다르다** | 다른 라인에선 유효 | **영구 분기.** upstream 하지 않는다 |
| `quarantine` | 근거 미확인. **판정 보류, 사용 정지** | 판단 유보 | 조사 결과로 채택 또는 폐기 |

`correction`을 계속 `scoped-variant`로 처리하면 조직 안에 진실이 두 개 자란다.
`scoped-variant`를 upstream 하면 다른 라인이 망가진다.

## 해소 규칙

1. `scope`가 걸린 컨텍스트에서는 **override가 원본에 항상 우선**한다.
2. 한 원본·한 섹션에 `status: active` override는 **최대 1개**. 둘 이상이면 lint 에러.
3. 자산이 override 대상 원본을 **직접 인용하면 lint 에러**. 반드시 override를 경유해 인용한다.
4. `upstream_reviewed` 이후 원본이 수정되면 lint가 **재검토 플래그**를 띄운다. 원본이 이미 고쳐졌으면 override를 `retired` 처리한다.
5. `pending-upstream`이 **90일 초과**면 경고. 영구 방치가 진실 분기의 실제 원인이다.

## 원본 쪽 표시

원본 **본문은 손대지 않되**, 프론트매터에 색인 표시 한 줄만 추가한다.

```yaml
has_overrides: true
```

내용 수정이 아니라 발견 가능성을 위한 메타데이터다. 이것이 없으면 원본만 열어본 사람은 override의 존재를 모른다. lint가 자동 관리한다.

## ADR과의 관계

**override 노트가 근거를 담으므로 별도 ADR을 만들지 않는다.** 같은 이야기를 두 벌 관리하지 않기 위함이다.

`wiki/decisions/`의 ADR은 **기존 문서와 무관한 신규 결정**에만 쓴다.

## ingest-ruling과의 구분

| | override | ingest-ruling |
|---|---|---|
| 대상 | `wiki/` 기존 문서 | `.raw/` 원자재 |
| 성격 | 동등한 위상의 문서와의 관계 | 원자재를 자산으로 가공할 때의 판정 |
| 원본 위치 | 위키에 남음 | `.raw`에 불변으로 남음 |

섞으면 `.raw` 전체가 override 대상이 되어 폴더가 터진다.

## 현재 활성 override

| 노트 | 원본 | kind | status |
|---|---|---|---|
| [[ovr-license-ranking-family-line]] | [[hypeproof-brand-license-structure-v0.1]] | scoped-variant | active |
| [[ovr-measurement-fifth-axis]] | [[hypeproof-measurement-rubric-from-hyrox-20260515]] | correction | pending-upstream |
| [[ovr-measurement-composite-score]] | [[hypeproof-measurement-rubric-from-hyrox-20260515]] | scoped-variant | active |

## 관련

- [[curriculum-schema]]
- [[edu-constitution]]
