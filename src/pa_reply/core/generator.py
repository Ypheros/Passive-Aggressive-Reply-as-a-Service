from pa_reply.core.prompts import build_prompt
from pa_reply.core.postprocess import postprocess
from pa_reply.core.safety import is_allowed
from pa_reply.model.hf_textgen import generate_text

def generate_reply(message: str, context: str | None, tone: str, length: str, language: str) -> str:
    prompt = build_prompt(message=message, context=context, tone=tone, length=length, language=language)

    raw = generate_text(prompt)
    reply = postprocess(raw)

    # If something weird comes out, degrade gracefully
    if not is_allowed(reply):
        return "I’ll respond once we keep this conversation respectful."

    return reply
