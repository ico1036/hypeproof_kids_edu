---
type: meta
title: "Hot Cache"
created: 2026-04-12
updated: 2026-05-15
tags:
  - meta/cache
---

# Hot Cache — 2026-05-15

최근 컨텍스트 스냅샷. 세션 시작 시 가장 먼저 읽을 것.

---

## 현재 상태: SK바이오팜 파일럿 진입 + HypeProof Studio 개발 시작 + HYROX 문서 구조 동기화

### 가장 최근 작업 (2026-05-15)

**HYROX 브랜치 wiki 구조 동기화 진행**
- 작업 브랜치: `sync-hyrox-to-upstream-wiki-structure-20260515`
- 기준: `upstream/main` 최신 vault 구조 (`sources/`, `questions/`, `meta/`, kebab-case, frontmatter 필수)
- HYROX 프로젝트 문서 파일명을 kebab-case로 변환하고 [[projects/_index]] 생성
- [[index]], [[log]], [[hot]], [[intel/_index]]에 HYROX 관련 문서 등록
- HTML artifacts (`HypeProof-HYROX-proposal-v1.html`, `HypeProof-pricing-benchmark.html`)는 wiki 페이지로 등록하지 않고 [[hypeproof-hyrox-framework-v1]]의 related artifact로만 참조

**HYROX 가격정책 최근 결론**
- 참가자 가격은 단일 기준: **₩15만 / 인·시간**
- Starter Program 4h = **₩60만 / 인·가족**
- 파일럿·단체 도입은 **₩40만~60만 / 인·가족** 범위 조정
- Level 1·2·3은 결제 상품이 아니라 Challenge 결과로 부여되는 검증 등급
- Facilitator/Partner License는 참가자 가격정책에서 제외하고 추후 운영자/B2B 모델에서 별도 설명

**PR#7 `feature/langgraph-gemini` → main 머지 완료**
- [[langgraph]]+[[gemini-2-5-flash]] 백엔드 전환 PR이 리뷰 후 main에 머지됨
- 파일럿 후 처리 예정: Ping/Pong 하트비트, iframe CSP, 10턴+ rolling summary

---

## 주요 임박 마일스톤

| 기한 | 내용 |
|---|---|
| 2026-05-15~30 | HypeProof Studio v0.1 빌드 |
| 2026-05-28~30 | 운영진 자녀 dry-run (4시간) — **게이트** |
| 2026-05-말 | [[sk-biopharma]] 수요조사용 제안서 제출 |
| 2026-06-01 | Studio v0.1 release + 가족 안내 메일 |
| 2026-06 (2~3주) | [[sk-biopharma]] 1회차 |

---

## 핵심 페이지

- [[projects/_index]] · [[hypeproof-hyrox-framework-v1]] · [[hypeproof-hyrox-session-20260511]]
- [[hypeproof-license-strategy-from-hyrox-20260515]] · [[hypeproof-measurement-rubric-from-hyrox-20260515]]
- [[2026-05-12-sk-biopharma-meeting]] · [[2026-05-14-sk-biopharma-followup]]
- [[sk-biopharma]] · [[bitree]] · [[oh-sungeun]]
- [[hypeproof-studio]] · [[adr-hypeproof-studio-v01]] · [[sixteen-essence]]
- [[sk-biopharma-pilot]]

---

## 스택 요약

| 레이어 | 기술 |
|---|---|
| 백엔드 | FastAPI + [[langgraph]] + [[gemini-2-5-flash]] |
| 프론트 | Next.js (App Router) |
| 관측성 | [[langfuse-observability]] v2 self-hosted |
| 교육 도구 | [[hypeproof-studio]] v0.1 (예정) / Cline (Plan B) |
