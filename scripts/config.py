# Families + forgiving alias regexes (case-insensitive).
# Tip: you can keep expanding this list; first match wins.

REPLACE = {
    "no-thinking": "",
    "w/o thinking": "",
    "4-1": "4.1",
    "3-7": "3.7",
    "3-5": "3.5",
    "-preview": "", 
    "-prerelease": "",
    "-beta": "",
    "-chat": "",
}

CATALOG = [
    # ---------- OpenAI: GPT 5 / 4.x / 4o / 4v ----------
    {"family": "gpt-5",           "aliases": [r"gpt[^\d]*5(?![\d\.])"]},
    {"family": "gpt-4.5",         "aliases": [r"gpt.*4\.?5(?!\d)"]},
    {"family": "gpt-4.1",         "aliases": [r"gpt.*4\.?1(?!\d)"]},
    {"family": "gpt-4-turbo",     "aliases": [r"gpt.*4(?![\d\.]).*turbo"]},
    {"family": "gpt-4o",          "aliases": [r"gpt.*4o(?![\d\.])"]},
    {"family": "gpt-4v",          "aliases": [r"gpt.*4v(?:\s*\(ision\))?"]},
    {"family": "gpt-4",           "aliases": [r"gpt[^\d]*4(?![\d\.])"]},
    {"family": "gpt-3.5-turbo",   "aliases": [r"gpt.*3\.?5(?![\d\.]).*turbo"]},
    {"family": "gpt-3.5",         "aliases": [r"gpt.*3\.?5(?!\d)"]},

    {"family": "o4",              "aliases": [r"\bo4(?![\d\.])"]},
    {"family": "o3",              "aliases": [r"\bo3(?![\d\.])"]},
    {"family": "o1",              "aliases": [r"\bo1(?![\d\.])"]},

    {"family": "gpt-oss",         "aliases": [r"gpt.*oss"]},

    # ---------- xAI Grok ----------
    {"family": "grok-4",          "aliases": [r"grok.*4(?![\d\.])"]},
    {"family": "grok-3",          "aliases": [r"grok.*3(?![\d\.])"]},
    {"family": "grok-2",          "aliases": [r"grok.*2(?![\d\.])"]},


    # ---------- Google Gemini ----------
    {"family": "gemini-2.5",     "aliases": [r"gemini.*2\.?5(?!\d)"]},
    {"family": "gemini-2.0",     "aliases": [r"gemini.*2\.?0(?!\d)"]},
    {"family": "gemini-1.5",     "aliases": [r"gemini.*1\.?5(?!\d)"]},
    {"family": "gemini-1.0",     "aliases": [r"gemini.*1\.?0(?!\d)"]},
    {"family": "gemini-advanced","aliases": [r"gemini.*advanced"]},

    {"family": "gemma-3",        "aliases": [r"gemma[^\d]*3(?![\d\.])"]},
    {"family": "gemma-2",        "aliases": [r"gemma[^\d]*2(?![\d\.])"]},
    {"family": "gemma-1.1",      "aliases": [r"gemma[^\d]*1\.?1(?![\d\.])"]},

    # {"family": "gemma-3n-e4b",   "aliases": [r"gemma.*3n.*e4b"]},
    # {"family": "gemma3",         "aliases": [r"gemma[^\d]*3(?:[- ]?(?:12|27|4)b)?"]},

    # ---------- Anthropic Claude ----------
    {"family": "claude-opus-4.1",    "aliases": [r"claude.*opus.*4\.?1(?!\d)", r"claude.*4\.?1(?!\d).*opus"]},
    {"family": "claude-opus-4",      "aliases": [r"claude.*opus[^\d]*4(?![\d\.])", r"claude[^\d]*4(?![\d\.]).*opus"]},
    {"family": "claude-sonnet-4",    "aliases": [r"claude.*sonnet.*4(?![\d\.])", r"claude.*4(?![\d\.]).*sonnet"]},

    {"family": "claude-3.7-sonnet",  "aliases": [r"claude.*3\.?7(?!\d).*sonnet", r"claude.*sonnet.*3\.?7(?!\d)"]},
    {"family": "claude-3.5-sonnet",  "aliases": [r"claude.*3\.?5(?!\d).*sonnet", r"claude.*sonnet.*3\.?5(?!\d)"]},
    {"family": "claude-3.5-haiku",   "aliases": [r"claude.*3\.?5(?!\d).*haiku", r"claude.*haiku.*3\.?5(?!\d)"]},
    {"family": "claude-3-opus",      "aliases": [r"claude[^\d]*3(?![\d\.]).*opus", r"claude.*opus[^\d]*3(?![\d\.])"]},
    {"family": "claude-3-sonnet",    "aliases": [r"claude[^\d]*3(?![\d\.]).*sonnet", r"claude.*sonnet[^\d]*3(?![\d\.])"]},
    {"family": "claude-3-haiku",     "aliases": [r"claude[^\d]*3(?![\d\.]).*haiku", r"claude.*haiku[^\d]*3(?![\d\.])"]},

    # ---------- Alibaba Qwen ----------
    {"family": "qwen3-coder",     "aliases": [r"qwen.*3(?![\d\.]).*coder"]},
    {"family": "qwen3",           "aliases": [r"qwen[^\d]*3(?![\d\.])"]},
    {"family": "qwen2.5",         "aliases": [r"qwen.*2\.?5(?!\d)"]},
    {"family": "qwen2",           "aliases": [r"qwen[^\d]*2(?![\d\.]|\.?5)"]},
    {"family": "qwen",            "aliases": [r"qwen(?!\d)", r"qwen[^\d]*vl"]},

    {"family": "qwq",             "aliases": [r"\bqwq\b"]},
    {"family": "qvq",             "aliases": [r"\bqvq\b"]},

    # ---------- Zhipu GLM ----------
    {"family": "glm-4.5",         "aliases": [r"glm.*4\.?5(?!\d)"]},
    {"family": "glm-4.1",         "aliases": [r"glm.*4\.?1(?!\d)"]},
    {"family": "glm-4",           "aliases": [r"glm[^\d]*4(?![\d\.])"]},

    # ---------- DeepSeek ----------
    # {"family": "deepseek-r1-distill-qwen32b", "aliases": [r"deepseek.*r1.*distill.*qwen.*32b"]},
    {"family": "deepseek-r1",    "aliases": [r"deepseek.*r1"]},

    {"family": "deepseek-v3",    "aliases": [r"deepseek.*v3(?![\d\.])"]},
    {"family": "deepseek-v2.5",  "aliases": [r"deepseek.*v2\.?5(?!\d)"]},

    # ---------- Meta Llama / NVIDIA Nemotron ----------
    {"family": "llama-4-maverick","aliases":[r"llama.*4(?![\d\.]).*maverick"]},
    {"family": "llama-4-scout",   "aliases": [r"llama.*4(?![\d\.]).*scout"]},
    {"family": "llama-4-behemoth","aliases":[r"llama.*4(?![\d\.]).*behemoth"]},
    {"family": "llama-3.3",       "aliases": [r"llama.*3\.?3(?!\d)"]},
    {"family": "llama-3.2",       "aliases": [r"llama.*3\.?2(?!\d)"]},
    {"family": "llama-3.1",       "aliases": [r"llama.*3\.?1(?!\d)"]},
    {"family": "llama-3",         "aliases": [r"llama.*3(?![\d\.])"]},
    {"family": "llama-2",         "aliases": [r"llama.*2(?![\d\.])"]},

    {"family": "nvidia-nemotron", "aliases": [r"nemotron(?:.*ultra)?"]},
    {"family": "nvlm-h",          "aliases": [r"\bnvlm.*h\b"]},
    {"family": "nvlm-d",          "aliases": [r"\bnvlm.*d\b"]},
    {"family": "nvila",           "aliases": [r"\bnvila\b"]},

    # ---------- Mistral (and tolerant “Magistral” typos) ----------
    {"family": "mistral",         "aliases": [r"\b(?:mistral|magistral)\b"]},

    # ---------- MiniMax ----------
    {"family": "minimax-m1",      "aliases": [r"(?:mini\s*max|minimax).*m1(?![\d\.])"]},
    {"family": "minimax-text-01", "aliases": [r"(?:mini\s*max|minimax).*text.*01"]},

    # ---------- Kimi ----------
    {"family": "kimi-k2",         "aliases": [r"(?:moonshotai.*kimi|kimi).*k2(?![\d\.])"]},

    # ---------- Tencent Hunyuan ----------
    {"family": "hunyuan-turbo-s",  "aliases": [r"hunyuan.*turbo.*s"]},
    {"family": "hunyuan-turbo",   "aliases": [r"hunyuan.*turbo(?![\d])"]},
    {"family": "hunyuan-large",   "aliases": [r"hunyuan.*large"]},
    {"family": "hunyuan-standard","aliases": [r"hunyuan.*standard"]},

    # ---------- Cohere / Command ----------
    {"family": "command-a",       "aliases": [r"(?:cohere\s*)?command.*a(?!\w)", r"coherecommand.*a"]},

    # ---------- Perplexity Sonar ----------
    {"family": "sonar-pro",       "aliases": [r"sonar.*pro"]},
    {"family": "sonar-reasoning", "aliases": [r"sonar.*reasoning"]},

    # ---------- Upstage Solar ----------
    {"family": "solar-pro-2",     "aliases": [r"solar.*pro.*2(?![\d\.])"]},

    # ---------- Amazon Nova ----------
    {"family": "nova-premier",    "aliases": [r"nova.*premier"]},
    {"family": "nova-pro",        "aliases": [r"nova.*pro"]},
    {"family": "nova-core",       "aliases": [r"nova.*core"]},
    {"family": "nova-experimental", "aliases": [r"amazon.*nova.*experimental"]},

    # ---------- Reka ----------
    {"family": "reka-core",       "aliases": [r"reka.*core"]},
    {"family": "reka-flash-3",    "aliases": [r"reka.*flash.*3(?![\d\.])"]},
    {"family": "reka-flash",      "aliases": [r"reka.*flash(?![\d])"]},

    # ---------- EXAONE / Phi / Tulu ----------
    {"family": "exaone-4.0-32b",  "aliases": [r"exaone.*4\.?0(?!\d).*32b"]},
    {"family": "phi-4",           "aliases": [r"phi.*4(?![\d\.])"]},
    {"family": "tulu3-405b",      "aliases": [r"tulu.*3(?![\d\.]).*405b"]},

    # ---------- Seed / Dots / Intern ----------
    {"family": "seed-1.6",        "aliases": [r"seed.*1\.?6(?!\d)"]},
    {"family": "seed-1.5-vl",     "aliases": [r"seed.*1\.?5(?!\d).*vl"]},
    {"family": "dots-vlm1",       "aliases": [r"dots.*vlm?1"]},
    {"family": "intern-s1",       "aliases": [r"intern.*s1"]},
    {"family": "internvl3",       "aliases": [r"internvl.*3(?![\d\.])"]},
    {"family": "internvl2-llama3-76b", "aliases": [r"internvl.*2.*llama.*3(?![\d\.]).*76b"]},
    {"family": "internvl2.5",     "aliases": [r"internvl.*2\.?5(?!\d)"]},
    {"family": "internvl2",       "aliases": [r"internvl.*2(?![\d\.])"]},

    # ---------- Misc remaining names ----------
    {"family": "athene-v2",       "aliases": [r"athene.*v2"]},
    {"family": "athene-70b",      "aliases": [r"athene.*70b"]},
    {"family": "aria",            "aliases": [r"\baria\b"]},
    {"family": "sensechat-vision","aliases": [r"sensechat.*vision"]},
    {"family": "points-1.5",      "aliases": [r"points.*1\.?5(?!\d)"]},
    {"family": "eagle-2.5",       "aliases": [r"eagle.*2\.?5(?!\d)"]},
    {"family": "evlm-kto",        "aliases": [r"evlm.*kto"]},
    {"family": "hpt-pro",         "aliases": [r"hpt.*pro"]},
    {"family": "rbdash-v1.2",     "aliases": [r"rbdash.*v1\.?2(?!\d)"]},
    {"family": "spare-7b",        "aliases": [r"spare.*7b"]},
    {"family": "360vl",           "aliases": [r"\b360vl\b"]},
    {"family": "telemm",          "aliases": [r"\btelemm\b"]},
    {"family": "llava-onevision", "aliases": [r"llava.*onevision"]},
    {"family": "ovis2",           "aliases": [r"ovis.*2.*34B"]},
    {"family": "ovia",            "aliases": [r"ovia"]},
    {"family": "miniCPM-V 2.0",   "aliases": [r"MiniCPM-V 2.0"]},
    {"family": "emu3",            "aliases": [r"Emu3"]},
    {"family": "yi-Large",        "aliases": [r"Yi-Large"]},
]

