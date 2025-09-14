大语言模型综合排行榜-250914

简介：
本表格汇总了常用大语言模型在主流评测排行榜上的表现。评测范围涵盖：
人类偏好（文字和视觉），知识与推理，数学能力，代码能力，和长文本推理。
在整合各项评测结果的基础上，计算出综合排名。

更新：
本周阿里通义千问新更新的模型中，qwen3-80b，qwen3-max和qwen3-30b上榜了。qwen3-80b仅有80亿参数，但表现相当不错。
Hugging Face在上周发布的的hermes-4-405b-reasoning也上榜了，不过没有特别亮眼的表现。
综合排名算法进行了微调：结合 Z-score 平均排名、Borda 计数法和 SVD 插补取均值 三种方法，使结果更合理稳健。
此外，微调了一下外观（在gpt-5的帮助下），希望它能稍稍好看一点。

评价：
综合实力最强的模型仍然是gpt-5，远超所有的对手。订阅openai的pro会员（200$/月）即可使用。只要预算够用，无脑冲这个。
最强的“免费”模型仍然是gemini-2.5-pro，可以在 https://aistudio.google.com/ 网站试用。同时该站点也可体验目前地表最强的文生图模型nano-banana。
最强的国内能用的模型仍然是阿里的qwen3-235b。有钱真的是为所欲为啊。此外，虽然其综合排名不是第一，但是“中文能力显著优于绝大多数国外大模型，写作时更符合中文逻辑结构和修辞习惯”（qwen3-235b自评）。日常生活可以考虑用它来当作主力模型。
编程/代码能力纸面上最强的是grok-4。但若综合考量工具调用、系统集成、上下文长度，以及使用手感，claude code还是很舒服的。
各开源模型的能力也毫不逊色。尤其是qwen3-30b，在能力不逊于claude-3.7-sonnet的情况下，参数量已经低到可以在本地台式机上跑了（虽然还是很吃显卡）。

本项目地址：https://github.com/Tennisatw/LLM-Leaderboard 。如果觉得本图有帮助，欢迎点个star。

<br>

LLM Composite Rankings–250914

Overview:
This table summarizes the performance of commonly used large language models across major benchmark rankings. The evaluation covers: Human preference (text and vision), Knowledge and reasoning, Mathematical ability, Coding ability, Long-context reasoning.
An overall ranking is calculated by aggregating results from these benchmarks.

Updates:
This week, several updated models from Alibaba's Qwen series made the list: Qwen3-80B, Qwen3-Max, and Qwen3-30B. Notably, Qwen3-80B has only 8 billion parameters but performs impressively well.
Hugging Face’s recently released Hermes-4-405B-Reasoning also joined the rankings, though it didn’t stand out significantly.
The overall ranking algorithm has been fine-tuned, now incorporating Z-score average ranking, Borda count, and SVD imputation with mean averaging, making the results more balanced and robust.
The visual design has been slightly improved (with the help of GPT-5)—hopefully it looks a bit nicer now.

Evaluation:
GPT-5 remains the most powerful model overall, far surpassing all competitors. It's available via an OpenAI Pro subscription at $200/month. If budget isn't a concern, this is the go-to choice—no hesitation needed.
The strongest free model is still Gemini 2.5 Pro, which can be tested at https://aistudio.google.com/
. The site also hosts Nano-Banana, currently the most powerful text-to-image model available.
The best model available domestically in China remains Qwen3-235B from Alibaba. As they say, "money talks." While it’s not ranked #1 overall, it claims to offer superior Chinese language capabilities, producing writing that aligns better with Chinese logic and rhetorical norms (according to Qwen3-235B itself). For daily use in Chinese, it’s a strong contender as your main model.
On paper, Grok-4 leads in coding ability, but when considering tool use, system integration, context length, and overall user experience, Claude Code still feels smoother.
Open-source models are holding their own. In particular, Qwen3-30B matches the capabilities of Claude 3.7 Sonnet, while being lightweight enough to run on a desktop machine (though still GPU-intensive).

Project link: https://github.com/Tennisatw/LLM-Leaderboard . If you find this chart helpful, please give it a star.