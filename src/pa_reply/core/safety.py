BANNED_SUBSTRINGS = [
    "kill yourself",
    "i will kill",
]

def is_allowed(text: str) -> bool:
    lower = text.lower()
    return not any(b in lower for b in BANNED_SUBSTRINGS)
