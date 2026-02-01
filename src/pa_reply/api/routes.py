from fastapi import APIRouter
from .schemas import GenerateRequest, GenerateResponse
from pa_reply.core.generator import generate_reply
from pa_reply.model.settings import settings

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok"}

@router.post("/generate", response_model=GenerateResponse)
def generate(req: GenerateRequest):
    reply = generate_reply(
        message=req.message,
        context=req.context,
        tone=req.tone,
        length=req.length,
        language=req.language,
    )
    return GenerateResponse(reply=reply, model_id=settings.model_id)
