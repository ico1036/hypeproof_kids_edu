---
type: meta
scope: startup-ir
title: "Startup Log"
created: 2026-08-17
updated: 2026-08-17
tags:
  - meta/log
  - curriculum
  - startup-ir
---

# Startup Log

창업·IR 라인(`scope: startup-ir`) 변경 이력. 최신 항목이 위. **추가 전용 — 과거 엔트리 수정 금지.**

공유 자산(`scope: common`) 변경은 [[curriculum-log]]에 기록한다. 라인 문서만 여기에 남긴다.

---

## [2026-08-17] research | 모두의 창업 프로젝트 (중기부)
- Pages: `startup-modoo-project-kr`
- Key insight: 우리가 설계하려던 IR이 **국가사업에 실물로 존재한다** — 공개 IR → Private IR → 대국민 IR 3단계, 1위 1억원, 4,000명 규모. 그리고 미성년자도 법정대리인 동의로 참가 가능해 민법 제8조 설계와 정합한다. 1R이 "관찰식 평가"라 7 Assets 측정 철학이 두 국가사업에서 모두 유효함이 확인됐다. 반면 두 개의 제약이 새로 생겼다 — **대필은 형사 문제**(작성자·도전자 전원 사기·업무방해죄)이므로 "AI가 사업계획서를 써준다"는 문구를 쓸 수 없고, **타 공모전 수상 아이디어는 공개 아이디어로 배제**되므로 청소년 대회와 모두의 창업을 같은 아이디어로 병행할 수 없다.

## [2026-08-17] split | 라인 작업 파일 분리
- 신설: `startup-hot`, `startup-log`
- Key insight: 라인을 볼트로 쪼갤 것인지 검토했고 하지 않기로 했다. `wiki/`↔`curriculum_wiki/` 분리는 결합도가 0에 가까워 성립했지만, 두 라인은 `scope: common` 26건(헌법·방법론 카드·지도안 규격)을 공유해 결합도가 높다. 복사하면 두 진실이 생기고 참조하면 이름만 분리다. **라인은 축이지 트리가 아니다** — 그래서 `scope`가 프론트매터 필드다. 경합하던 것은 지식이 아니라 작업 상태(hot·log)뿐이었으므로 그것만 쪼갰다.

## [2026-08-17] research | YEEP 벤치마크 전수 + 진단도구 충돌
- Pages: `startup-yeep-benchmark-kr`, `startup-yeep-resource-manifest`
- 원본: `.raw/yeep/` 47파일 1.1GB (gitignore, 매니페스트로 재수집)
- Key insight: 국가가 무료로 배포하는 것이 예상보다 훨씬 크다 — 모의 IR·가상 크라우드펀딩·13개 주제 교안(초중고 3종 세트)·카드덱·34차시. "IR 체험을 시킨다"는 차별점이 성립하지 않는다. 살아남는 셋(실제성·AI 검증 밀도·개인 귀속 증거)은 전부 [[seven-ai-native-assets-original]]에서 나온다. 동시에 KOEF 진단도구가 백분위·T점수·등급 명명을 쓰는데 대회 참가에 필수라 헌법 5개 조항과 충돌한다.

## [2026-08-17] ruling | 자산 승계 판정
- Pages: `ruling-startup-ir-asset-alignment`
- Key insight: 7 Assets 원본의 절대 원칙("측정은 과정 신호에서")이 대회 배점 70점과 같은 구조다. 6개 Asset이 배점 88점에 직접 대응한다. 차별점은 새로 발명할 것이 아니라 기존 자산의 직접 귀결이었다. 반대로 [[no-debug-philosophy]]는 반전된다 — 실패 직면이 20점이므로 실패를 감추면 점수가 사라진다.

## [2026-08-17] research | IR 덱 표준 3계보
- Pages: `startup-ir-deck-structures`
- Key insight: 청소년 대회 사업계획서 양식이 정부 PSST 표준의 축소판이다. 장난감 양식이 아니라 예비창업패키지로 그대로 이어지는 실사용 규격이다. 청소년판은 재무·IP를 빼고 "예상 장애 요소"·"갈등 해결 방법"을 넣었다 — 돈을 빼고 과정과 관계를 넣은 것이 70점의 정체다.

## [2026-08-17] research | 대회 심사 배점 해부
- Pages: `startup-youth-competition-kr`
- Key insight: 심사 기준이 아이템 품질이 아니라 창업가정신 역량 4군이다. 아이템 30점 / 과정·태도·협업 70점. AI로 문서를 매끄럽게 쓰면 30점은 오르지만 70점의 증거가 사라진다. 지도교사 필수·동아리 2인 이상이라 사교육 단독으로는 참가 불가.

## [2026-08-17] research | 미성년자 창업 법적 상한
- Pages: `startup-minor-legal-boundary-kr`
- Key insight: 민법 제5조만 보면 미성년자 계약은 취소 가능해 "진짜 창업"이 성립하기 어렵다. 제8조 영업 허락을 받으면 그 범위에서 성년자와 동일하다. 부모 동의서 1장이 아니라 영업 허락을 커리큘럼에 내장해야 하며, 범위를 스스로 정의해야 허락받으므로 첫 IR이 부모 대상이 된다. 법인 설립을 목표로 두면 부모가 실질 주체가 되어 학습 귀속이 흐려진다.
