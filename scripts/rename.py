import re
from difflib import get_close_matches
from config import REPLACE, CATALOG, TIER_MAP, SIZE_PAT, DATE_TRAILERS

def strip_dates(s: str) -> str:
    out = s
    changed = True
    while changed:
        changed = False
        for pat in DATE_TRAILERS:
            m = pat.search(out)
            if m:
                # out = out[:m.start()]
                out = out[:m.start()] + out[m.end():]
                changed = True
    return out

def extract_size(s: str):
    m = SIZE_PAT.search(s)
    return f"{m.group(1)}b" if m else None

def extract_tiers(s: str):
    tiers = []
    for k,v in TIER_MAP.items():
        if re.search(rf"{k}", s):
            tiers.append(v)
    # de-dup, keep stable order
    seen, out = set(), []
    for t in tiers:
        if t not in seen:
            seen.add(t); out.append(t)
    return out

def pick_family(s: str, catalog=CATALOG):
    # try regex alias match first
    for entry in catalog:
        for pat in entry["aliases"]:
            if re.search(pat, s, flags=re.I):
                return entry["family"]
    # fallback: fuzzy to last token-ish
    tokens = re.findall(r"[a-z0-9][a-z0-9\.\-]*", s)
    guess = "-".join(tokens[:3]) if tokens else s
    families = [c["family"] for c in catalog]
    close = get_close_matches(guess, families, n=1, cutoff=0.6)
    if not close:
        return guess
    else:
        return close[0]

def rename(raw: str, catalog=CATALOG):
    s = raw.lower()
    for old, new in REPLACE.items():
        s = s.replace(old, new)
    s = re.sub(r"\s+", " ", s.strip())
    size = extract_size(s)
    tiers = extract_tiers(s)

    s = strip_dates(s)

    family = pick_family(s, catalog)

    # build canonical in a stable order:
    # family - tier(s)? - size?
    parts = [family]
    # avoid duplicating size if family already encodes it
    for t in tiers:
        if t not in parts and t not in family:
            parts.append(t)
    if size and size not in family:         
        parts.append(size)
    # final cleanup: squeeze repeated dashes
    canonical = "-".join(p for p in parts if p)
    canonical = re.sub(r"-{2,}", "-", canonical)
    return canonical

# print(rename('Claude 3.7 Sonnet [R]'))

# gpt-4-1106-preview
# gemma-3n-e4b-it
# Llama 3.2 1B
# Qwen3 0.7b