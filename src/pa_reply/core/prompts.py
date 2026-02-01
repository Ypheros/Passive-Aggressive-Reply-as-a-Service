TONE_GUIDANCE = {
    "mild": "Lightly passive-aggressive, polite, subtle.",
    "medium": "Clearly passive-aggressive, witty, not insulting.",
    "nuclear": "Very passive-aggressive and sharp, but no threats or hate.",
}

LENGTH_GUIDANCE = {
    "short": "1-2 sentences.",
    "medium": "2-4 sentences.",
    "long": "4-7 sentences.",
}

def build_prompt(message: str, context: str | None, tone: str, length: str, language: str) -> str:
    ctx = f"Context: {context}\n" if context else ""
    return (
        f"Language: {language}\n"
        f"Tone: {TONE_GUIDANCE[tone]}\n"
        f"Length: {LENGTH_GUIDANCE[length]}\n\n"
        f"{ctx}"
        f"Incoming message: {message}\n"
        f"Write the reply:"
    )
