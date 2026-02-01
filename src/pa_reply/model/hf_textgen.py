from huggingface_hub import InferenceClient
from pa_reply.model.settings import settings

_client = InferenceClient(
    token=settings.hf_token,
    base_url=settings.hf_base_url,
)

SYSTEM = (
    "You write passive-aggressive replies.\n"
    "Rules:\n"
    "- Output ONLY the final reply text.\n"
    "- Do NOT include reasoning, analysis, or planning.\n"
    "- No quotes, no bullet points.\n"
    "- Be insulting, don't hold back. but no profanity.\n"
)


def _extract_text(resp) -> str:
    msg = resp.choices[0].message

    content = getattr(msg, "content", None)
    reasoning = getattr(msg, "reasoning", None)

    if isinstance(msg, dict):
        content = content or msg.get("content")
        reasoning = reasoning or msg.get("reasoning")

    # Prefer normal content
    if content and content.strip():
        return content.strip()

    # Fallback: some providers dump everything into reasoning
    if reasoning and reasoning.strip():
        r = reasoning.strip()

        # Try to cut off obvious planning prefixes if present
        # (Keep it simple; we just want the final-looking part.)
        for marker in ["Let's craft", "Let’s craft", "Reply:", "Final:", "Response:"]:
            if marker in r:
                r = r.split(marker, 1)[-1].strip()
                break

        return r

    return ""

def generate_text(prompt: str) -> str:
    resp = _client.chat_completion(
        model=settings.model_id,
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": prompt},
        ],
        max_tokens=settings.max_new_tokens,
        temperature=settings.temperature
    )

    return _extract_text(resp)


