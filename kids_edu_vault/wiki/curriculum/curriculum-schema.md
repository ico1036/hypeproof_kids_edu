---
type: spec
status: draft
ip_owner: unverified
title: "커리큘럼 자산 프론트매터 스키마"
owner: JY
created: 2026-08-08
updated: 2026-08-08
tags:
  - curriculum
  - schema
  - edu-11-16
---

# 커리큘럼 자산 프론트매터 스키마

컴파일러(L4)의 입력은 산문이 아니라 **프론트매터**다. 아래 필드가 없으면 그 자산은 조합 불가능하며, 강사는 그것을 재사용할 수 없다.

## 공통 필수 필드

모든 `wiki/curriculum/` 노트에 적용.

```yaml
type: activity | model | principle | rubric | guardrail | constraint | asset | track | lesson-plan | override | ingest-ruling
status: draft | active | quarantine | retired
scope: edu-11-16          # 유효 범위
ip_owner: unverified | hypeproof | partner-<name> | joint | derived-external
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [curriculum, ...]
```

## `ip_owner` — 값 체계

`ip_owner`는 **누락 금지**. 파트너 IP가 섞인 자산은 제3자 라이선스 패키지에서 기계적으로 제외되어야 한다. → [[edu-11-16-parent-track-ip-boundary]]

| 값 | 뜻 | 라이선스 패키지 |
|---|---|---|
| **`unverified`** | **기본값. 귀속 판정 전** | ⛔ **자동 제외** |
| `hypeproof` | 판정 완료. 법인 단독 소유 | ✅ 포함 |
| `partner-<name>` | 파트너 소유 | ⛔ 제외 (인바운드 계약 범위 내에서만 사용) |
| `joint` | 공동 소유 | ⚠️ 개별 합의 필요 |
| `derived-external` | 외부 저작물 기반 2차적저작물 | ⚠️ 재배포 검토 필요 |

### 왜 `unverified`가 기본값인가

2026-08-08 기준 **48건 전부 `unverified`다.** 이는 미완이 아니라 정직한 상태다.

초기에는 파일을 만들 때마다 습관적으로 `hypeproof`를 넣었으나, **각 파일에 대해 "정말 법인 단독 소유인가"를 판정한 적이 없었다.** 전부 같은 값으로 채워진 필드는 "판정이 끝났다"는 잘못된 인상을 주고, 라이선스 패키지 빌드 시 그것을 믿으면 위험하다.

실제로 판정이 필요한 사례:

| 대상 | 쟁점 |
|---|---|
| `wiki/intel/ped-*` 10건 | 외부 저작물의 요약·번역. 인용 범위를 넘는 요약이 재배포되면 문제. **`derived-external` 후보** |
| `models/kr-models-*` 4건 | 국내 교육과정 모형 정리. 같은 성격 |
| `models/m-00*` 8건 | Gold Standard PBL 7요소(PBLWorks), 스캐폴딩 3요소 등은 **원저자의 프레임**이다 |
| `.raw` 유래 자산 | 원본은 Jay의 아이데이션 산출물. **개인 vs 법인 귀속이 정리된 적 없다** |

마지막 항목이 특히 그렇다. 회사–창업자 간 IP 귀속 문제이며 **법률 검토 영역**이다. 임의로 `hypeproof`를 적는 것은 추정이다.

### 판정 규칙

- **판정 없이 `hypeproof`로 올리지 않는다.** 판정 근거를 노트 본문 또는 `edu-11-16-parent-track-ip-boundary`에 남긴다
- `partner-<name>`의 `<name>`은 **파트너사가 확정된 뒤** 채운다. 현재 미확정
- `derived-external`은 원저작물 출처를 함께 기록한다
- **`unverified`가 남아 있는 자산은 라이선스 패키지 빌드에서 자동 제외**된다. 이것이 이 값의 안전 기능이다

## activity — 활동 원자

조합의 최소 단위. 30~60분. "차시"보다 작고 "단계"보다 크다.

```yaml
type: activity
id: act-<3자리>                  # 불변. 파일명이 바뀌어도 이 값으로 참조
model: M?                        # 소속 수업모형
principle: []                    # 원리 번호
level: [lv1, lv2]                # 적용 발달구간. 변형은 본문에
duration_min: 45
requires: [act-003, asset-...]   # 선행 자산·활동
forbids: []                      # 동시·인접 배치 금지
evidence: ""                     # 이 활동이 남기는 증거물 1개
axes: [input, load]              # 측정 5축 중 훈련 대상
prohibited_moves: []             # 금지 개입. 강사 매뉴얼로 자동 추출
prep_assets: []                  # 사전 준비 자산
safety: none | attention | protocol   # protocol이면 별도 대응 절차 필수
method: [m-002]                  # 채택 방법론 → wiki/curriculum/models/
guidance:                        # m-002 요건. 발견형 활동에 필수
  space: ""                      # 탐색 공간을 어떻게 좁히는가
  elicit: ""                     # 설명 유도 발문
  feedback: ""                   # 즉각 피드백 통로
individual_evidence: ""          # 소집단 활동의 개별 산출물 (m-005 요건)
retry: true                      # 재시도 기회 유무 (m-006 요건)
```

