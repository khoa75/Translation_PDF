from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
import shutil
from services.pdf_translator import TranslationService

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize translation service
translation_service = TranslationService()
translation_service.load_models()

@app.get("/models")
async def get_models():
    """
    Get available translation models.
    """
    models = ["lstm", "transformer"]
    return {"models": models}

@app.post("/translate")
async def translate_text(text: str, model_type: str = "lstm"):
    """
    Translate text using the specified model.
    """
    try:
        translated_text = translation_service.translate_text(text, model_type)
        return {
            "original_text": text,
            "translated_text": translated_text,
            "model_type": model_type
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/translate-pdf")
async def translate_pdf(pdf_file: UploadFile = File(...), model_type: str = "lstm"):
    """
    Translate a PDF file using the specified model.
    """
    try:
        # Save uploaded file temporarily
        temp_file_path = f"/tmp/{pdf_file.filename}"
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(pdf_file.file, buffer)
        
        # Define output path
        output_path = f"/tmp/translated_{pdf_file.filename}"
        
        # Translate the PDF
        translation_service.translate_pdf(temp_file_path, output_path, model_type)
        
        # Return path to translated PDF
        return {"translated_pdf_path": output_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/benchmark")
async def get_benchmark_results():
    """
    Get benchmark results for all models.
    """
    # This is a placeholder implementation
    # In a real implementation, this would return actual benchmark results
    return {
        "lstm": {
            "bleu_score": 0.85,
            "rouge_score": 0.82,
            "training_time": "120s",
            "inference_time": "2.5s"
        },
        "transformer": {
            "bleu_score": 0.92,
            "rouge_score": 0.89,
            "training_time": "300s",
            "inference_time": "1.8s"
        }
    }