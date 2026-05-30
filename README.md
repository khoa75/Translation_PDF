# English‑PDF → Vietnamese‑PDF Translation Service

## Overview
This project provides an end‑to‑end system that takes an **English PDF** as input, extracts its text, translates the content into **Vietnamese** using a custom‑trained **Transformer** (augmented with an existing LSTM model from `Translation.ipynb`), and generates a translated **Vietnamese PDF** for download.

## Features
- Upload English PDF files via a simple UI (Gradio or React).
- Automatic text extraction (`pdfminer.six`).
- Hybrid translation engine:
  - Fast draft with the LSTM baseline.
  - High‑quality refinement with a Transformer trained from scratch.
- PDF generation preserving paragraph flow (`fpdf2`).
- Benchmarking tools to compare BLEU, ROUGE, METEOR and inference latency.
- Docker‑compose setup for one‑click local deployment.

## Architecture
```
[Frontend] → FastAPI Backend → Translator Service
                              │
                              ├─ LSTM baseline (saved checkpoint)
                              └─ Custom Transformer (trained on EN‑VI parallel data)
                              ↓
                        PDF Generation (Vietnamese)
```

## Quick Start
```bash
# Clone the repository
git clone <repo_url>
cd Translation

# Create virtual environment
python -m venv .venv && source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Train the Transformer (optional, requires data in data/processed)
python scripts/train_transformer.py --data data/processed

# Run the API
uvicorn backend.main:app --reload
```

## Docker
```bash
# Build the image
docker build -t pdf-translator .

# Start all services (API + optional UI)
docker compose up
```
The service will be reachable at `http://localhost:8000`.

## API Endpoints
- `POST /translate-pdf` – multipart PDF upload, query param `model=lstm|transformer|ensemble`.
- `GET /health` – health check.
- `GET /metrics` – benchmark results (BLEU, latency, etc.).

## Benchmarking
```bash
python benchmark/evaluation.py --model transformer
```
Outputs BLEU, ROUGE, METEOR scores and logs inference time.

## Contributing
Feel free to open issues or pull requests. Please keep the code style consistent and update the documentation when adding new features.

## License
[MIT License](LICENSE)
