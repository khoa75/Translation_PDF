from pydantic import BaseModel
from typing import Optional

class TranslationRequest(BaseModel):
    text: str
    model: Optional[str] = "envit5"

class TranslationResponse(BaseModel):
    translated_text: str
    model_used: str

class PDFTranslationRequest(BaseModel):
    model: Optional[str] = "envit5"

class BenchmarkResponse(BaseModel):
    bleu_score: Optional[float] = None
    rouge_score: Optional[float] = None
    meteor_score: Optional[float] = None
    inference_latency: Optional[float] = None
    