# CATALOG2 = [
#     # ---------- OpenAI: GPT 5 / 4.x / 4o / 4v ----------
#     {"family": "gpt-5",           "aliases": [r"gpt\s*[- ]?5(?!\d)"]},
#     {"family": "gpt-4.5",         "aliases": [r"gpt[^0-9]*4\.?5"]},
#     {"family": "gpt-4.1",         "aliases": [r"gpt[^0-9]*4\.?1(?!\d)"]},
#     {"family": "gpt-4-turbo",     "aliases": [r"gpt\s*[- ]?4\s*[- ]?turbo"]},
#     {"family": "gpt-4",           "aliases": [r"gpt[^0-9]*4\b"]},

#     {"family": "gpt-4o",          "aliases": [r"gpt\s*[- ]?4o\b", r"gpt\s*[- ]?4o\s*\("]},
#     {"family": "gpt-4v",          "aliases": [r"gpt\s*[- ]?4v", r"gpt\s*[- ]?4v\(ision\)"]},

#     {"family": "o4",              "aliases": [r"\bo4\b"]},
#     {"family": "o3",              "aliases": [r"\bo3\b"]},
#     {"family": "o1",              "aliases": [r"\bo1\b"]},

#     {"family": "gpt-oss",         "aliases": [r"gpt\s*[- ]?oss"]},

