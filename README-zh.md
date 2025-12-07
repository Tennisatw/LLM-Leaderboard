[English version](README.md)

# 大语言模型综合排行榜

![](25-12-07/zh.png)

本表格汇总了常用大语言模型在主流评测排行榜上的表现。评测范围涵盖：

人类偏好（文字和视觉），知识与推理，数学能力，代码能力，长文本推理，和指令遵循能力。

在整合各项评测结果的基础上，计算出综合排名。

<br>

## 各榜单简介及数据来源

针对大语言模型的每一个能力，选择了1-3个榜单进行评测。在选择榜单时尽量挑选实时更新的，通用的，且有区分度的榜单。

<br>

### 人类偏好

[LLM text arena](https://huggingface.co/spaces/lmarena-ai/lmarena-leaderboard)

通过真实用户对话投票，评估大语言模型在**综合对话体验**上的表现，包括理解能力、回答质量、逻辑性和互动自然度。分数更新很快。

<br>

[LLM vision arena](https://huggingface.co/spaces/lmarena-ai/lmarena-leaderboard)

通过真实用户对话投票，评估大语言模型在**视觉相关**的模型输出上的表现，包括图像理解、描述生成、视觉推理等。

<br>

### 知识与推理能力

[MMLU-Pro](https://artificialanalysis.ai/evaluations/mmlu-pro)

一个专为更严谨评估大型语言模型语言理解与推理能力而设计的多任务难度提升版知识问答基准，共收录约 12,000 道更具挑战性的题目，选项数量从原始的 4 个增加至 10 个，同时强化了复杂推理需求与题目鲁棒性。

<br>

[GPQA-diamond](https://github.com/idavidrein/gpqa)

GPQA是一个用于评估大语言模型在高质量、专业难度问答（尤其是跨学科推理和知识深度）上的基准数据集。其中 GPQA-Diamond 是指其中最困难、最严格的人类专家编写和验证的问题子集。

<br>

[Humanity’s Last Exam（HLE）](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

HLE是一个多模态语言模型基准测试，包含约 2,500 道专家设计的跨学科难题，旨在成为衡量 AI 在封闭学术问题上人类专家水平的“最后考试”式评测。

<br>

### 数学推理

[AIME 2025](https://artificialanalysis.ai/evaluations/aime-2025)

美国数学邀请赛 (AIME) 基准测试旨在评估大型语言模型在一项面向高中生、仅限受邀参加的著名数学竞赛中的表现。该基准测试极具挑战性，涵盖代数、几何和数论等广泛的数学主题。

<br>

### 代码能力

[LiveCodeBench](https://livecodebench.github.io/leaderboard.html)

针对大型语言模型（LLM）进行 **实时代码生成与执行能力** 测评的基准，侧重评估模型在动态环境下编写、运行并修正代码的表现。

<br>

[SWE-Bench](https://www.swebench.com/)

SWE-Bench 是一个用于评估大型语言模型在真实软件工程场景中自动修复代码能力的基准数据集与测试平台，基于 GitHub 开源项目的历史问题与修复提交构建。

<br>

### 长文本推理

[AA-LCR](https://artificialanalysis.ai/evaluations/artificial-analysis-long-context-reasoning)

专注于在**超长文本**中进行分析和推理的人工智能基准与方法，用于评估模型在复杂、多层次语境下的理解与推理能力。

<br>

### 指令遵循

[IFBench](https://github.com/allenai/IFBench)

IFBench 是一个用于评估语言模型在“**精确遵循可验证指令**”能力上的基准测试。