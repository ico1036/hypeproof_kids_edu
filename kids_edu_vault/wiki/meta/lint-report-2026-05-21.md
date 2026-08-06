---
type: meta
title: "Lint Report 2026-05-21"
created: 2026-05-21
updated: 2026-05-21
tags:
  - meta
  - lint
status: done
---

# Lint Report: 2026-05-21

PR #9, #10, #11 머지 후속 처리 + 정기 점검.

## Summary

- 이슈 발견: 7건
- 자동 수정: 6건
- 검토 필요 잔여: 1건 (pre-existing dead links in lint-report-2026-05-15)

---

## 수정 완료

### [FIX-1] PR#9 파일 frontmatter 누락
- **대상**: `projects/sk-biopharm-bitree-hypeproof-meeting-20260512.md`
- **문제**: 파일 전체에 YAML frontmatter 없음 (type, created, tags 등 전부 누락)
- **처리**: frontmatter 추가 (type: intel, tags: sk-biopharma/bitree/meeting 등)

### [FIX-2] HYROX 파일명 kebab-case 위반 (3건)
- `HypeProof-HYROX-framework-v1.md` → `hypeproof-hyrox-framework-v1.md`
- `HypeProof-HYROX-session-20260511.md` → `hypeproof-hyrox-session-20260511.md`
- `HypeProof-assets-v0.1.md` → `hypeproof-hyrox-assets-v0.1.md`
- **연동**: `index.md`, `intel/llm-pulse/_index.md`, `runbooks/llm-pulse-update.md` wikilink 일괄 업데이트

### [FIX-3] `projects/_index.md` 누락
- **문제**: `wiki/projects/` 폴더에만 `_index.md` 없었음
- **처리**: navigational 인덱스 생성, 4개 문서 등록

### [FIX-4] dangling wikilink 제거
- **대상**: `specs/track-b/dental-supersearch-curriculum-v4.md` related 필드
- **제거**: `[[hypeproof-7-ai-native-mind-dentist-scoring-curriculum-20260520]]` (볼트에 존재하지 않는 파일)

---

## 잔여 dead links (pre-existing, 우선순위 낮음)

`meta/lint-report-2026-05-15.md` 내 참조 (이전 lint 기록으로 삭제 불필요):
- `[[2026-04-21-stack-meeting]]`, `[[assets_v0.2]]`, `[[brackets]]`, `[[deploy-code-server]]`, `[[implementer]]`, `[[production_requirements]]`, `[[rehearsal-checklist]]`, `[[reviewer]]`

기타 pre-existing:
- `[[curriculum-v0.3]]` / `[[2026-04-19-curriculum-v0.3]]` — comms 아카이브 내 참조, 페이지 삭제된 것으로 추정
- `[[mounts]]`, `[[services]]` — `decisions/adr-container-deployment.md` 내 기술 용어 약어, 실제 페이지 불필요

---

## False Positives (스캐너 한계)

- `[[dental-supersearch-engine-workshop-v2]]` — `.html` 파일로 존재 (`specs/track-b/dental-supersearch-engine-workshop-v2.html`). `.md` 전용 스캐너 false positive. Obsidian에서는 정상 해결됨.
- `[[HypeProof-assets-v0.1]]` 유형 — Python `.stem` 파싱이 `.v0.1`을 확장자로 처리하여 오탐. 실제로는 정상 링크였음 (현재 kebab-case 변환으로 해소).