#     # ---------- xAI Grok ----------
#     {"family": "grok-2",          "aliases": [r"grok\s*[- ]?2(?!\d)"]},
#     {"family": "grok-3",          "aliases": [r"grok\s*[- ]?3(?!\d)"]},
#     {"family": "grok-4",          "aliases": [r"grok\s*[- ]?4(?!\d)"]},

#     # ---------- Google Gemini ----------
#     {"family": "gemini-advanced",     "aliases": [r"gemini\s*[- ]?advanced"]},
#     {"family": "gemini-1.0",          "aliases": [r"gemini\s*[- ]?1\.?0(?!\d)", r"gemini\s*1\.?0"]},
#     {"family": "gemini-1.5",          "aliases": [r"gemini\s*[- ]?1\.?5(?!\d)", r"gemini\s*1\.?5"]},
#     {"family": "gemini-2.0",          "aliases": [r"gemini\s*[- ]?2\.?0(?!\d)", r"gemini\s*2\.?0"]},
#     {"family": "gemini-2.5",          "aliases": [r"gemini\s*[- ]?2\.?5(?!\d)", r"gemini\s*2\.?5"]},
#     {"family": "gemma3",              "aliases": [r"\bgemma\s*3\b", r"gemma3[- ]?(12|27|4)b"]},
#     {"family": "gemma-3n-e4b",        "aliases": [r"gemma\s*3n\s*e4b"]},

