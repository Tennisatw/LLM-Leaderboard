![中文版本](README-zh.md)

# LLM Quantitative Capability Evaluation Table

This table summarizes the performance of commonly used large language models (LLMs) across major benchmark evaluations. The benchmarks cover various aspects such as human preference, knowledge and reasoning abilities, mathematical skills, coding proficiency, and multimodal capabilities. The goal is to assess each model's strengths and arrive at an approximate overall ranking.

<br>

## Introduction to Each Benchmark and Data Source

For each core capability of large language models, 1-3 representative leaderboards were selected for evaluation. Preference was given to leaderboards that are updated in real time, have broad applicability, and offer strong differentiation among models.

<br>

### Human Preference

[LMArena-text](https://huggingface.co/spaces/lmarena-ai/lmarena-leaderboard)

Evaluates **overall dialogue experience** through real user voting—assessing comprehension, response quality, logic, and conversational naturalness. Scores are updated frequently.

<br>

### Knowledge & Reasoning

[MMLU-Pro](https://artificialanalysis.ai/evaluations/mmlu-pro)

An advanced multi-task benchmark designed to more rigorously test language understanding and reasoning. It includes ~12,000 challenging questions, increasing options from 4 to 10 and strengthening requirements for complex reasoning and question robustness.

<br>

[GPQA](https://huggingface.co/spaces/TIGER-Lab/MMLU-Pro)

A benchmark for evaluating high-quality, expert-level Q&A—especially on interdisciplinary reasoning and deep knowledge. The GPQA-Diamond subset includes the most difficult, expert-curated questions.

<br>

[Humanity’s Last Exam](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

A multimodal benchmark with ~2,500 expert-designed, cross-disciplinary problems. It aims to assess whether AI can match human expert performance on closed academic tasks—like a “final exam” for AI.

<br>

### Long Context Reasoning

[AA-LCR](https://artificialanalysis.ai/evaluations/artificial-analysis-long-context-reasoning)

Designed to assess a model’s ability to analyze and reason across **very long texts**, this benchmark focuses on multi-layered, complex contextual understanding and inference.

<br>

### Mathematical Ability

[AIME2025](https://artificialanalysis.ai/evaluations/aime-2025)

The American Invitational Mathematics Examination (AIME) benchmark tests models on highly challenging problems in algebra, geometry, and number theory—designed for elite high school math competitors.

<br>

### Coding Ability

<!-- [SWE-Bench](https://www.swebench.com/)

SWE-Bench 是一个用于评估大型语言模型在真实软件工程场景中自动修复代码能力的基准数据集与测试平台，基于 GitHub 开源项目的历史问题与修复提交构建。

<br> -->

[LiveCodeBench](https://livecodebench.github.io/leaderboard.html)

Measures real-time code generation and execution. It evaluates how well a model can write, run, and debug code dynamically in an interactive environment.

<br>

### Multimodal Ability

[MMMU](https://mmmu-benchmark.github.io/)

A large-scale, interdisciplinary benchmark focused on assessing a model’s ability to reason across text and image modalities. It covers a wide variety of academic topics and real-world scenarios.