### 방법론 파생 필수 필드 (2026-08-08 추가)

방법론 라이브러리 조사에서 도출된 요건. → [[models/_index|방법론 라이브러리]]

- **`guidance`** — 발견형 활동(`method`에 m-002 포함)은 3개 하위 필드를 모두 채운다. **하나라도 비면 그 활동은 "안내된 발견"이 아니라 방치**이며, 명시적 수업보다 나쁜 결과를 낸다 (Alfieri et al. 2011: 비유도 발견 d=−0.38)
- **`individual_evidence`** — 소집단 활동은 개별 산출물이 있어야 한다. 없으면 증거가 개인에게 귀속되지 않아 Evidence(Sediment)가 성립하지 않는다
- **`retry`** — 피드백이 발생하는 활동에서 `false`면 그 피드백은 형성평가가 아니다

### 필드 주석

- **`evidence`** — 증거물이 없는 활동은 만들지 않는다. Evidence(Sediment)에 적재될 것이 없으면 그 시간은 상품 가치를 만들지 않는다.
- **`prohibited_moves`** — 이 라인 품질의 핵심 장치. "무엇을 하는가"보다 **"무엇을 하지 않는가"**가 결과를 결정한다. → [[prohibited-moves]]
- **`requires` / `forbids`** — 컴파일러가 배치 유효성을 검증하는 근거. 산문에 숨어 있으면 검증이 안 되고, 라이선스 강사는 산문을 읽지 않는다.
- **`duration_min`** — 회차 총시간에 의존하지 않게 30/45/60 단위로만 쓴다. 회차 포맷이 바뀌어도 자산을 안 건드리기 위함. → [[edu-11-16-session-format]]
- **`safety: protocol`** — 정서적 어려움이 드러날 수 있는 활동. 개별 대응 절차 문서 링크 필수.

## lesson-plan — 지도안

활동 원자를 1차시 분량으로 조립한 결과. 컴파일러의 출력이자 강사의 실행 문서.

```yaml
type: lesson-plan
track: <track-id>
session: <회차>-<차시>
activities: [act-001, act-004]   # 구성 활동
model: [M1]
level: lv1 | lv2
duration_min: 110
evidence: []                     # 이 차시가 남기는 증거물
completion_link: []              # 연결된 수료 요건
```

규격과 작성 순서는 [[lesson-plan-authoring-guide]].

## override — 기존 문서와의 관계 선언

원본은 수정하지 않는다. 관계만 별도 노트로 선언한다.

```yaml
type: override
kind: correction | scoped-variant | quarantine
status: active | retired | upstreamed | pending-upstream
supersedes: "[[원본페이지]]#섹션앵커"
also_affects: ""                 # 같은 주장을 담은 다른 원본 (선택)
upstream_reviewed: YYYY-MM-DD    # 이 날짜의 원본을 보고 판단했다
grounds: ""                      # 근거 (헌법 조항, 조사 문서 등)
```

`supersedes` / `also_affects` 에 등재된 원본에는 lint가 `has_overrides: true` 를 자동 부착한다. **원본 본문은 수정하지 않는다.**

`kind` 분류와 해소 규칙은 [[override-protocol]].

## ingest-ruling — 승격 판정

`.raw/` 원자재를 자산으로 승격할 때 무엇을 왜 바꿨는지 기록. 원본은 `.raw`에 불변으로 남는다.

```yaml
type: ingest-ruling
source: ".raw/<파일명>"
ruling: adopt | transform | reject | defer
grounds: ""
produced: []                     # 이 판정으로 생성된 자산
```

## Lint 규칙

`/wiki-lint` 실행 시 아래를 검사한다.

1. `wiki/curriculum/**` 에 `ip_owner` 누락 → 에러 (프론트매터 기준. 본문 코드블록은 무시)
2. `evidence`가 빈 `activity` → 경고
3. 한 원본·한 섹션에 `status: active` override 2개 이상 → 에러
4. 자산이 override 대상 원본을 직접 인용 → 에러 (override 경유 필수)
5. `status: pending-upstream` 이 90일 초과 → 경고
6. `safety: protocol` 인데 대응 절차 링크 없음 → 에러
7. `method`에 m-002 포함인데 `guidance` 하위 필드 미완 → 에러
8. 소집단 활동인데 `individual_evidence` 비어 있음 → 에러
9. 피드백 활동인데 `retry: false` → 경고
10. `ip_owner`가 정의된 5개 값 외 → 에러
11. **`ip_owner: unverified` → 라이선스 패키지 빌드에서 자동 제외** (경고, 빌드 시 에러)

## 관련

- [[override-protocol]]
- [[edu-constitution]]
- [[lesson-plan-authoring-guide]]
