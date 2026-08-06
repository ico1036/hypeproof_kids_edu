---
type: source
title: "7 AI Native Assets — 측정 구조 검토 원본"
created: 2026-06-01
updated: 2026-06-01
tags:
  - source/original
  - framework/7-ai-native-assets
  - measurement/behavior-signals
  - domain/boa-dental
status: ingested
source_file: ".raw/articles/7assets-measurement-review-original-20260523.html"
related:
  - "[[seven-ai-native-assets-original]]"
  - "[[sk-biopharma-pilot]]"
  - "[[hypeproof-studio]]"
---

# 7 AI Native Assets — 측정 구조 검토 원본

사용자가 “이게 오리지널”이라고 지정한 HTML 원본. 문서 메타는 `boa-search-skill-creator · 2026-05-23 · 보아치과 AI 온보딩 검토`.

## 핵심 명제

- 7 AI Native Assets는 선언적 지식이 아니라 **절차적 역량**이다.
- Q&A는 자산을 **가르치는 데** 쓸 수 있지만, 자산을 **측정하는 데** 쓰면 타당도가 낮다.
- 측정은 실제 과정 신호에서 해야 한다.
- 특히 `Verification reflex`와 `Iteration reflex`는 질문으로는 원천적으로 측정이 어렵고 행동 관찰이 필요하다.

## 원본의 측정 원칙

| 레이어 | 역할 | 결론 |
|---|---|---|
| Layer A — Q&A | 교육 + 경계 선언 | 측정에 쓰지 말 것 |
| Layer B — 행동 신호 | 자산별 proxy 신호 자동 집계, LLM judge, 세션 간 변화 추적 | 채점 타당도 높음 |

## 7 Assets별 Q&A 측정 유효성

| Asset | Q&A 유효성 | 원본 판단 |
|---|---|---|
| Delegation judgment | 유효 | 경계선 선언 자체에 의미. 압박 상황에서는 행동 확인 필요 |
| Intent clarity | 부분적 | 유도된 답일 수 있음. 초기 프롬프트 구조가 더 직접 신호 |
| Context design | 부분적 | 방법을 아는 것과 실제 쓰는 것은 다름 |
| Taste | 낮음 | 좋은 결과를 말하는 것과 나쁜 결과를 거부하는 것은 다름 |
| Ownership | 낮음 | 실패 시 책임 언어/회고에서 드러남 |
| Verification reflex | 거의 불가 | 반사는 계획이 아니라 자동 행동. 행동 관찰 필요 |
| Iteration reflex | 거의 불가 | 실제 몇 번 돌아와 깎았는지만 측정값 |

## 행동 신호

- 첫 번째 프롬프트 길이/구조: Intent clarity, Context design
- 세션 간 프롬프트 변화: Context design, Iteration reflex
- 같은 목적 내 수정 횟수: Taste, Iteration reflex
- 출처 확인 후속 메시지: Verification reflex
- 세션 복귀 간격 + 지참 내용: Iteration reflex, Ownership
- 피드백 분포 추세: Taste, Ownership
- 자기 회고 언어 패턴: Ownership

## SK바이오팜 적용 메모

SK바이오팜 가족 AI 게임 랩에 적용할 때도 원칙은 동일하다. 게임을 만든다는 결과만으로 7 Assets를 측정했다고 보면 안 된다. 수업 중 `프롬프트 구조`, `수정 패턴`, `테스트/검증 행동`, `부모-자녀 역할 분담`, `회고 언어`, `다음 버전 계획`을 HypeProof Studio가 로그로 남기고, 그 행동 증거로 성장 리포트를 작성해야 한다.