#     # ---------- Anthropic Claude ----------
#     {"family": "claude-3-opus",         "aliases": [r"claude\s*3\s*opus", r"claude\s*sonnet\s*3"]},
#     {"family": "claude-3-sonnet",       "aliases": [r"claude\s*3\s*sonnet", r"claude\s*sonnet\s*3"]},
#     {"family": "claude-3-haiku",        "aliases": [r"claude\s*3\s*haiku", r"claude\s*haiku\s*3"]},
#     {"family": "claude-3.5-sonnet",     "aliases": [r"claude\s*3\.?5\s*sonnet", r"claude\s*sonnet\s*3\.?5"]},
#     {"family": "claude-3.7-sonnet",     "aliases": [r"claude\s*3\.?7\s*sonnet", r"claude\s*sonnet\s*3\.?7"]},
#     {"family": "claude-opus-4.1",       "aliases": [r"\bclaude\s*opus\s*4\.1\b", r"\bclaude\s*4\.1\s*opus\b"]},
#     {"family": "claude-opus-4",         "aliases": [r"\bclaude\s*opus\s*4(?!\.\d)\b", r"\bclaude\s*4\s*opus\b"]},
#     {"family": "claude-sonnet-4",       "aliases": [r"claude\s*sonnet\s*4", r"claude\s*4\s*sonnet"]},

