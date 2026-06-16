# Agent Working Notes – Document Translation Benchmark Platform

## Quick Start

- **Run backend:** `cd src && uvicorn api.main:app --host 0.0.0.0 --port 8000`
- **Run frontend:** `streamlit run frontend/app.py`
- **Run with Docker:** `docker compose up`
- **Entrypoint for local dev:** Root `main.py` removed. Real app is in `src/api/main.py`.

## Environment & Tooling

- **Python:** 3.13+ (enforced in `pyproject.toml`).
- **Dependency manager:** `uv` (lockfile is `uv.lock`; do **not** commit `uv.lock` changes unless you deliberately updated deps).
- **Virtual env:** `.venv/`.  Do not commit `.venv/` or `.env`.

## Monorepo Layout & Ownership

| Directory | What lives here |
|-----------|-----------------|
| `src/api/` | FastAPI app (`main.py`), Pydantic schemas (`schemas.py`), empty `routers/` directory for future use. |
| `frontend/` | Streamlit app (`app.py`). Hardcodes `BACKEND_URL = "http://localhost:8000"`. |
| `notebooks/` | Jupyter notebook (`Translate.ipynb`) for training and experimentation. |
| `src/services/pdf_translator/` | `TranslationService` class. `extractor.py` is **missing** and needs creation. |
| `src/models/` | Owns **all** model code. `src/models/__init__.py` is currently empty. |
| `src/models/lstm/` | Seq2Seq LSTM encoder/decoder (`model.py`), training (`train.py`), evaluation (`evaluate.py`). |
| `src/models/transformer/` | Transformer model (`model.py`, `multihead_attention.py`), training notebook (`01_transformer_training.ipynb`). `TransformerModel.forward` is unimplemented. |
| `src/benchmark/` | Metrics tracker, BLEU/ROUGE/METEOR evaluators, matplotlib visualizers. |
| `src/__init__.py` | Empty, intentionally kept. |
| `data/` | Data directory (raw/processed/vocab ignored by `.gitignore`). |
| `tests/` | Empty. |

## Architecture & Wiring

```
Frontend (Streamlit)
         |
         | HTTP
         v
Backend (FastAPI) ──> TranslationService (PDF in/out)
         |                      |
         |                      v
         |              {LSTM Seq2Seq | Transformer}
         |
         └── GET /benchmark (stubbed; returns hardcoded scores)
```

- Backend CORS is **wildcarded** (`allow_origins=["*"]`); okay for local dev, not for production.
- `src/api/main.py` instantiates `TranslationService()` and calls `load_models()` at import time; any import errors in model code will crash the server on startup.

## Key Gotchas

1. **`extractor.py` is missing:** `src/services/pdf_translator/__init__.py` imports `PDFExtractor` from `.extractor`, but the file is not in the repo. Any import of `TranslationService` will fail until this file is created.
2. **Canonical dependencies are in `pyproject.toml`:** `backend/requirements.txt` was removed. Use `pyproject.toml` and `uv` for package management.
3. **`docker-compose.yml`** is now updated to use Python images for both backend and frontend services.
4. **`Dockerfile`** updated to install deps from `pyproject.toml` and runs `uvicorn api.main:app`. It does **not** serve the Streamlit frontend.
5. **Stub state:** No model checkpoints exist yet. `get_model()` is unimplemented, `TransformerModel.forward()` is `pass`. `TranslationService.translate_text()` currently returns placeholder strings like `[LSTM Translation] {text}`.
6. **No more `main.py` at root:** Removed to avoid confusion. Real entrypoint is `src/api/main.py`.
7. **`.gitignore` ignores checkpoints and data directories:** If you generate model checkpoints or processed data, they will not show up in `git status`.

## Testing

- There are no tests yet (`tests/` is empty). If you add tests, use `pytest` or `unittest`.
- No existing test commands, CI, or pre-commit hooks.

## Style & Conventions

- Follow PEP 8 for Python code.
- Keep `pyproject.toml` as the source of truth for dependencies.
- Run backend from `src/` directory: `cd src && uvicorn api.main:app --host 0.0.0.0 --port 8000`

## Verification

- After starting the backend, verify with: `curl http://localhost:8000/models`
- The placeholder `/benchmark` and `/translate` endpoints will return hardcoded or stubbed data.