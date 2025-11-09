[中文版本](README-zh.md)

# LLM Composite Rankings

![](25-11-09/en.png)

This chart compiles the performance of commonly used large language models across major benchmark leaderboards. Evaluation categories include:

Human preference (text & vision), Knowledge and reasoning, Mathematical ability, Coding capability, Long-context reasoning, and Instruction following.

Based on the aggregated results from these evaluations, an overall ranking is produced.

<br>

## Introduction to Each Benchmark and Data Source

For each core capability of large language models, 1-3 representative leaderboards were selected for evaluation. Preference was given to leaderboards that are updated in real time, have broad applicability, and offer strong differentiation among models.

<br>

### Human Preference

[LLM text arena](https://huggingface.co/spaces/lmarena-ai/lmarena-leaderboard)

Evaluates **overall dialogue experience** through real user voting—assessing comprehension, response quality, logic, and conversational naturalness. Scores are updated frequently.

<br>

[LLM vision arena](https://huggingface.co/spaces/lmarena-ai/lmarena-leaderboard)

Evaluates **vision-related** model outputs through real user voting—assessing image understanding, description generation, visual reasoning, and more.

<br>

### Knowledge & Reasoning

[MMLU-Pro](https://artificialanalysis.ai/evaluations/mmlu-pro)

An advanced multi-task benchmark designed to more rigorously test language understanding and reasoning. It includes ~12,000 challenging questions, increasing options from 4 to 10 and strengthening requirements for complex reasoning and question robustness.

<br>

[GPQA-diamond](https://github.com/idavidrein/gpqa)

The GPQA is a benchmark for evaluating high-quality, expert-level Q&A—especially on interdisciplinary reasoning and deep knowledge. The GPQA-Diamond subset includes the most difficult, expert-curated questions.

<br>

[Humanity’s Last Exam (HLE)](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

A multimodal benchmark with ~2,500 expert-designed, cross-disciplinary problems. It aims to assess whether AI can match human expert performance on closed academic tasks—like a “final exam” for AI.

<br>

### Mathematical Ability

[AIME 2025](https://artificialanalysis.ai/evaluations/aime-2025)

The American Invitational Mathematics Examination (AIME) benchmark tests models on highly challenging problems in algebra, geometry, and number theory—designed for elite high school math competitors.

<br>

### Coding Ability

[LiveCodeBench](https://livecodebench.github.io/leaderboard.html)

Measures real-time code generation and execution. It evaluates how well a model can write, run, and debug code dynamically in an interactive environment.

<br>

[SWE-Bench](https://www.swebench.com/)

SWE-Bench is a benchmark dataset and testing platform for evaluating large language models' ability to automatically fix code in real software engineering scenarios, built on the historical issues and fix submissions of GitHub open-source projects.

<br>

### Long Context Reasoning

[AA-LCR](https://artificialanalysis.ai/evaluations/artificial-analysis-long-context-reasoning)

Designed to assess a model’s ability to analyze and reason across **very long texts**, this benchmark focuses on multi-layered, complex contextual understanding and inference.

<br>

### Instruction Following

[IFBench](https://github.com/allenai/IFBench)

IFBench is a benchmark for evaluating a language model's ability to **precisely follow verifiable instructions**.