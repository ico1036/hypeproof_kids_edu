---
type: intel
status: summarized
scope: edu-11-16
ip_owner: hypeproof
title: "LLM 서비스 미성년자 연령 정책 (2026-08-08 확인)"
source_date: 2026-08-08
created: 2026-08-08
updated: 2026-08-08
tags:
  - intel
  - research
  - compliance
  - edu-11-16
---

# LLM 서비스 미성년자 연령 정책

L0 사이클 ① 검증 대상 5번. **정책은 자주 바뀐다. 이 문서의 확인 날짜는 2026-08-08이며, 파일럿 D-day 전 재확인 필수.**

## 요점 (TL;DR)

| 서비스 | 최소 연령 | 13세 미만 경로 | Lv1(11~13) 사용 가능? |
|---|---|---|---|
| **Claude** | **만 18세** | 없음 | ❌ 불가. 강사 준비용만 |
| **ChatGPT** | 만 13세 + 18세 미만은 보호자 동의 | 없음 | △ 13세만 가능 |
| **Gemini** | 만 13세 (개인 계정) | ✅ **Family Link 감독 계정** | ✅ **가능** |

## 1. Claude — 18세 이상, 미성년 경로 없음

소비자 약관 §2:

> "You must be at least 18 years old or the minimum age required to consent to use the Services in your location, whichever is higher."

보호자 동의를 통한 미성년자 이용 경로가 **약관에 명시되어 있지 않다.**

### K-12 약관은 우리에게 적용되지 않는다

Anthropic은 별도의 [US K-12 약관](https://www.anthropic.com/legal/k12-terms)을 운영한다. 다만:

- 계약 주체가 **교육기관**(학교·학군 등)이며 개인이 아니다
- **미국 전역 대상**이고 캘리포니아주 법이 준거법이며 FERPA 준수를 전제한다
- 민간 사교육기관의 포함 여부가 명확하지 않다

→ **국내 가족 대상 상품에는 적용 불가.** Claude는 아동 실습 도구에서 제외하고 강사 준비용으로만 쓴다는 기존 판단이 유지된다.

## 2. ChatGPT — 13세 이상, 18세 미만은 보호자 동의

> "You must be at least 13 years old or the minimum age required in your country to consent to use the Services."
> "If you are under 18 you must have your parent or legal guardian's permission to use the Services."

부가 사항:
- **부모 관리 기능(parental controls)** 제공 — 계정 연결 시 일부 설정 관리, quiet hours 지정, 제한적 안전 알림 수신. **단, 보호자가 대화 내용을 읽거나 모니터링할 수는 없다**
- 2026년 **연령 예측 시스템**이 도입되어, 성인이라고 신고한 계정에도 청소년 제한이 적용될 수 있다

### 우리에게 주는 시사점

- Lv1(11~13세) 중 **11·12세는 ChatGPT 사용 불가.** 13세만 가능하며, 같은 반 안에서 연령이 갈린다
- "보호자가 로그를 본다"는 전제의 운영 설계는 **성립하지 않는다.** 부모 관리 기능은 대화 열람을 제공하지 않는다. 로그 공유가 필요하면 별도 수단이 있어야 한다
- 연령 예측 시스템 탓에 강사 계정도 예기치 않게 청소년 모드로 전환될 수 있다 — 리허설 시 확인 항목

## 3. Gemini — Family Link 감독 계정으로 13세 미만도 가능 ★

Google 공식 지원 문서 기준:

- 개인·학교 Google 계정으로 Gemini를 쓰려면 **만 13세 이상**(국가별 해당 연령), 직장 계정은 18세 이상
- **13세 미만도 보호자가 Family Link로 활성화하면 감독 계정으로 Gemini Apps 로그인 가능**
- 보호자가 Family Link 앱으로 접근 권한을 켜고 끌 수 있으며, 자녀가 처음 활성화하면 보호자에게 이메일 알림
- 13세 미만 계정 제한: **Keep Activity 설정 불가**, "Hey Google"·Voice Match 사용 불가
- **EEA·스위스·영국에서는 감독 계정으로 Gemini Apps 이용 불가** (한국은 해당 없음)

## ⛔ 설계 변경 — Lv1 "아동 계정 없음" 가정이 틀렸다

`.raw` 문서는 Lv1(11~13세)에 **"아동 계정 없음. 강사 계정 스크린 공유 + 부모 계정 가정 실습"**을 전제로 활동을 설계했다. 이 전제는 **Gemini + Family Link 경로를 놓친 것**이다.

바뀌는 것:

1. **Lv1도 자기 계정으로 직접 실습할 수 있다** (Gemini, 보호자가 Family Link로 활성화). 강사 계정 스크린 공유에 묶일 이유가 없다
2. 보호자 동의가 **약관 준수를 넘어 운영 절차에 내장**된다 — 보호자가 직접 켜야 하고 알림을 받는다. 헌법 B-4(동의 선행)와 자연스럽게 맞물린다
3. **"아이가 손으로 옮겨 적어 전달"** 같은 우회 설계가 불필요해질 수 있다. 다만 필사가 정독을 강제하는 교육적 효과는 별개이므로, 약관 회피용이 아니라 **의도된 교육 장치**로 유지할지 재판단한다
4. 다중 모델 활동에서 **Gemini를 Lv1의 기본 모델로 고정**하는 것이 가장 단순한 준수 경로다

→ 활동 원자 설계 시 반영. [[placement-rules]] C-2 갱신 대상.

## 운영 체크리스트

- [ ] 트랙별 사용 모델을 연령 요건에 맞춰 고정 (Lv1 = Gemini, Lv2 = Gemini/ChatGPT)
- [ ] Lv1 등록 절차에 **Family Link 활성화 안내** 포함
- [ ] 보호자 동의서에 사용 모델·계정 구조 명시
- [ ] 로그 공유가 필요하면 별도 수단 확보 (ChatGPT 부모 관리 기능은 대화 열람 미제공)
- [ ] Claude는 강사 준비용으로만. 아동 노출 금지
- [ ] **파일럿 D-day 전 전 항목 재확인** — 정책 변경 빈도가 높다

## 출처

- [Anthropic Consumer Terms of Service](https://www.anthropic.com/legal/consumer-terms)
- [Anthropic Terms of Service: US K-12](https://www.anthropic.com/legal/k12-terms)
- [OpenAI Terms of Use](https://openai.com/policies/row-terms-of-use/)
- [Parental controls in ChatGPT (OpenAI Help Center)](https://help.openai.com/en/articles/12315553-parental-controls-in-chatgpt)
- [Manage your child's access to Gemini Apps (Google For Families Help)](https://support.google.com/families/answer/16109150?hl=en)
- [What you need to sign in to Gemini Apps (Gemini Apps Help)](https://support.google.com/gemini/answer/13278668?hl=en)

## 관련

- [[edu-constitution]] — B-6
- [[placement-rules]]
- [[edu-11-16-research-plan]]
