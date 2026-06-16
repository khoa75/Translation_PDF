# Document Translation Benchmark Platform

This project builds an end‑to‑end service that converts an English PDF into a fully translated Vietnamese PDF using a custom‑trained Transformer (augmented with an existing LSTM model).

## Features

- Upload English PDF documents
- Translate documents into Vietnamese
- Compare translation quality across models
- Download translated PDF files
- View benchmarking metrics

## Technology Stack

### Machine Learning
- Python 3.13+
- PyTorch
- Hugging Face Transformers
- SentencePiece
- SpaCy

### Backend
- FastAPI
- Uvicorn

### Frontend
- Streamlit

### Data Processing
- PDFMiner.six
- PyMuPDF
- FPDF2

### Evaluation
- SACREBLEU
- ROUGE
- NLTK
- Seaborn/Matplotlib/Plotly (for visualization)

### Deployment
- Docker
- Docker Compose

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd document-translation-platform
   ```

2. Install dependencies using UV:
   ```
   uv sync
   ```

## Usage

### Backend (FastAPI)
```bash
cd src && uvicorn api.main:app --host 0.0.0.0 --port 8000
```

### Frontend (Streamlit)
```bash
streamlit run frontend/app.py
```

### Docker (Recommended for development)
```bash
docker compose up
```

The backend will be available at http://localhost:8000
The frontend will be available at http://localhost:8501

## Project Structure

```
document-translation-platform/
├── src/                    # Source code
│   ├── api/                # FastAPI application
│   │   ├── main.py         # Application entrypoint
│   │   ├── schemas.py      # Pydantic schemas
│   │   └── routers/        # API routers (future)
│   ├── services/           # Business logic
│   │   └── pdf_translator/ # PDF translation service
│   │       ├── __init__.py
│   │       ├── extractor.py # PDF text extraction
│   │       └── generator.py # PDF generation
│   ├── benchmark/          # Evaluation and benchmarking
│   │   ├── evaluation.py
│   │   ├── metrics.py
│   │   └── visualization.py
│   └── models/             # Machine learning models
│       ├── lstm/           # Seq2Seq LSTM implementation
│       │   ├── model.py
│       │   ├── train.py
│       │   └── evaluate.py
│       └── transformer/    # Transformer implementation
│           ├── model.py
│           ├── multihead_attention.py
│           └── 01_transformer_training.ipynb
├── frontend/               # Streamlit frontend
│   └── app.py
├── data/                   # Data directory (ignored by git)
│   ├── raw/
│   ├── processed/
│   └── vocab/
├── docs/                   # Documentation
│   ├── deployment.md
│   └── README.md
├── tests/                  # Tests (to be added)
├── Project_Plan.md         # Detailed project plan
├── pyproject.toml          # Dependency management
├── uv.lock                 # Lock file (not committed)
├── Dockerfile              # Docker configuration
└── docker-compose.yml      # Docker compose configuration
```

## API Endpoints

- `POST /translate` - Translate text
- `POST /translate-pdf` - Translate PDF document
- `GET /models` - Get available models
- `GET /benchmark` - Get benchmark results

## Models

The platform includes two neural machine translation models:

1. **Seq2Seq LSTM**: A traditional sequence-to-sequence model with attention mechanism
2. **Transformer**: A modern transformer architecture for improved translation quality

## Benchmarking

The platform provides comprehensive benchmarking of both models across multiple metrics:

- **Translation Quality**
  - BLEU scores
  - ROUGE scores
  - METEOR scores

- **Efficiency**
  - Training time
  - Inference latency
  - Memory usage

- **Model Complexity**
  - Number of parameters
  - Model size

## Development Roadmap

As outlined in [Project_Plan.md](./Project_Plan.md), the project follows a structured 11-phase approach:

1. **Phase 0**: Research and Planning (1 week)
2. **Phase 1**: Data Pipeline (1 week)
3. **Phase 2**: Baseline Seq2Seq LSTM (1 week)
4. **Phase 4**: Transformer (2 weeks)
5. **Phase 5**: Benchmark Framework (1 week)
6. **Phase 6**: PDF Translation Service (2 weeks)
7. **Phase 7**: Backend API (1 week)
8. **Phase 8**: Frontend Interface (1 week)
9. **Phase 9**: Dockerization (2 days)
10. **Phase 10**: Deployment (2 days)
11. **Phase 11**: Documentation (3 days)

## Success Criteria

The project is considered complete when:
- User can upload PDF files
- User can choose a translation model
- Translation is generated successfully
- Translated PDF can be downloaded
- Benchmark dashboard is available
- Application runs via Docker
- Documentation is complete

## Expected Learning Outcomes

By completing this project, developers will gain experience in:
- Natural Language Processing
- Machine Translation
- Deep Learning
- PyTorch
- Transformer Architecture
- Model Evaluation
- Backend Development
- FastAPI
- Docker
- Linux Deployment
- MLOps Fundamentals
- Product Engineering

## Future Enhancements

- Vietnamese Translation
- Multi-Language Support
- Speech-to-Text Translation
- OCR Integration
- RAG-enhanced Translation
- LLM-based Translation Evaluation
- CI/CD Automation
- Kubernetes Deployment