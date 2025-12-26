from dataclasses import dataclass
from datetime import datetime, timezone

@dataclass
class StepTime:
    start: datetime
    end: datetime | None = None
    duration_ms: float | None = None