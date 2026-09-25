# WorkTrace

WorkTrace is a runnable prototype for scoping skilled-trade video capture as robotics training data. A worker selects concrete tasks and capture conditions; the app produces a deterministic pilot brief with payout, buyer value, readiness, warnings, and a three-step operating plan.

All people, tasks, demand labels, rates, and results in the demo are fictional. The frontend simulates the domain operation locally so GitHub Pages can host it. The matching Python operation is runnable and tested source; it is **not deployed**.

## Run

```bash
npm ci
npm run dev
```

Open `http://localhost:3000`. The workflow supports task selection, capture-mode selection, privacy controls, validation, loading/result states, reset, and clipboard export.

## Verify

```bash
npm run typecheck
npm run test:e2e
npm run audit:prod
npm run build
cd api && uv sync --frozen && uv run pytest
```

Run the API with `cd api && uv run uvicorn main:app --reload`. POST `/capture-plan` to execute the validated domain operation.

## Structure

- `app/` — Next.js App Router UI
- `api/` — FastAPI capture-plan operation and integration tests
- `data/demo.json` — shared explicit fictional fixture
- `tests/` — Playwright interaction and mobile-overflow coverage
- `docs/` — product, architecture, review, and build prompts
- `research/notes.md` — summarized source research

Source inspiration: [Ideabrowser public idea](https://www.ideabrowser.com/hub/ideas/tradesperson-video-marketplace-for-robotics-companies).
