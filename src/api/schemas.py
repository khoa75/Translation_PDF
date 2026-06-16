from pydantic import BaseModel
from typing import List, Optional

class TranslationRequest(BaseModel):
    text: str
    model_type: str = "lstm"  # Can be "lstm" or "transformer"
    
class TranslationResponse(BaseModel):
    translated_text: str
    model_type: str
    
class PDFTranslationRequest(BaseModel):
    pdf_path: str
    model_type: str = "lstm"  # Can be "lstm" or "transformer"
    
class PDFTranslationResponse(BaseModel):
    translated_pdf_path: str
    status: str