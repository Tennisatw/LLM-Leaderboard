# Families + forgiving alias regexes (case-insensitive).
# Tip: you can keep expanding this list; first match wins.

REPLACE = {
    "no-thinking": "",
    "w/o thinking": "",
    "thinking": "",
    "reasoning": "",
    "deepthinking": "",
    "[r]": "",
    # "4-1": "4.1",
    # "3-7": "3.7",
    # "3-5": "3.5",
    "-preview": "", 
    "-prerelease": "",
    "-beta": "",
    "-chat": "",
    "distill ": "distill",
    "openai": "",
    "azurephi": "phi",
    "azurewizardlm": "wizardlm",
    "anthropicclaude": "claude",
    "coherec4ai": "",
    "coherecommand": "command",
    "doubaoseed": "doubao-seed",
    "huggingfacesmollm": "smollm",
    "huggingfacezephyr": "zephyr",
    "moonshotaikimi": "kimi",
    "metallama": "llama",
    "nvidiallama": "llama",
    "metacodellama": "code-llama",
    "minimaxminimax": "minimax",
    "openchatopenchat": "openchat",
    "rwkvrwkv": "rwkv",
    "snowflakesnowflake": "snowflake",
}

CATALOG = [
    # ---------- OpenAI: GPT 5 / 4.x / 4o / 4v ----------
    {"family": "gpt-5.1",        "aliases": [r"gpt.*5[.\-]?1(?!\d)"]},
    # {"family": "gpt-5-codex",    "aliases": [r"gpt[^\d]*5(?![\d\.]).*codex"]},
    {"family": "gpt-5",          "aliases": [r"gpt[^\d]*5(?![\d\.])"]},
    {"family": "gpt-4.5",        "aliases": [r"gpt.*4[.\-]?5(?!\d)"]},
    {"family": "gpt-4.1",        "aliases": [r"gpt.*4[.\-]?1(?!\d)"]},
    {"family": "gpt-4-turbo",    "aliases": [r"gpt.*4(?![\d\.]).*turbo"]},
    {"family": "gpt-4o",         "aliases": [r"gpt.*4o(?![\d\.])"]},
    {"family": "gpt-4v",         "aliases": [r"gpt.*4v(?:\s*\(ision\))?"]},
    {"family": "gpt-4",          "aliases": [r"gpt[^\d]*4(?![\d\.])"]},
    {"family": "gpt-3.5-turbo",  "aliases": [r"gpt.*3[.\-]?5(?![\d\.]).*turbo"]},
    {"family": "gpt-3.5",        "aliases": [r"gpt.*3[.\-]?5(?!\d)"]},

    {"family": "o4",             "aliases": [r"\bo4(?![\d\.])"]},
    {"family": "o3",             "aliases": [r"\bo3(?![\d\.])"]},
    {"family": "o1",             "aliases": [r"\bo1(?![\d\.])"]},

    {"family": "gpt-oss",        "aliases": [r"gpt.*oss"]},

    # ---------- xAI Grok ----------
    {"family": "grok-4.1",       "aliases": [r"grok.*4[.\-]?1(?!\d)"]},
    {"family": "grok-4",         "aliases": [r"grok.*4(?![\d\.])"]},
    {"family": "grok-3",         "aliases": [r"grok.*3(?![\d\.])"]},
    {"family": "grok-2",         "aliases": [r"grok.*2(?![\d\.])"]},


    # ---------- Google Gemini ----------
    {"family": "gemini-3",       "aliases": [r"gemini.*3(?![\d\.])"]},
    {"family": "gemini-2.5",     "aliases": [r"gemini.*2[.\-]?5(?!\d)"]},
    {"family": "gemini-2.0",     "aliases": [r"gemini.*2[.\-]?0(?!\d)"]},
    {"family": "gemini-1.5",     "aliases": [r"gemini.*1[.\-]?5(?!\d)"]},
    {"family": "gemini-1.0",     "aliases": [r"gemini.*1[.\-]?0(?!\d)"]},
    {"family": "gemini-advanced","aliases": [r"gemini.*advanced"]},

    {"family": "gemma-3",        "aliases": [r"gemma[^\d]*3(?![\d\.])"]},
    {"family": "gemma-2",        "aliases": [r"gemma[^\d]*2(?![\d\.])"]},
    {"family": "gemma-1.1",      "aliases": [r"gemma[^\d]*1[.\-]?1(?![\d\.])"]},

    # ---------- Anthropic Claude ----------
    {"family": "claude-sonnet-4.5",  "aliases": [r"claude.*sonnet.*4[.\-]?5(?!\d)", r"claude.*4[.\-]?5(?!\d).*sonnet"]},
    {"family": "claude-opus-4.1",    "aliases": [r"claude.*opus.*4[.\-]?1(?!\d)", r"claude.*4[.\-]?1(?!\d).*opus"]},
    {"family": "claude-opus-4",      "aliases": [r"claude.*opus[^\d]*4(?![\d\.])", r"claude[^\d]*4(?![\d\.]).*opus"]},
    {"family": "claude-sonnet-4",    "aliases": [r"claude.*sonnet.*4(?![\d\.])", r"claude.*4(?![\d\.]).*sonnet"]},

    {"family": "claude-3.7-sonnet",  "aliases": [r"claude.*3[.\-]?7(?!\d).*sonnet", r"claude.*sonnet.*3[.\-]?7(?!\d)"]},
    {"family": "claude-3.5-sonnet",  "aliases": [r"claude.*3[.\-]?5(?!\d).*sonnet", r"claude.*sonnet.*3[.\-]?5(?!\d)"]},
    {"family": "claude-3.5-haiku",   "aliases": [r"claude.*3[.\-]?5(?!\d).*haiku", r"claude.*haiku.*3[.\-]?5(?!\d)"]},
    {"family": "claude-3-opus",      "aliases": [r"claude[^\d]*3(?![\d\.]).*opus", r"claude.*opus[^\d]*3(?![\d\.])"]},
    {"family": "claude-3-sonnet",    "aliases": [r"claude[^\d]*3(?![\d\.]).*sonnet", r"claude.*sonnet[^\d]*3(?![\d\.])"]},
    {"family": "claude-3-haiku",     "aliases": [r"claude[^\d]*3(?![\d\.]).*haiku", r"claude.*haiku[^\d]*3(?![\d\.])"]},
    {"family": "claude-2.1",         "aliases": [r"claude*2[.\-]?1(?![\d\.])"]},
    {"family": "claude-2.0",         "aliases": [r"claude*2[.\-]?0(?![\d\.])"]},

    # ---------- Alibaba Qwen ----------
    {"family": "qwen3-coder",     "aliases": [r"qwen.*3(?![\d\.]).*coder"]},
    {"family": "qwen3-max",       "aliases": [r"qwen.*3(?![\d\.]).*max"]},
    # {"family": "qwen3-vl",        "aliases": [r"qwen.*3(?![\d\.]).*vl"]},
    {"family": "qwen3",           "aliases": [r"qwen[^\d]*3(?![\d\.])"]},
    {"family": "qwen2.5",         "aliases": [r"qwen.*2[.\-]?5(?!\d)"]},
    {"family": "qwen2",           "aliases": [r"qwen[^\d]*2(?![\d\.]|[.\-]?5)"]},
    {"family": "qwen",            "aliases": [r"qwen(?!\d)", r"qwen[^\d]*vl"]},

    {"family": "qwq",             "aliases": [r"\bqwq\b"]},
    {"family": "qvq",             "aliases": [r"\bqvq\b"]},

    # ---------- Zhipu GLM ----------
    {"family": "glm-4.6",         "aliases": [r"glm.*4[.\-]?6(?!\d)"]},
    {"family": "glm-4.5v",        "aliases": [r"glm.*4[.\-]?5(?!\d)v"]},
    {"family": "glm-4.5",         "aliases": [r"glm.*4[.\-]?5(?!\d)"]},
    {"family": "glm-4.1",         "aliases": [r"glm.*4[.\-]?1(?!\d)"]},
    {"family": "glm-4",           "aliases": [r"glm[^\d]*4(?![\d\.])"]},

    # ---------- DeepSeek ----------
    {"family": "deepseek-r1-distill-qwen",     "aliases": [r"deepseek.*r1.*distill.*qwen"]},
    {"family": "deepseek-r1-distill-llama",    "aliases": [r"deepseek.*r1.*distill.*llama"]},
    {"family": "deepseek-r1",     "aliases": [r"deepseek.*r1"]},
    {"family": "deepseek-v3.2",   "aliases": [r"deepseek.*v3[.\-]?2(?!\d)"]},
    {"family": "deepseek-v3.1",   "aliases": [r"deepseek.*v3[.\-]?1(?!\d)"]},
    {"family": "deepseek-v3",     "aliases": [r"deepseek.*v3(?![\d\.])"]},
    {"family": "deepseek-v2.5",   "aliases": [r"deepseek.*v2[.\-]?5(?!\d)"]},

    # ---------- Meta Llama / NVIDIA Nemotron ----------
    {"family": "llama-4-maverick","aliases": [r"llama.*4(?![\d\.]).*maverick"]},
    {"family": "llama-4-scout",   "aliases": [r"llama.*4(?![\d\.]).*scout"]},
    {"family": "llama-4-behemoth","aliases": [r"llama.*4(?![\d\.]).*behemoth"]},
    {"family": "llama-3.3",       "aliases": [r"llama.*3[.\-]?3(?!\d)"]},
    {"family": "llama-3.2",       "aliases": [r"llama.*3[.\-]?2(?!\d)"]},
    {"family": "llama-3.1",       "aliases": [r"llama.*3[.\-]?1(?!\d)"]},
    {"family": "llama-3",         "aliases": [r"llama.*3(?![\d\.])"]},
    {"family": "llama-2",         "aliases": [r"llama.*2(?![\d\.])"]},

    {"family": "nvidia-nemotron", "aliases": [r"nemotron(?:.*ultra)?"]},
    {"family": "nvlm-h",          "aliases": [r"\bnvlm.*h\b"]},
    {"family": "nvlm-d",          "aliases": [r"\bnvlm.*d\b"]},
    {"family": "nvila",           "aliases": [r"\bnvila\b"]},

    # ---------- Mistral ----------
    {"family": "magistral-large", "aliases": [r"\bmagistral.*large"]},
    {"family": "magistral-medium","aliases": [r"\bmagistral.*medium"]},
    {"family": "magistral-small", "aliases": [r"\bmagistral.*small"]},
    {"family": "magistral",       "aliases": [r"\bmagistral\b"]},
    {"family": "ministral",       "aliases": [r"\bministral\b"]},
    {"family": "mixtral",         "aliases": [r"\bmixtral\b"]},
    {"family": "pixtral",         "aliases": [r"\bpixtral\b"]},
    {"family": "mistral-large",   "aliases": [r"\bmistral.*large"]},
    {"family": "mistral-medium",  "aliases": [r"\bmistral.*medium"]},
    {"family": "mistral-small",   "aliases": [r"\bmistral.*small"]},
    {"family": "mistral",         "aliases": [r"\bmistral\b"]},

    # ---------- MiniMax ----------
    {"family": "minimax-m2",      "aliases": [r"(?:mini\s*max|minimax).*m2(?![\d\.])"]},
    {"family": "minimax-m1",      "aliases": [r"(?:mini\s*max|minimax).*m1(?![\d\.])"]},
    {"family": "minimax-text-01", "aliases": [r"(?:mini\s*max|minimax).*text.*01"]},

    # ---------- Kimi ----------
    {"family": "kimi-k2",         "aliases": [r"(?:moonshotai.*kimi|kimi).*k2(?![\d\.])"]},

    # ---------- Tencent Hunyuan ----------
    {"family": "hunyuan-turbo-s", "aliases": [r"hunyuan.*turbo.*s"]},
    {"family": "hunyuan-turbo",   "aliases": [r"hunyuan.*turbo(?![\d])"]},
    {"family": "hunyuan-large",   "aliases": [r"hunyuan.*large"]},
    {"family": "hunyuan-standard","aliases": [r"hunyuan.*standard"]},

    # ---------- Cohere / Command ----------
    {"family": "aya-expanse",     "aliases": [r"aya.*expanse"]},
    {"family": "aya-vision",      "aliases": [r"aya.*vision"]},
    {"family": "command-a",       "aliases": [r"(?:cohere\s*)?command.*a(?!\w)", r"coherecommand.*a"]},
    {"family": "command-r",       "aliases": [r"(?:cohere\s*)?command.*r(?!\w)", r"coherecommand.*r"]},

    # ---------- Perplexity Sonar ----------
    {"family": "sonar-pro",       "aliases": [r"sonar.*pro"]},
    {"family": "sonar-reasoning", "aliases": [r"sonar.*reasoning"]},

    # ---------- HuggingFace smollm / zephyr ----------
    {"family": "smollm-2",        "aliases": [r"smollm.*2(?![\d\.])"]},
    {"family": "zephyr",          "aliases": [r"zephyr"]},

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
    {"family": "exaone-4.0",      "aliases": [r"exaone.*4[.\-]?0(?!\d)"]},
    {"family": "phi-4",           "aliases": [r"phi.*4(?![\d\.])"]},
    {"family": "phi-3",           "aliases": [r"phi.*3(?![\d\.])"]},
    {"family": "tulu-3",          "aliases": [r"tulu.*3(?![\d\.])"]},
    {"family": "tulu-2",          "aliases": [r"tulu.*2(?![\d\.])"]},

    # ---------- Seed / Dots / Intern ----------
    {"family": "doubao-seed-code", "aliases": [r"seed.*code"]},
    {"family": "seed-1.6",        "aliases": [r"seed.*1[.\-]?6(?!\d)"]},
    {"family": "seed-1.5-vl",     "aliases": [r"seed.*1[.\-]?5(?!\d).*vl"]},
    {"family": "dots-vlm1",       "aliases": [r"dots.*vlm?1"]},
    {"family": "intern-s1",       "aliases": [r"intern.*s1"]},
    {"family": "internvl3",       "aliases": [r"internvl.*3(?![\d\.])"]},
    {"family": "internvl2-llama3", "aliases": [r"internvl.*2.*llama.*3(?![\d\.]).*76b"]},
    {"family": "internvl2.5",     "aliases": [r"internvl.*2[.\-]?5(?!\d)"]},
    {"family": "internvl2",       "aliases": [r"internvl.*2(?![\d\.])"]},

    # ---------- Misc remaining names ----------
    {"family": "360vl",           "aliases": [r"\b360vl\b"]},
    {"family": "aria",            "aliases": [r"aria"]},
    {"family": "athene-v2",       "aliases": [r"athene.*v2"]},
    {"family": "athene",          "aliases": [r"athene"]},
    {"family": "eagle-2.5",       "aliases": [r"eagle.*2[.\-]?5(?!\d)"]},
    {"family": "emu3",            "aliases": [r"Emu3"]},
    {"family": "evlm-kto",        "aliases": [r"evlm.*kto"]},
    {"family": "hermes",          "aliases": [r"hermes"]},
    {"family": "hpt-pro",         "aliases": [r"hpt.*pro"]},
    {"family": "llava-onevision", "aliases": [r"llava.*onevision"]},
    {"family": "miniCPM-V 2.0",   "aliases": [r"MiniCPM-V 2.0"]},
    {"family": "openchat",        "aliases": [r"openchat"]},
    {"family": "ovis2",           "aliases": [r"ovis.*2.*34B"]},
    {"family": "ovia",            "aliases": [r"ovia"]},
    {"family": "points-1.5",      "aliases": [r"points.*1[.\-]?5(?!\d)"]},
    {"family": "rbdash-v1.2",     "aliases": [r"rbdash.*v1[.\-]?2(?!\d)"]},
    {"family": "sensechat-vision","aliases": [r"sensechat.*vision"]},
    {"family": "spare",           "aliases": [r"spare"]},
    {"family": "telemm",          "aliases": [r"\btelemm\b"]},
    {"family": "yi-Large",        "aliases": [r"Yi-Large"]},
    {"family": "minicpm-v-2_6",   "aliases": [r"minicpm-v-2_6"]},
]

TIER_MAP = {
    # size and speed descriptors
    "nano": "nano",
    "mini": "mini", "minimal": "mini",
    "small": "small",
    "flash": "flash",
    "fast": "fast",
    # "flash-lite": "flash-lite", "flashlite": "flash-lite",
    "lite": "lite",

    # # high/low descriptors
    # "high": "high",
    # "medium": "medium", "mid": "medium", "midlevel": "medium", "mid-level": "medium",
    # "low": "low", "lo": "low",

    # release-type descriptors
    "exp": "exp", "experimental": "exp",
    "pro": "pro", "professional": "pro",

    # cognitive descriptors
    "thinking": "reasoning", "reasoning": "reasoning",
    "deepthink": "reasoning", "deepthinking": "reasoning",
    "wthinking": "reasoning", "withthinking": "reasoning",
    # "instruct": "instruct",

    # marketing descriptors
    "ultra": "ultra",
    "super": "super",
    "plus": "plus",
    "max": "max",
    "turbo": "turbo",

    # others
    "nemotron": "nemotron",
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
    re.compile(r"\.\d{2}-\d{2}"),          # "Strip '.MM-DD'"
    re.compile(r"-\d{4}"),                 # "Strip '-NNNN'"
]
