# Document Translation Benchmark Platform

This project builds an end‑to‑end service that converts an English PDF into a fully translated Vietnamese PDF using a custom‑trained Transformer (augmented with an existing LSTM model).

## Evolution of Neural Machine Translation: LSTM vs Transformer

### Author

Khoa

### Project Type

AI Engineer Side Project

### Duration

5 Days

---

# 1. Project Overview

## 1.1 Background

Machine Translation has evolved significantly over the last decade. Traditional Sequence-to-Sequence models based on Long Short-Term Memory (LSTM) networks were once the dominant approach for neural machine translation. However, the introduction of the Transformer architecture revolutionized the field by improving translation quality, scalability, and training efficiency.

This project aims to build a practical document translation platform while simultaneously evaluating and comparing different neural machine translation architectures.

---

## 1.2 Objectives

The system should allow users to:

- Upload English PDF documents
- Translate documents into Vietnamese
- Compare translation quality across models
- Download translated PDF files
- View benchmarking metrics

The project will compare:

1. Seq2Seq LSTM
2. Transformer

---

# 2. Project Goals

## Functional Goals

### Translation

- Translate English text into Vietnamese
- Support sentence-level translation
- Support document-level translation

### PDF Processing

- Upload PDF files
- Extract text from PDF
- Translate extracted content
- Generate translated PDF

### Benchmarking

- Compare model performance
- Display evaluation metrics
- Visualize model results

---

## Non-Functional Goals

### Performance

- Fast inference time
- Efficient memory usage

### Scalability

- Containerized deployment
- Modular architecture

### Maintainability

- Clean code structure
- Documentation
- Automated testing

---

# 3. System Architecture

```text
Frontend
    |
    v
FastAPI Backend
    |
    v
Translation Service
    |
    +--------------------+
    |                    |
    v                    v
LSTM + Attention Models  Transformer Models
    |
    v
Benchmark Moule
    |
    v
Storage Layer
```

---

# 4. Technology Stack

## Machine Learning

- Python
- PyTorch
- Hugging Face Transformers

## Backend

- FastAPI
- Uvicorn

## Frontend

- Streamlit

## Data Storage

- MongoDB

## Deployment

- Docker
- Docker Compose
- Linux VPS

---

# 5. Dataset Selection

## 5.1 Selected Dataset Strategy

To ensure the custom-trained models (Seq2Seq LSTM+Attention and Transformer) can handle the diverse nature of document translation (ranging from academic papers to technical manuals and reports), a **hybrid dataset strategy** is adopted:

### Core Training Corpus: Combined OPUS Books & MTet (Curated Subset)

- **OPUS Books:** Provides rich narrative structures and continuous context flow. However, to prevent the model from sounding overly literary or "dramatic" when translating official documents, it will be augmented with a curated subset of **MTet**.
- **MTet (VietAI):** Selected for its multi-domain coverage. A subset focusing on formal domains (tech, academic, news, and legal) will be merged with OPUS Books to balance vocabulary and adapt the models to formal document styles.

### Validation & Benchmark Datasets

- **IWSLT 2015 (TED Talks):** ~133K pairs of highly clean, academic-adjacent text. It will serve as the internal validation set during the training loop to monitor convergence.
- **FLORES-200 (Meta):** A gold-standard evaluation dataset. This will be strictly reserved for the _Benchmark Framework (Phase 4)_ to evaluate final model performance (BLEU, ROUGE) and will **never** be exposed to the models during training to prevent data leakage.

---

## 5.2 Candidate Datasets Analysis

The following datasets were evaluated during the research phase:

| Dataset Name        | Scale (Sentence Pairs) | Data Quality   | Primary Domain            | Project Role                | Justification                                                                                     |
| :------------------ | :--------------------- | :------------- | :------------------------ | :-------------------------- | :------------------------------------------------------------------------------------------------ |
| **PhoMT** _(VinAI)_ | ~3.02M                 | Very High      | News / General            | Candidate Baseline          | Gold standard for En-Vi baseline training, but mostly limited to news-style text.                 |
| **MTet** _(VietAI)_ | ~4.2M                  | High           | Multi-domain (11 Sectors) | **Selected (Subset)**       | Crucial for adapting the model to diverse document types (medical, law, tech).                    |
| **OPUS Books**      | ~100K+                 | High           | Literature / Novels       | **Selected (Core)**         | Great for long-context patterns and continuous sentence variations.                               |
| **IWSLT 2015**      | ~133K                  | Very High      | TED Talks / Academic      | **Selected (Validation)**   | Exceptionally clean alignment; ideal for fast evaluation during training epochs.                  |
| **CCMatrix**        | Multi-Million          | Medium (Noisy) | Web Crawl                 | Excluded                    | Huge scale but contains high noise levels; requires heavy preprocessing for custom architectures. |
| **FLORES-200**      | ~1,012 (per split)     | Very High      | Wiki / Miscellaneous      | **Selected (Testing Only)** | Industry-standard for zero-shot translation benchmarking and final metrics calculation.           |

