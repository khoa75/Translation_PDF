# Document Translation Benchmark Platform

This project builds an end-to-end service that converts an English PDF into a fully translated Vietnamese PDF using a custom-trained Transformer (augmented with an existing LSTM model).

## Features

- Upload English PDF documents
- Translate documents into Vietnamese
- Compare translation quality across models
- Download translated PDF files
- View benchmarking metrics

## Technology Stack

- Python
- PyTorch
- FastAPI
- Streamlit
- Docker

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd document-translation-platform
   ```

2. Install dependencies:
   ```
   pip install -r backend/requirements.txt
   ```

3. For frontend (Streamlit):
   ```
   pip install streamlit
   ```

## Usage

1. Start the backend server:
   ```
   uvicorn backend.main:app --host 0.0.0.0 --port 8000
   ```

2. Run the frontend:
   ```
   streamlit run frontend/app.py
   ```

3. Or use Docker for easier deployment:
   ```
   docker-compose up -d
   ```

## Project Structure

```
document-translation-platform/
├── backend/              # Backend API service
├── frontend/             # Streamlit frontend
├── models/               # Machine learning models
│   ├── lstm/             # Seq2Seq LSTM implementation
│   └── transformer/      # Transformer implementation
├── benchmark/            # Evaluation and benchmarking
├── services/              # PDF translation service
│   └── pdf_translator/   # PDF processing components
├── data/                 # Data processing and storage
└── docs/                 # Documentation
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

- BLEU scores
- ROUGE scores
- METEOR scores
- Training time
- Inference time
- Memory usage