# Architecture

The static Next.js app imports `data/demo.json` and computes the same deterministic plan as `api/main.py`, enabling a real interactive Pages demo without pretending the backend is live. FastAPI owns the canonical validated operation for local or future hosted use.

`CaptureRequest → validation → plan_capture → CapturePlan`

Validation covers bounded tasks, supported environments and capture modes, unique names, and a buyer rate above worker rate. The operation calculates duration, estimated clips, worker payout, buyer value, readiness, and safety/privacy warnings.

Production separation: browser → API gateway → application service → PostgreSQL; direct signed media upload → encrypted object storage; queue → redaction/transcode/annotation workers → human QA → immutable delivery manifest. Emit structured events for brief created, consent granted, upload complete, redaction flagged, QA rejected, delivery accepted, payout released, and access denied. Trace every delivery back to recording, consent and transformation versions.

Failure modes: resumable uploads, idempotency keys, checksum verification, quarantine for malware/corruption, dead-letter queues, manual-review thresholds, and fail-closed delivery when rights or privacy status is incomplete.
