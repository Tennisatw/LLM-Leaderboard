{
    "glm-4.5v": "glm-4.5v",
    "DeepSeek R1Distill Qwen32B": "deepseek-r1-distill-qwen-32B"
}

import re

pattern = r"deepseek.*r1.*distill.*qwen"
text = "DeepSeek R1Distill Qwen32B"

print(re.match(pattern, text, re.IGNORECASE))