#     # ---------- Alibaba Qwen ----------
#     {"family": "qwen",                  "aliases": [r"\bqwen(?!\d)", r"qwen\s*[- ]?vl\b"]},
#     {"family": "qwen2",                 "aliases": [r"\bqwen\s*2\b(?!\.?5)"]},
#     {"family": "qwen2.5",               "aliases": [r"\bqwen\s*2\.?5\b"]},
#     {"family": "qwen3-coder",           "aliases": [r"qwen3\s*[- ]?coder\s*[- ]?", r"qwen3\s*coder"]},
#     {"family": "qwen3",                 "aliases": [r"\bqwen3\b(?![-\s]*coder\b)"]},

#     {"family": "qwq",                 "aliases": [r"\bqwq\b"]},
#     {"family": "qvq",                 "aliases": [r"\bqvq\b"]},

#     # ---------- Zhipu GLM ----------
#     {"family": "glm-4.5",             "aliases": [r"\bglm\s*[- ]?4[-\s]*\.?5(?!\w)"]},
#     {"family": "glm-4.1",             "aliases": [r"\bglm\s*[- ]?4[-\s]*\.?1(?!\w)"]},
#     {"family": "glm-4",               "aliases": [r"\bglm\s*[- ]?4(?!\d)"]},

#     # ---------- DeepSeek ----------
#     {"family": "deepseek-r1",         "aliases": [r"deepseek\s*[- ]?r1", r"deepseek\s*r10528"]},
#     {"family": "deepseek-v2.5",       "aliases": [r"deepseek\s*[- ]?v2[-\s]*\.?5"]},
#     {"family": "deepseek-v3",         "aliases": [r"deepseek\s*[- ]?v3(?!\d)"]},
#     {"family": "deepseek-r1-distill-qwen32b",   "aliases": [r"deepseek\s*r1.*distill.*qwen\s*32b"]},

#     # ---------- Meta Llama / NVIDIA Nemotron ----------
#     {"family": "llama-3.1",           "aliases": [r"llama\s*3\.?1"]},
#     {"family": "llama-3.3",           "aliases": [r"llama\s*3\.?3"]},
#     {"family": "llama-4-maverick",    "aliases": [r"llama\s*4\s*maverick"]},
#     {"family": "llama-4-scout",       "aliases": [r"llama\s*4\s*scout"]},
#     {"family": "llama-4-behemoth",    "aliases": [r"llama\s*4\s*behemoth"]},

