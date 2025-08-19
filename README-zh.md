![English version](README.md)

# 大语言模型定量能力评估表

![]

本表格汇总了常用大语言模型在常用评测榜单上的表现。榜单涵盖人类偏好、知识与推理能力、数学能力、代码能力、多模态能力等多个方面。目的是评估各大模型的各项能力水平，并得出大致的综合能力排名。

This table summarizes the performance of commonly used large language models across major benchmark evaluations. The benchmarks cover various aspects such as human preference, knowledge and reasoning abilities, mathematical skills, coding proficiency, and multimodal capabilities. The goal is to assess each model's strengths and arrive at an approximate overall ranking.

本表每半个月更新一次。上次更新日期：25年08月17日。

This table is updated every two weeks. Last update date: August 17, 2025.

<br>

## 各榜单简介及数据来源 - Introduction to Each Benchmark and Data Source

针对大语言模型的每一个能力，选择了1-3个榜单进行评测。在选择榜单时尽量挑选实时更新的，通用的，且有区分度的榜单。

For each core capability of large language models, 1-3 representative leaderboards were selected for evaluation. Preference was given to leaderboards that are updated in real time, have broad applicability, and offer strong differentiation among models.

<br>

#### 人类偏好 - Human Preference

[LMArena](https://huggingface.co/spaces/lmarena-ai/lmarena-leaderboard)

<!-- https://lmarena.ai/leaderboard -->

通过真实用户对话投票，评估大语言模型在**综合对话体验**上的表现，包括理解能力、回答质量、逻辑性和互动自然度。分数更新很快。

Evaluates **overall dialogue experience** through real user voting—assessing comprehension, response quality, logic, and conversational naturalness. Scores are updated frequently.

<br>

#### 知识与推理能力 - Knowledge & Reasoning

[MMLU-Pro](https://artificialanalysis.ai/evaluations/mmlu-pro)

一个专为更严谨评估大型语言模型语言理解与推理能力而设计的多任务难度提升版知识问答基准，共收录约 12,000 道更具挑战性的题目，选项数量从原始的 4 个增加至 10 个，同时强化了复杂推理需求与题目鲁棒性。

An advanced multi-task benchmark designed to more rigorously test language understanding and reasoning. It includes ~12,000 challenging questions, increasing options from 4 to 10 and strengthening requirements for complex reasoning and question robustness.

<br>

[GPQA](https://huggingface.co/spaces/TIGER-Lab/MMLU-Pro)

一个用于评估大语言模型在高质量、专业难度问答（尤其是跨学科推理和知识深度）上的基准数据集。其中 GPQA-Diamond 是指其中最困难、最严格的人类专家编写和验证的问题子集。

A benchmark for evaluating high-quality, expert-level Q&A—especially on interdisciplinary reasoning and deep knowledge. The GPQA-Diamond subset includes the most difficult, expert-curated questions.

<br>

[Humanity’s Last Exam](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

HLE是一个多模态语言模型基准测试，包含约 2,500 道专家设计的跨学科难题，旨在成为衡量 AI 在封闭学术问题上人类专家水平的“最后考试”式评测。

A multimodal benchmark with ~2,500 expert-designed, cross-disciplinary problems. It aims to assess whether AI can match human expert performance on closed academic tasks—like a “final exam” for AI.

<br>

### 长文本推理 - Long Context Reasoning

[AA-LCR](https://artificialanalysis.ai/evaluations/artificial-analysis-long-context-reasoning)

专注于在**超长文本**中进行分析和推理的人工智能基准与方法，用于评估模型在复杂、多层次语境下的理解与推理能力。

Designed to assess a model’s ability to analyze and reason across **very long texts**, this benchmark focuses on multi-layered, complex contextual understanding and inference.

<br>

<!-- ### 指令遵循? -->

<!-- ### 事实问答？ -->

<!-- [SimpleQA](https://www.kaggle.com/benchmarks/openai/simpleqa) -->

#### 数学能力 - Mathematical Ability

[AIME2025](https://artificialanalysis.ai/evaluations/aime-2025)

美国数学邀请赛 (AIME) 基准测试旨在评估大型语言模型在一项面向高中生、仅限受邀参加的著名数学竞赛中的表现。该基准测试极具挑战性，涵盖代数、几何和数论等广泛的数学主题。

Based on the American Invitational Mathematics Examination, this benchmark tests models on highly challenging problems in algebra, geometry, and number theory—designed for elite high school math competitors.

<br>

#### 代码能力 - Coding Ability

<!-- [SWE-Bench](https://www.swebench.com/)

SWE-Bench 是一个用于评估大型语言模型在真实软件工程场景中自动修复代码能力的基准数据集与测试平台，基于 GitHub 开源项目的历史问题与修复提交构建。

<br> -->

[LiveCodeBench](https://livecodebench.github.io/leaderboard.html)

针对大型语言模型（LLM）进行 **实时代码生成与执行能力** 测评的基准，侧重评估模型在动态环境下编写、运行并修正代码的表现。

Measures real-time code generation and execution. It evaluates how well a model can write, run, and debug code dynamically in an interactive environment.

<br>

#### 多模态能力 - Multimodal Ability

[MMMU](https://mmmu-benchmark.github.io/)

一个跨学科、多模态的大规模评测基准，旨在测试大型模型在涵盖文本、图像等多模态输入下的综合理解与推理能力。

A large-scale, interdisciplinary benchmark focused on assessing a model’s ability to reason across text and image modalities. It covers a wide variety of academic topics and real-world scenarios.