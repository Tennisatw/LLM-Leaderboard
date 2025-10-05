name = "Anthropicclaude-sonnet-4-5-20250929-thinking-32k"

from rename import rename

a = rename(name)
print(a)

###########

# pattern = r"claude.*sonnet.*4[.\-]?5(?!\d)"
# name = 'claude-sonnet-4-5-thinking-32k'

# import re
# print(re.search(pattern, name, flags=re.I))  # Match object if found, else None