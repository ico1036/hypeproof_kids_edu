---
type: project
title: "HypeProof Measurement Rubric from HYROX v0.1"
status: developing
created: 2026-05-15
updated: 2026-05-15
has_overrides: true
tags:
  - project
  - rubric
  - measurement
  - hyrox
---

# HypeProof Measurement Rubric from HYROX v0.1

작성: 2026-05-15

## 0. 핵심

HYROX가 시간을 재듯, HypeProof는 **AI 협업 과정의 품질**을 잰다.

HypeProof 측정값은 단일 시간이 아니라 다음 4개 축의 합성 점수다.

1. 입력 품질
2. 부하/반복 품질
3. 검증/조율 품질
4. 언러닝/전이 품질

이 4축은 HypeProof 4주 커리큘럼과 대응된다.

- Week 1 Foundation — 입력이 결과를 결정한다
- Week 2 Load — 만족하지 않는다
- Week 3 Mastery — 모델 너머를 본다
- Week 4 Transcendence — 초심으로 돌아간다

---

## 1. HypeProof 표준 경기 구조

HYROX가 `1km run + station`을 8번 반복하듯, HypeProof는 다음 4개 스테이션을 고정한다.

### Station 1. 입력 만들기 / Foundation

측정 대상:
- 문제 정의
- 맥락 제공
- 목표 명확성
- 제약조건 명시
- 예시/자료 제공

대응 원칙:
- 전심전력
- 잇기가설
- 질문공터
- 입력굴리기

### Station 2. 밀어붙이기 / Load

측정 대상:
- 첫 답변에 만족하지 않고 개선 요구
- 역할/관점 부여
- 반례/실패 조건 탐색
- 더 높은 기준 제시

대응 원칙:
- 부하걸기
- 만족유예
- 역할몰입
- 역목표

### Station 3. 비교/검증하기 / Mastery

측정 대상:
- 여러 후보 생성
- 후보 비교
- 외부 기준/데이터/사용자 관점으로 검증
- AI에게 위임한 것과 사람이 판단한 것의 구분

대응 원칙:
- 백번뽑기
- 다중모델
- 추상사다리
- 수행위임역전

### Station 4. 재구성/전이하기 / Transcendence

측정 대상:
- 배운 전략을 의심하고 수정
- 다른 맥락으로 적용
- 과몰입에서 빠져나와 결과물의 의미 설명
- 다음 반복 계획 수립

대응 원칙:
- 언러닝
- 상상
- 소격
- 천번째감탄

---

## 2. 공통 점수 구조

각 스테이션 25점, 총 100점.

- Station 1 Foundation: 25점
- Station 2 Load: 25점
- Station 3 Mastery: 25점
- Station 4 Transcendence: 25점

감점/페널티:
- 프롬프트 대리 작성: 실격 또는 비공식 기록
- 결과물만 제출하고 과정 로그 없음: 큰 감점
- AI 출력 그대로 복붙: 감점
- 기준 위반 콘텐츠: 실격
- 주어진 시간/제약조건 초과: 감점
- 타인 결과물 표절: 실격

---

## 3. Level 측정

### Level 1 — Verified AI Practitioner

측정 목표:
- AI와 기본적으로 협업할 수 있는가

표준 과제:
- 주어진 주제로 AI와 함께 결과물 1개 완성
- 4개 스테이션 전부 수행
- 과정 로그 제출

통과 기준:
- 총점 60점 이상
- 각 스테이션 최소 10점 이상
- 결과물 완성
- 과정 설명 가능

핵심 평가:
- 입력을 제대로 넣었는가
- AI 결과를 보고 한 번 이상 개선했는가
- 결과물의 장단점을 말할 수 있는가

### Level 2 — Verified AI Professional

측정 목표:
- 자기 도메인 문제에 AI를 전략적으로 적용할 수 있는가

표준 과제:
- 자기 실제 문제/업무/학습 주제를 가져옴
- AI와 함께 해결안/산출물 제작
- 여러 후보 비교
- 실패 조건/리스크 분석
- 최종 의사결정 근거 제출

통과 기준:
- 총점 75점 이상
- Station 2, 3에서 각각 18점 이상
- 외부 기준 또는 실제 사용자/도메인 기준으로 검증

핵심 평가:
- 단순 생성이 아니라 판단/검증을 했는가
- AI를 도구가 아니라 협업 시스템으로 썼는가
- 자기 문제에 재사용 가능한 프로세스를 만들었는가

### Level 3 — Verified AI Leader

측정 목표:
- 다른 사람을 AI 협업 과정으로 이끌 수 있는가

표준 과제:
- 타인의 문제를 받아 HypeProof 4스테이션으로 안내
- 참가자의 입력을 대신 써주지 않고 질문으로 끌어냄
- 결과물 개선 과정을 코칭
- 마지막에 참가자 성장 리포트 작성

통과 기준:
- 총점 85점 이상
- Station 4에서 20점 이상
- 코칭 관찰 평가 통과
- 참가자 결과물 완성률 기준 충족

핵심 평가:
- 남을 대신해주는가, 남이 하게 만드는가
- 질문으로 사고를 끌어내는가
- HypeProof 16원칙을 상황에 맞게 적용하는가

---

## 4. License 측정

### HypeProof Creator License

측정 목표:
- 공식 기록/랭킹/Competition에 참여할 자격이 있는가

발급 기준:
- Level 1 이상 또는 공식 Challenge 1회 완료
- 표준 기록 시스템 등록
- 부정행위/표절/대리작성 규정 동의
- 시즌 등록

유지 기준:
- 시즌 내 최소 1회 공식 Challenge 참여
- 기록/포트폴리오 갱신

### HypeProof Facilitator License

측정 목표:
- HypeProof 경기를 공식 운영하고 참가자를 코칭할 수 있는가

발급 기준:
- Level 3 취득
- 모의 운영 평가 통과
- 실제 보조 운영 1회 이상
- 안전/콘텐츠/학부모 커뮤니케이션 기준 통과
- HypeProof 승인

핵심:
- Level 3는 후보 자격
- Facilitator License는 공식 운영 권한

### HypeProof Partner License

측정 목표:
- 기관이 HypeProof 프로그램을 품질 기준에 맞게 열 수 있는가

발급 기준:
- HypeProof 승인
- 최소 1명 이상 Facilitator License 보유
- 표준 운영 매뉴얼 준수
- 기록/리포트 시스템 연동
- 브랜드 가이드 준수
- 품질 감사 수용

핵심:
- Partner License는 브랜드/커리큘럼/운영자료/마케팅자료 사용권
- 인증/기록 발급권은 HypeProof 시스템에 남긴다

---

## 5. 한 문장

**HypeProof는 시간을 재지 않는다. 대신 4주 커리큘럼을 4개 표준 스테이션으로 만들고, 입력·반복·검증·전이 능력을 같은 룰로 측정한다.**
