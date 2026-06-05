# AGENTS Overview

The **Document Translation Benchmark Platform** is organized as a collection of loosely‑coupled agents (services/components) that communicate through well‑defined interfaces.  Below is a concise description of each agent, their responsibilities, and the primary files/folders where their implementation lives.

---

## 1. Frontend Agent
**Location:** `frontend/`
**Type:** UI / client‑side application (Gradio *or* React + Vite).  
**Responsibilities:**
- Accept PDF uploads from the user.
- Allow model selection (LSTM, Transformer).
- Display translation results and benchmark visualizations.
- Communicate with the **Backend API Agent** via HTTP.

---

## 2. Backend API Agent
**Location:** `backend/`
**Framework:** FastAPI (served by Uvicorn).
**Responsibilities:**
- Expose REST endpoints:
  - `POST /translate` – translate raw text.
  - `POST /translate-pdf` – end‑to‑end PDF translation.
  - `GET /models` – list available translation models.
  - `GET /benchmark` – retrieve latest benchmark results.
- Validate requests using **pydantic** schemas.
- Forward work to the **Translation Service Agent** and **Benchmark Agent**.
- Return JSON responses or streamed PDF files.

---

## 3. Translation Service Agent
**Location:** `services/pdf_translator/`
**Responsibilities:**
- **PDF Extraction** – `extractor.py` uses `pdfminer.six` or `PyMuPDF` to obtain raw English text.
- **Model Invocation** – loads a model from the **Model Agents** (LSTM / Transformer) and performs inference.
- **PDF Generation** – `generator.py` writes the translated Vietnamese text back to PDF using `fpdf2` or `reportlab`.
- Handles model‑selection logic supplied by the API.

**Implementation Status:** Partially implemented
- PDF extraction functionality implemented
- Translation pipeline in progress
- PDF generation pending implementation

---

## 4. Model Agents
### 4.1 LSTM Agent
**Location:** `models/lstm/`
- Implements a classic Seq2Seq LSTM encoder‑decoder.
- Provides `train.py`, `model.py` and checkpoint handling.


### 4.3 Transformer Agent
**Location:** `models/transformer/`
- Implements a full Transformer architecture (or fine‑tunes a HuggingFace `MarianMT` / `M2M100` model).
- Handles positional encoding, multi‑head attention, and encoder‑decoder stacks.

All three agents expose a common helper function `get_model(name: str) -> torch.nn.Module` defined in `models/__init__.py` so that the **Translation Service Agent** can load any model by name.

**Implementation Status:** Implemented
- Model architecture implemented
- Training pipeline pending implementation
- Evaluation metrics pending implementation

---

## 5. Benchmark Agent
**Location:** `benchmark/`
**Responsibilities:**
- **Evaluation** – `evaluation.py` computes BLEU, ROUGE, METEOR on a validation set.
- **Metrics Recording** – `metrics.py` stores per‑epoch loss, accuracy, and timing.
- **Visualization** – `visualization.py` produces plots (matplotlib/plotly) for loss curves and benchmark dashboards.
- Results are consumed by the **Frontend Agent** (or a separate dashboard service) via the `GET /benchmark` endpoint.

---

## 6. Storage Layer Agent
**Location:** `data/` and optional database (`backend/services/` with SQLModel or Motor).
**Responsibilities:**
- Persist raw PDFs, processed tokenized data, and vocabularies.
- Store model checkpoints (`models/**/checkpoint.pt`).
- Optionally maintain a PostgreSQL / MongoDB instance for metadata (experiment logs, benchmark scores).

---

## 7. Orchestration / Docker Agent
**Location:** `Dockerfile`, `docker-compose.yml`
**Responsibilities:**
- Build container images for **Backend API**, **Frontend**, and optional **Database**.
- Wire networking so that the frontend can reach the backend (`http://backend:8000`).
- Provide a single `docker compose up` command that launches the full system, satisfying the **Success Criteria** section of the plan.

---

## 8. Documentation Agent
**Location:** `docs/` and `README.md`
**Responsibilities:**
- Host architecture diagrams, setup guides, and API specifications.
- Keep the project up‑to‑date with generated OpenAPI docs from FastAPI.

---

### How the Agents Interact
```text
Frontend ⇄ Backend API ⇄ Translation Service ⇄ {LSTM | Transformer}
                 │                         │
                 └─ Benchmark Agent ⇄ Storage Layer ⇄ Data
```
The arrows denote HTTP calls or direct Python imports, depending on whether the interaction crosses container boundaries (frontend ↔ backend) or stays in‑process (backend ↔ service/model agents).

---

*This AGENTS.md file provides a high‑level map of the system’s components, making it easier for new contributors to locate the code responsible for each functional area.*
