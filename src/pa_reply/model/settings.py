import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic import BaseModel

ENV_PATH = Path(__file__).resolve().parents[3] / ".env"
load_dotenv(dotenv_path=ENV_PATH)

class Settings(BaseModel):
    model_id: str = os.getenv("MODEL_ID", "HuggingFaceH4/zephyr-7b-beta")
    hf_token: str | None = os.getenv("HF_TOKEN")
    hf_base_url: str = os.getenv("HF_BASE_URL", "https://router.huggingface.co")

    temperature: float = float(os.getenv("TEMPERATURE", "0.8"))
    max_new_tokens: int = int(os.getenv("MAX_NEW_TOKENS", "96"))

settings = Settings()
