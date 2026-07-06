---
type: source
title: "보아치과 AI 홈페이지 실습 큐시트"
source_type: document
source_date: 2026-07-06
ingested: 2026-07-06
raw:
  - ".raw/documents/boa-dental-ai-homepage-cuesheet-20260706.pdf"
  - ".raw/documents/boa-dental-ai-homepage-cuesheet-20260706.html"
  - ".raw/documents/boa-dental-ai-homepage-cuesheet-20260706.txt"
related:
  - "[[boa-dental]]"
  - "[[boa-dental-ai-homepage-cuesheet-20260706-spec]]"
  - "[[dental-website-copyclone-v3]]"
  - "[[hypeproof-studio]]"
tags:
  - source/document
  - boa-dental
  - workshop/cuesheet
  - track-b
---

# 보아치과 AI 홈페이지 실습 큐시트

## Source

- 원본 PDF: `.raw/documents/boa-dental-ai-homepage-cuesheet-20260706.pdf`
- 원본 HTML: `.raw/documents/boa-dental-ai-homepage-cuesheet-20260706.html`
- 텍스트 추출본: `.raw/documents/boa-dental-ai-homepage-cuesheet-20260706.txt`

## 요약

2026-07-06 기준 보아치과 AI 홈페이지 실습의 2시간 큐시트 정본. 외부에 보여줄 수 있는 형태로, 발표/해커톤 감성을 빼고 시간대별 진행 콘텐츠만 남긴 문서다.

## 운영 방식

- 수강생: 치과원장 11명
- 운영진: 메인강사 1명, 보조강사 5명
- 지원 배치: 보조강사 1명당 수강생 2명 담당, 11번째 수강생은 3인 포드 배치
- 메인강사는 보아치과 홈페이지를 만든다고 가정하고 스크린을 띄워 단계별로 진행한다.
- 수강생은 같은 단계에서 각자 병원 홈페이지를 만들고, 보조강사는 중간중간 막히는 부분을 현장에서 지원한다.

## 최종 결과물

1. 홈페이지
2. 배포 URL
3. GitHub 저장소
4. `agent.md` 인수인계 문서

## 사전 준비물

1. BOA 치과 완성 데모
2. HypeProof Studio 등록 플로우: 설치, 학생 등록, 토큰 발급, 토큰 입력, 채팅 테스트 5분 컷
3. 배포 스킬: Cloudflare, GitHub Pages
4. 디자인 스킬
5. Playwright MCP

## 핵심 변경점

- 강의 방식은 메인강사와 수강생을 분리해 두 번 설명하지 않는다. 메인강사가 보아치과 홈페이지를 만드는 화면을 기준으로 진행하고, 수강생은 같은 시간에 자기 병원 홈페이지를 따라 만든다.
- Context Engineering은 `URL만 넣은 1차 결과`와 `병원 컨텍스트를 자세히 넣은 2차 결과`의 차이를 체감시키는 구간이다.
- Loop Engineering은 루브릭을 정의한 뒤 Playwright MCP 등으로 검사하고, 미달 항목을 수정하며, 루브릭을 만족할 때까지 반복시키는 구간이다.
- Context/Loop 세션 말미에는 보조강사가 현장에서 발견한 best-case를 큐레이션한다. 큐레이션 대상 기준은 `*봉호님 작성 예정`으로 남긴다.
- 20:35-20:58의 최종안 고정은 홈페이지 최종안 저장, 배포 URL 생성, GitHub 저장소에 지금까지 작업한 내용 업로드, `agent.md` 업로드까지 포함한다.

## 관련 스펙

- 운영 정본: [[boa-dental-ai-homepage-cuesheet-20260706-spec]]
- 기존 설계 맥락: [[dental-website-copyclone-v3]]
- 대상 이해관계자: [[boa-dental]]
