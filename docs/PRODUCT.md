# Product plan

## ICP and JTBD

**ICP:** robotics companies training manipulation systems for industrial and warehouse work, starting with a data-program lead responsible for one failing task. **Supplier:** authorized skilled workers and employers with repeatable work and clear site rights.

**JTBD:** “When a deployed task still fails outside the lab, help me commission representative demonstrations with known consent, coverage, and outcomes so I can run the next training cycle without building a field-operations team.”

## MVP

Buyer brief intake → task ontology and acceptance criteria → worker/site qualification → capture plan and consent → upload → privacy screening → human segmentation/labels → buyer acceptance and payout. The prototype implements the deterministic capture-plan operation, not recording, upload, model training, or payment.

## Data model

- `Buyer`, `Program`, `TaskSpec`, `AcceptanceRule`
- `Worker`, `Credential`, `Site`, `ConsentGrant`
- `CaptureSession`, `Recording`, `Segment`, `Annotation`, `QualityCheck`
- `LicenseGrant`, `Delivery`, `Payout`, `Dispute`

Every derivative retains lineage to source recording, participant/site consent, license scope, annotator, model-assisted transformations, and buyer acceptance.

## Technical architecture

Next.js buyer/contributor workflows; FastAPI domain service; PostgreSQL metadata and append-only audit events; S3-compatible encrypted object storage with per-tenant keys; background jobs for transcoding/redaction; signed upload/download URLs; OIDC/RBAC; policy engine for consent and retention. Pages serves this static demo only.

## AI/model strategy

Use commodity vision/audio models for candidate face/screen/address detection, shot-boundary detection, hand/tool/object proposals, and transcription. Humans approve safety-critical labels and redactions. Start model-agnostic and log model/version/confidence. The moat is not a foundation model; it is task-specific accepted data, edge-case coverage, and trusted rights lineage.

## Economics

Pilot price hypothesis: $2.5k–$7.5k for a narrow task. Target gross margin: 45%+ after worker/site payments, capture support, annotation, QA, and storage. The source’s $50–$200/hour range is a directional anchor, not validation. Instrument revenue per accepted minute, worker payout per recorded hour, acceptance rate, rework hours, acquisition cost, and time-to-delivery. Kill the wedge if two paid pilots cannot reach 30% contribution margin after manual operations.

## Validation and GTM

Founder-led outbound to robotics data and deployment leads. Lead with one concrete failure-prone task and a sample acceptance spec, not a marketplace pitch. Recruit supply only after a funded brief. Expand inside an account from one task to adjacent tasks at the same site, then reuse the qualified worker/site network for a second buyer.

## Moat

Trusted contributor/site relationships, task ontologies linked to buyer acceptance outcomes, edge-case coverage maps, consent/license provenance, and operational learning about what footage is rejected. A directory and generic labels are not defensible.

## Risks

Workplace safety; employer ownership; worker surveillance concerns; privacy and biometric laws; union rules; export controls; biased geography/task coverage; dataset poisoning; duplicate/low-quality footage; buyer-specific schemas; long enterprise procurement; robots changing faster than data delivery. Mitigate with buyer-funded scope, explicit site/worker consent, minimum collection, revocation/retention policy, human QA, and auditable lineage.

## Roadmap

- **0–30 days:** 10 buyer interviews, two observed workflows, one marked-up task spec, one paid pilot LOI; run capture manually.
- **31–60 days:** consent workflow, signed uploads, task schema, human QA console, delivery manifest; complete first pilot.
- **61–90 days:** second paid buyer, contributor qualification, acceptance analytics, redaction assistance, repeat-task pricing; decide whether to deepen one vertical.

## Success metrics

Paid pilots, accepted minutes / delivered minutes, first-pass acceptance, capture-to-delivery time, repeat briefs per buyer, worker effective hourly pay, contribution margin, privacy/safety incidents, and consent revocations.
