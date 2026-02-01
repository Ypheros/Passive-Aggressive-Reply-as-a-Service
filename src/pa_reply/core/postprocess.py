def postprocess(text: str) -> str:
    t = (text or "").strip()
    if not t:
        return "[EMPTY_MODEL_OUTPUT]"
    return t
