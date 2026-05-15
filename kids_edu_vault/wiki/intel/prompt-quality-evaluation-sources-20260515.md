# Prompt quality / HAIC evaluation sources for HypeProof scoring

작성: 2026-05-15

## Core sources

1. Anthropic — Prompt engineering overview
- URL: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview
- Key point: Before prompt engineering, define success criteria and empirical tests. Prompting is tied to evals, not vibes.

2. Anthropic — Define success criteria and build evaluations
- URL: https://platform.claude.com/docs/en/test-and-evaluate/develop-tests
- Key point: success criteria should be specific, measurable, achievable, relevant. Prefer task-specific evals. Automate when possible. Use quantitative metrics, qualitative scales only if consistent.

3. Anthropic — Demystifying evals for AI agents
- URL: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- Key point: agent evals rely on tasks, trials, graders, transcripts/traces, outcomes, eval harnesses. Graders can be code-based, model-based, human. Transcript analysis includes turns, token usage, tool calls.

4. OpenAI — Prompt guidance
- URL: https://developers.openai.com/api/docs/guides/prompt-guidance
- Key point: prompts should define target outcome, success criteria, constraints, available context, final answer shape. Strong basis for measuring prompt completeness.

5. EvalLM — Interactive Evaluation of Large Language Model Prompts on User-Defined Criteria
- URL: https://arxiv.org/html/2309.13633v2
- Key point: prompt iteration involves testing on sample inputs, evaluating outputs, revising prompts. EvalLM supports user-defined criteria and compares prompt alternatives. Study showed more diverse criteria, twice as many outputs examined, 59% fewer revisions.

6. Evaluating Human-AI Collaboration: A Review and Methodological Framework
- URL: https://arxiv.org/html/2407.19098v2
- Key point: HAIC evaluation needs performance, interaction quality, task allocation, adaptability, and human-AI synergy; traditional efficiency/accuracy alone is insufficient.

7. Efficient multi-prompt evaluation of LLMs / PromptEval
- URL: https://arxiv.org/abs/2405.17202
- Key point: LLM evaluation is prompt-sensitive; robust evaluation should consider performance distribution across prompt variants, not one prompt. Useful for HypeProof branching/sampling metrics.

## Implication for HypeProof

HypeProof Score should not be a subjective prompt-quality grade. It should be a log-based evaluation harness:

- Task: standardized challenge brief
- Trial: one participant attempt
- Transcript/trace: full prompt-output-edit-test sequence
- Outcome: final artifact and whether it passes objective checks
- Graders:
  - code-based/log-based: turns, tokens, prompt fields, iterations, branches, tests, edits, completion
  - model-based: rubric only for dimensions not objectively countable
  - human: calibration and spot checks

## Candidate measurable dimensions

1. Prompt completeness
- target outcome present
- constraints present
- context/evidence present
- output format present
- examples/reference present

2. Iteration behavior
- number of meaningful revisions
- delta between versions
- whether feedback was specific

3. Branching/sampling
- number of alternatives generated
- number of alternatives compared
- explicit selection rationale

4. Validation behavior
- number of tests/run-throughs
- number of defects found
- number of defects fixed
- final artifact pass/fail

5. Human control
- user edits vs AI raw output
- accept/reject decisions
- rationale messages

6. Efficiency
- total time
- turns
- tokens/cost
- rework ratio

## One-liner

Official sources support a HypeProof measurement system based on success criteria, empirical evals, transcripts/traces, outcome checks, and prompt/output iteration logs — not subjective vibes.
