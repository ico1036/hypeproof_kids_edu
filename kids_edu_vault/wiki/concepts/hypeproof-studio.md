---
type: concept
title: "HypeProof Studio"
created: 2026-05-14
updated: 2026-07-06
tags:
  - concept/product
  - concept/tool
status: in-progress
---

# HypeProof Studio

HypeProof Lab의 자체 교육 IDE. VS Code fork 기반 + 자체 chat panel 통합.  
SK바이오팜 1회차에서 첫 데뷔 예정.

---

## 제품 구성

| 레이어 | 기술 |
|---|---|
| IDE 본체 | VS Code fork (Track A) |
| Chat Panel | 자체 chat panel UI (Track B, 병렬 빌드) |
| 백엔드 | HypeProof Proxy (Anthropic API 중계 + 측정 데이터 수집) |

---

## 버전 로드맵

| 버전 | 목표일 | 주요 기능 |
|---|---|---|
| v0.1 | 2026-06-01 | Mac 우선, Win v0.1.1(회차 직전), 기본 chat panel |
| v0.1.1 | SK바이오팜 1회차 직전 | Windows 지원 |
| v0.2 | 2026-07 이후 | STT(음성 입력), web 모드, auto-update (국립암센터 대비) |

---

## 차별점

- **STT 통합** (v0.2~): 8~12세 타이핑 부담 해소
- **Manual-approve 모드 강제**: file write/exec 시 부모 승인 필수
- **HypeProof Proxy**: API 중계 + 측정 데이터 자동 수집 → [[sixteen-essence]] 행동 매핑
- **브랜드**: 100% HypeProof Lab 브랜딩 (Cline·VS Code 레퍼런스 노출 없음)

---

## 빌드 계획 (v0.1)

- **Track A**: VS Code fork — IDE 전체 (메인)
- **Track B**: 자체 chat panel UI — Freelancer 1인 전담 검토 ($5~8K)
- **데드라인 게이트**: 5/28 dry-run (운영진 자녀 대상 4시간)
  - 미달 시 Plan B: Cline + HypeProof Proxy로 1회차 운영

---

## Plan B

5/28 dry-run 미달 시 대안:
- **도구**: Cline + HypeProof Proxy
- **데뷔**: Studio 8월 정식 데뷔 (국립암센터 일정 맞춤)

---


## SK바이오팜 게임 제작 모드 (2026-06-08)

SK바이오팜 가족 AI 게임 창작 수업은 봉호 커리큘럼을 본체로 두고 Studio로 구현한다. 봉호 커리큘럼을 구현하는 Studio는 범용 코딩툴 대체물이 아니라, 아이/가족이 4시간 안에 게임 제작 루프를 완주하도록 돕는 guided education OS다.

- Skill Pack: [[hypeproof-studio-game-skillpack-v1]]
- 핵심 기능: 게임 목표 설정, 캐릭터/세계/규칙 입력, 안전 룰 적용, V1 생성, 플레이 검증, V2/V3 개선, 발표 카드, 7 Assets 리포트 데이터 저장
- 방향: 게임 제작에 특화된 스킬·룰·프롬프트를 사전 탑재하여 실패율을 낮춘다.

## 보아치과 홈페이지 제작 모드 (2026-06-29)

[[2026-06-29-weekly-on-hypeproof]]에서 보아치과 강의는 Studio가 단순 코드 생성기가 아니라 전후 비교와 수정 과정을 남기는 교육 OS여야 한다고 정리됐다.

- 목표 산출물: 홈페이지 초안, 가능하면 공개 URL
- 핵심 로그: 첫 V1, 설명 카드/Context Pack, 피드백 루프, 최종본, 발표용 Before/After
- 교육 가치: 수강자가 "AI에게 무엇을 설명해야 결과가 달라지는지"와 "원하는 방향까지 어떻게 반복 수정하는지"를 체화
- 운영 리스크: 리허설 전 Claude Code 대비 Studio 성능 격차를 테스트하고, 필요하면 fallback을 준비해야 한다.

## 보아치과 2시간 실습 운행 조건 (2026-07-06)

[[boa-dental-ai-homepage-cuesheet-20260706-spec]] 기준, Studio 세팅은 19:10-19:30 구간 안에 완료되어야 한다.

- 등록 플로우: 설치, 학생 등록, 토큰 발급, 토큰 입력, 채팅 테스트를 5분 컷으로 준비
- 사용 목적: Reference First, Context Engineering, Loop Engineering, 최종 URL/GitHub/`agent.md` 업로드까지 한 흐름에서 운행
- 보조 도구: 디자인 스킬, 배포 스킬, Playwright MCP
- 핵심 로그: URL만 넣은 1차 초안, 병원 컨텍스트 반영 2차 초안, 루브릭 검사/수정 반복, 최종 산출물과 `agent.md`

## ADR

[[adr-hypeproof-studio-v01]]

---

## 관련 페이지

- [[adr-hypeproof-studio-v01]]
- [[sixteen-essence]]
- [[2026-05-14-sk-biopharma-followup]]
- [[sk-biopharma-pilot]]