---

# 6. Development Roadmap

---

## Phase 0: Research and Planning

### Duration

1 Week

### Deliverables

- Project proposal
- Dataset analysis
- Architecture design

### Outputs

```text
docs/
├── proposal.md
├── architecture.md
└── dataset_analysis.md
```

---

## Phase 1: Data Pipeline

### Duration

1 Week

### Objectives

Build a reusable preprocessing pipeline.

### Tasks

- Download dataset
- Clean data
- Tokenization
- Vocabulary creation
- Train-validation-test split

### Outputs

```text
data/
├── raw/
├── processed/
└── vocab/
```

---

## Phase 2: Baseline Seq2Seq LSTM

### Duration

1 Week

### Objectives

Implement a basic Seq2Seq LSTM model.

### Tasks

- Encoder LSTM
- Decoder LSTM
- Training pipeline
- Evaluation pipeline

### Metrics

- Training Loss
- Validation Loss
- BLEU Score

### Outputs

```text
models/
└── lstm/
```

---

## Phase 4: Transformer

### Duration

2 Weeks

### Objectives

Implement Transformer architecture.

### Tasks

- Positional Encoding
- Multi-Head Attention
- Encoder-Decoder Architecture

### Metrics

- BLEU Score
- Training Time
- Inference Time

### Outputs

```text
models/
└── transformer/
```

---

## Phase 5: Benchmark Framework

### Duration

1 Week

### Objectives

Create an evaluation framework for comparing models.

### Metrics

#### Translation Quality

- BLEU
- ROUGE
- METEOR

#### Efficiency

- Training Time
- Inference Latency
- Memory Usage

#### Model Complexity

- Number of Parameters
- Model Size

### Outputs

```text
benchmark/
├── evaluation.py
├── metrics.py
└── visualization.py
```

---

## Phase 6: PDF Translation Service

### Duration

2 Weeks

### Objectives

Translate complete PDF documents from English to Vietnamese.

### Pipeline

```text
PDF Upload
      |
      v
Text Extraction
      |
      v
Translation
      |
      v
PDF Generation
```

### Features

- Upload PDF
- Select translation model
- Download translated PDF

### Outputs

```text
services/
└── pdf_translator/
```

---

## Phase 7: Backend API

### Duration

1 Week

### Objectives

Expose translation functionality through REST APIs.

### Endpoints

```http
POST /translate
```

```http
POST /translate-pdf
```

```http
GET /benchmark
```

```http
GET /models
```

### Outputs

```text
backend/
├── api/
├── services/
└── schemas/
```

---

## Phase 8: Frontend Interface

### Duration

1 Week

### Features

- PDF Upload
- Model Selection
- Translation Results
- Benchmark Dashboard

### Outputs

```text
frontend/
```

---

## Phase 9: Dockerization

### Duration

2 Days

### Objectives

Containerize the entire application.

### Deliverables

```text
Dockerfile

docker-compose.yml
```

### Success Criteria

```bash
docker compose up
```

runs the complete system successfully.

---

## Phase 10: Deployment

### Duration

2 Days

### Objectives

Deploy the application to a Linux server.

### Deployment Stack

```text
Nginx
    |
FastAPI
    |
Translation Models
```

---

## Phase 11: Documentation

### Duration

3 Days

### Deliverables

#### README

Include:

- Installation
- Training
- Deployment
- Usage Guide

#### Technical Report

1. Introduction
2. Dataset
3. Methodology
4. Seq2Seq LSTM
5. Transformer
6. Benchmark Results
7. Deployment
8. Discussion
9. Future Work

---

# 7. Project Structure

```text
document-translation-platform/

├── backend/
├── frontend/
├── models/
│   ├── lstm/

│   └── transformer/
│
├── benchmark/
├── services/
│   └── pdf_translator/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── vocab/
│
├── docs/
├── tests/
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

# 8. Success Criteria

The project is considered complete when:

- User can upload PDF files
- User can choose a translation model
- Translation is generated successfully
- Translated PDF can be downloaded
- Benchmark dashboard is available
- Application runs via Docker
- Documentation is complete

---

# 9. Expected Learning Outcomes

By completing this project, the developer will gain experience in:

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

---

# Future Enhancements

- Vietnamese Translation
- Multi-Language Support
- Speech-to-Text Translation
- OCR Integration
- RAG-enhanced Translation
- LLM-based Translation Evaluation
- CI/CD Automation
- Kubernetes Deployment
