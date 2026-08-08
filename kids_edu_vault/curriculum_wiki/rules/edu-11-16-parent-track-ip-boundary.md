---
type: decision
status: accepted
scope: edu-11-16
ip_owner: unverified
title: "11~16세 교육 — 부모 트랙 IP 경계"
decided: 2026-08-08
owner: JY
created: 2026-08-08
updated: 2026-08-08
tags:
  - decision
  - curriculum
  - ip
  - edu-11-16
---

# 결정 — 부모 트랙은 파트너 IP, 우리는 접합면만

## 맥락

Jay 개요는 Parent Protocol을 **대화교육 파트너** 담당으로 두고 "모듈 IP는 파트너 소유"를 명시한다. 동시에 부모 트랙은 아동 트랙과 촘촘히 맞물려야 한다 — 부모가 서명하는 합의서, 부모에게 발송되는 물증, 가족 합동 세션 등이 아동 측 증거 산출의 일부이기 때문이다.

또한 조직은 이후 강사 라이선스 판매를 계획하고 있다(HYROX 기반 Facilitator License 층).

## 결정

**경계선: 부모의 행동을 바꾸는 내용 = 파트너 / 부모가 아동의 증거에 참여하는 절차 = 우리.**

| 우리(HypeProof) | 파트너 |
|---|---|
| 부모가 서명하는 합의서·동의서 양식 | 부모 대화법 교육 내용 |
| 부모에게 발송되는 물증의 형식·시점 | 성과 압박·비교 다루기 모듈 |
| 가족 합동 세션의 **운영 규칙**(발언권·타이머·역할) | 부모 윤리 모듈 |
| 아동 트랙이 부모에게 넘기는 것의 정의 | 부모 세션의 스크립트·워크북 본문 |

**구현**: 모든 자산 프론트매터에 `ip_owner: hypeproof | partner-<name> | joint` 필수. 파트너 소유 노트는 **접합면(입력·출력·타이밍·전제조건)만** 기록하고 내부 내용은 링크로만 참조한다.

## 근거

파트너 IP가 우리 자산에 섞이면:

1. **재판매 구멍** — Facilitator License 패키지에서 그 모듈만 제외되어 상품이 쪼개진다
2. **교체 비용** — 파트너 변경 시 뒤엉킨 부분을 뜯어내야 한다. 지금 분리는 몇 분, 나중 분리는 며칠
3. **계약 위반 소지** — git 히스토리는 삭제해도 남는다. NDA 조항이 있으면 그 자체로 문제

동시에 인터페이스만으로는 통합 설계가 안 나온다. 그래서 폴더 분리가 아니라 **필드 분리**를 택했다. 나중에 `ip_owner`로 기계적 분리가 가능하다.

## 귀결

- **Parent AI Dialogue(1인 100만)는 우리가 파는 파트너 IP다.** 인바운드 라이선스 계약이 선행해야 한다
- 이 모듈은 **아웃바운드 라이선스 패키지에서 제외**된다
- lint 규칙: `curriculum_wiki/**`에 `ip_owner` 누락 시 에러. 값 체계는 5단(`unverified` 기본값) → [[curriculum-schema]]
- 지도안 "가정 연계" 항목은 작성 시 IP 경계 확인 대상 → [[lesson-plan-quality-checklist]]

## 미결

### ⛔ IP 귀속 판정 48건 미완 (2026-08-08)

`curriculum_wiki/**` 33건 + `curriculum_wiki/research/ped-*` 10건 + `_templates` 5건이 **전부 `ip_owner: unverified`** 상태다. 초기에 습관적으로 `hypeproof`를 넣었으나 판정 근거가 없어 전량 되돌렸다. → [[curriculum-schema]]

판정이 필요한 쟁점:

| 대상 | 쟁점 | 예상 값 |
|---|---|---|
| `intel/ped-*` 10건 | 외부 저작물의 요약·번역 | `derived-external` |
| `models/kr-models-*` 4건 | 국내 교육과정 모형 정리 | `derived-external` |
| `models/m-00*` 8건 | Gold Standard PBL 7요소, 스캐폴딩 3요소 등 원저자 프레임 포함 | `derived-external` 또는 부분 `hypeproof` |
| `.raw` 유래 자산 | 원본이 Jay의 아이데이션 산출물. **개인 vs 법인 귀속 미정리** | 법률 검토 필요 |
| 우리 순수 창작 (헌법·금지개입·스키마·배치제약) | | `hypeproof` |

**이 판정은 저작권 판단이 섞여 있어 법률 검토가 선행되어야 한다.** 특히 `.raw` 유래 자산의 개인–법인 귀속은 회사 설립·지분 구조와 함께 정리될 사안이다.

그동안 `unverified`가 안전장치로 작동한다 — 라이선스 패키지 빌드에서 자동 제외되므로, 판정 없이 외부로 나가지 않는다.

### 그 외

- `partner-<name>`의 실제 값 미정 — **파트너사가 누구인지 확정되지 않았다**
- 외부 전문가의 Diagnostic 결과가 강사에게 **어떤 형태로** 전달되는가. 원본 해석을 그대로 넘기면 진단 라벨 문제가 재발한다 → [[ruling-profile-based-differentiation]]
- 파트너 계약의 실제 조항 확인 (본 결정은 개요 기재 사항에 근거한 설계 판단이며 계약서 검토가 아니다)
- `joint` 로 분류될 자산이 실제로 있는지 — 있다면 지분·사용권 별도 합의 필요

## 관련

- [[curriculum-schema]]
- [[edu-11-16-track-architecture]]
