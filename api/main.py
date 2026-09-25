from typing import Literal
from fastapi import FastAPI
from pydantic import BaseModel, Field, model_validator

app = FastAPI(title="WorkTrace capture planning API", version="0.1.0")

class Task(BaseModel):
    name: str = Field(min_length=3, max_length=120)
    minutes: int = Field(ge=5, le=240)
    steps: int = Field(ge=1, le=100)
    complexity: int = Field(ge=1, le=5)
    environment: Literal["shop floor", "plant room", "job site", "confined"]

class CaptureRequest(BaseModel):
    tasks: list[Task] = Field(min_length=1, max_length=12)
    capture_mode: Literal["smart-glasses", "tripod", "dual-view"]
    privacy_screening: bool = True
    worker_rate_per_hour: int = Field(ge=25, le=500)
    buyer_rate_per_hour: int = Field(ge=50, le=1000)
    @model_validator(mode="after")
    def unique_tasks(self):
        names = [task.name.casefold() for task in self.tasks]
        if len(names) != len(set(names)): raise ValueError("task names must be unique")
        if self.buyer_rate_per_hour <= self.worker_rate_per_hour: raise ValueError("buyer rate must exceed worker rate")
        return self

class CapturePlan(BaseModel):
    total_minutes: int
    estimated_clips: int
    worker_payout_usd: int
    buyer_value_usd: int
    readiness_score: int
    recommendation: str
    warnings: list[str]

def plan_capture(payload: CaptureRequest) -> CapturePlan:
    total = sum(task.minutes for task in payload.tasks); complexity = sum(task.complexity for task in payload.tasks)
    multiplier = {"smart-glasses": 1.0, "tripod": 0.82, "dual-view": 1.18}[payload.capture_mode]
    readiness = min(96, round(54 + len(payload.tasks)*8 + complexity*2 + (8 if payload.privacy_screening else 0) + (5 if payload.capture_mode == "smart-glasses" else 0)))
    warnings = []
    if not payload.privacy_screening: warnings.append("Privacy review is required before buyer delivery.")
    if any(task.environment == "confined" for task in payload.tasks): warnings.append("Confined-space footage requires a spotter and site approval.")
    return CapturePlan(total_minutes=total, estimated_clips=round(total/3.5), worker_payout_usd=round(total/60*payload.worker_rate_per_hour), buyer_value_usd=round(total/60*payload.buyer_rate_per_hour*multiplier), readiness_score=readiness, recommendation="Ready for a paid capture pilot" if readiness >= 82 else "Resolve capture gaps before matching", warnings=warnings)

@app.get("/health")
def health() -> dict[str, str]: return {"status":"ok"}

@app.post("/capture-plan", response_model=CapturePlan)
def capture_plan(payload: CaptureRequest) -> CapturePlan: return plan_capture(payload)