#     {"family": "nvidia-nemotron",     "aliases": [r"nemotron", r"nemotron\s*ultra"]},
#     {"family": "nvlm-h",              "aliases": [r"\bnvlm[- ]?h\b"]},
#     {"family": "nvlm-d",              "aliases": [r"\bnvlm[- ]?d\b"]},
#     {"family": "nvila",               "aliases": [r"\bnvila\b"]},

#     # ---------- Mistral (and tolerant “Magistral” typos) ----------
#     {"family": "mistral",             "aliases": [r"\bmistral\b", r"magistral"]},

#     # ---------- MiniMax ----------
#     {"family": "minimax-m1",          "aliases": [r"\bminimax\s*[- ]?m1\b", r"mini\s*max\s*m1"]},
#     {"family": "minimax-text-01",     "aliases": [r"\bminimax\s*[- ]?text\s*[- ]?01\b"]},

#     # ---------- Kimi ----------
#     {"family": "kimi-k2",             "aliases": [r"\bkimi\s*[- ]?k2\b", r"moonshotai.*kimi.*k2"]},

#     # ---------- Tencent Hunyuan ----------
#     {"family": "hunyuan-turbo",       "aliases": [r"hunyuan\s*[- ]?turbo\b"]},
#     {"family": "hunyuan-turbos",      "aliases": [r"hunyuan\s*[- ]?turbos\b"]},
#     {"family": "hunyuan-standard",    "aliases": [r"hunyuan\s*[- ]?standard"]},
#     {"family": "hunyuan-large",       "aliases": [r"hunyuan\s*[- ]?large"]},

#     # ---------- Cohere / Command ----------
#     {"family": "command-a",           "aliases": [r"(cohere)?\s*command\s*a\b", r"coherecommand[- ]?a"]},

#     # ---------- Perplexity Sonar ----------
#     {"family": "sonar-pro",           "aliases": [r"\bsonar\s*pro\b"]},
#     {"family": "sonar-reasoning",     "aliases": [r"\bsonar\s*reasoning\b"]},

#     # ---------- Upstage Solar ----------
#     {"family": "solar-pro-2",         "aliases": [r"solar\s*pro\s*2"]},

#     # ---------- Amazon Nova ----------
#     {"family": "nova-premier",        "aliases": [r"\bnova\s*premier\b"]},
#     {"family": "nova-pro",            "aliases": [r"\bnova\s*pro\b"]},
#     {"family": "nova-core",           "aliases": [r"\bnova\s*core\b"]},
#     {"family": "nova-experimental-chat","aliases":[r"amazon[- ]?nova.*experimental.*chat"]},

#     # ---------- Reka ----------
#     {"family": "reka-core",           "aliases": [r"\breka\s*core\b"]},
#     {"family": "reka-flash",          "aliases": [r"\breka\s*flash\b"]},
#     {"family": "reka-flash-3",        "aliases": [r"\breka\s*flash\s*3\b"]},

#     # ---------- EXAONE / Phi / Tulu ----------
#     {"family": "exaone-4.0-32b",      "aliases": [r"\bexaone\s*4\.?0\s*32b"]},
#     {"family": "phi-4",               "aliases": [r"\bphi\s*[- ]?4\b"]},
#     {"family": "tulu3-405b",          "aliases": [r"\btulu\s*3\s*405b"]},

#     # ---------- Seed / Dots / Intern ----------
#     {"family": "seed-1.5-vl",         "aliases": [r"\bseed\s*1\.?5\s*[- ]?vl"]},
#     {"family": "seed-1.6",            "aliases": [r"\bseed\s*1\.?6"]},

#     {"family": "dots-vlm1",           "aliases": [r"\bdots\s*\.?vlm?1"]},

