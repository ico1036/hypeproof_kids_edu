---
type: source
status: ingested
title: "보아치과 이후 피드백 — 치과 AI 홈페이지 만들기"
created: 2026-06-07
updated: 2026-06-07
source_type: html memo
source_path: ".raw/articles/dental-homepage-seminar-feedback-20260607.html"
origin: "그룹채팅3 클라이언트 피드백 — 보아치과 이후"
people:
  - "[[park-junghyun]]"
  - "[[lee-jaewon]]"
related:
  - "[[boa-dental]]"
  - "[[dental-homepage-seminar-v1]]"
  - "[[dental-supersearch-curriculum-v4]]"
  - "[[치과의사-curriculum-v3]]"
tags:
  - source/client-feedback
  - 치과
  - 홈페이지
  - workshop
---

# 보아치과 이후 피드백 — 치과 AI 홈페이지 만들기

## 원본

- Raw: `.raw/articles/dental-homepage-seminar-feedback-20260607.html`
- 형식: HTML 내부 메모
- 대상: 치과 대상 「AI로 홈페이지 만들기」 세미나
- 목적: 강의 공동 기획 동료 전달용
- 피드백 출처: 그룹채팅3 클라이언트 피드백, [[park-junghyun]] · [[lee-jaewon]]
- 맥락 정정: **보아치과 이후 피드백** ([[boa-dental]])

## 핵심 요약

> [[boa-dental]] 이후 피드백 기준, 치과 비전문가가 따라만 하면 실제 홈페이지가 완성되는 **요리교실식 세미나**로 설계하고, 중간중간 AI 개념·스킬을 양념처럼 넣는다.

## 추출된 요구사항

1. **요리교실 모델**
   - 참가자별 자유 제작이 아니라, 특정 치과 홈페이지 샘플 1개를 그대로 따라 만든다.
   - 본인 치과 홈페이지는 세미나 후 같은 방법으로 각자 확장한다.

2. **재료 사전 준비**
   - 로고·이미지 등 데모용 에셋은 강사 측에서 미리 준비한다.
   - 참가자에게 준비를 맡기면 복잡해지고 누락 가능성이 높다.

3. **실제 배포까지 완료**
   - 목표는 단순 제작 시연이 아니라 실제 작동하는 홈페이지를 띄우는 것까지다.
   - 비교 프레임: 기존 외주/카페24 관리비 구조 ↔ AI 셀프 제작 + 무료 배포 구조.

4. **기술 스택 제안**
   - [[gabia]]에서 도메인만 구매한다.
   - [[claude-code]]로 제작한다.
   - [[vercel]] 또는 [[cloudflare]]로 배포하여 서버비 0원을 지향한다.
   - 레퍼런스: [[hypeproof-ai-xyz]] — 1시간 안 걸려 제작한 예시.

5. **비전문가 눈높이**
   - 참가자는 [[vercel]]·[[cloudflare]] 존재 자체를 모를 수 있다는 전제로 설계한다.
   - “전부 설명”보다 “따라 하면 결과가 나오는 단계별 떠먹여주기”가 중요하다.

6. **AI 교육은 삽입형 미니 모듈**
   - 실습 흐름 사이에 토큰 등 AI 기초 개념을 짧게 넣는다.
   - 홈페이지를 더 잘 만들기 위한 skill/tip을 자연스럽게 끼워 관심을 유도한다.

## 다음 액션

- 따라 만들 샘플 치과 홈페이지 1개 확정
- 데모용 로고·이미지 에셋 패키지 준비
- [[gabia]] 도메인 구매 → [[vercel]]/[[cloudflare]] 배포 실습 동선 정리
- 단계별 “떠먹여주기” 스크립트 작성
- 중간 삽입할 AI 개념·스킬 미니 모듈 선정

## 위키 반영

- 새 스펙: [[dental-homepage-seminar-v1]]
- 관련 기존 트랙: [[치과의사-curriculum-v3]], [[dental-supersearch-curriculum-v4]]
- 새 컴포넌트/엔티티: [[boa-dental]], [[gabia]], [[cafe24]], [[claude-code]], [[vercel]], [[cloudflare]], [[hypeproof-ai-xyz]], [[park-junghyun]], [[lee-jaewon]]
