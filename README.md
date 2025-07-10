# Course Recommendation API

This is a FastAPI backend for course recommendation using your specialization relevancy matrix CSV.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the API server:
   ```bash
   uvicorn main:app --reload
   ```

3. Endpoints:
   - `/specializations` — Get all past specializations (rows)
   - `/targets` — Get all target programs (columns)
   - `/recommend?from_spec=...&to_spec=...` — Get recommendation, score, and alternatives

The API loads the matrix from `../study-abroad-app/corrected_specialization_matrix (1).csv`. 