#     {"family": "intern-s1",           "aliases": [r"\bintern[- ]?s1\b"]},
#     {"family": "internvl3",           "aliases": [r"\binternvl\s*3"]},
#     {"family": "internvl2.5",         "aliases": [r"\binternvl\s*2\.?5"]},
#     {"family": "internvl2",           "aliases": [r"\binternvl\s*2(?!\.5)"]},
#     {"family": "internvl2-llama3-76b","aliases": [r"\binternvl\s*2\s*[- ]?llama\s*3\s*[- ]?76b"]},

#     # ---------- Misc remaining names from your list ----------
#     {"family": "athene-v2",           "aliases": [r"\bathene\s*v2"]},
#     {"family": "athene-70b",          "aliases": [r"\bathene\s*70b"]},
#     {"family": "aria",                "aliases": [r"\baria\b"]},
#     {"family": "sensechat-vision",    "aliases": [r"sensechat.*vision"]},
#     {"family": "points-1.5",          "aliases": [r"\bpoints\s*1\.?5"]},
#     {"family": "eagle-2.5",           "aliases": [r"eagle\s*2\.?5"]},
#     {"family": "evlm-kto",            "aliases": [r"\bevlm\s*[- ]?kto\b"]},
#     {"family": "hpt-pro",             "aliases": [r"\bhpt\s*pro\b"]},
#     {"family": "rbdash-v1.2",         "aliases": [r"rbdash\s*v1\.?2"]},
#     {"family": "spare-7b",            "aliases": [r"\bspare\s*[- ]?7b"]},
#     {"family": "360vl",               "aliases": [r"\b360vl\b"]},
#     {"family": "telemm",              "aliases": [r"\btelemm\b"]},
#     {"family": "llava-onevision",     "aliases": [r"llava[- ]?onevision"]},
#     {"family": "ovia",                "aliases": [r"\bovis\s*2\b"]},
#     {"family": "ovis2",               "aliases": [r"\bovis\s*2\b"]},
# ]

TIER_MAP = {
    # size and speed descriptors
    "nano": "nano",
    "mini": "mini", "minimal": "mini",
    "small": "small",
    "flash": "flash",
    # "flash-lite": "flash-lite", "flashlite": "flash-lite",
    "lite": "lite", "light": "lite",

    # high/low descriptors
    "high": "high",
    "medium": "medium", "mid": "medium", "midlevel": "medium", "mid-level": "medium",
    "low": "low", "lo": "low",

    # release-type descriptors
    "exp": "exp", "experimental": "exp",

    # role or purpose descriptors
    "pro": "pro", "professional": "pro",

    # cognitive descriptors
    "thinking": "thinking", "reasoning": "thinking",
    "deepthink": "thinking", "deepthinking": "thinking",
    "wthinking": "thinking", "withthinking": "thinking",
    "distill": "distill",

    # marketing descriptors
    "ultra": "ultra",
    "super": "super",
    "plus": "plus",
    "max": "max",
    "turbo": "turbo",
}

import re
SIZE_PAT = re.compile(r"(\d{1,4}(?:\.\d+)?)\s?b", re.IGNORECASE)


DATE_TRAILERS = [
    re.compile(r"-20\d{2}-\d{2}-\d{2}$"),  # "Strip trailing '-YYYY-MM-DD'"
    re.compile(r"-20\d{6}$"),              # "Strip trailing '-YYYYMMDD'"
    re.compile(r"-20\d{2}-\d{2}$"),        # "Strip trailing '-YYYY-MM'"
    re.compile(r"-20\d{2}$"),              # "Strip trailing '-YYYY'"
    re.compile(r"-\d{6}$"),                # "Strip trailing '-NNNNNN' (e.g., '-250628')"
    re.compile(r"-\d{4}$"),                # "Strip trailing '-NNNN' (e.g., '-0528', '-0711')"
    re.compile(r"\([\w\s'/-]+\)$"),        # "Strip trailing parentheses containing dates or qualifiers (e.g., '(May'25)', '(10/22)')"
    re.compile(r"-20\d{6}"),               # "Strip '-YYYYMMDD'"
    re.compile(r"-\d{4}"),                 # "Strip '-NNNN'"
]
