import uuid
from dataclasses import field, dataclass
from typing import Any, Dict, Optional, TypeVar
from ingestion.entities.step_time import StepTime

@dataclass
class BaseState:
    steps_ran: Dict[str, StepTime] = field(default_factory=dict[str, StepTime])
    errors: list = field(default_factory=list)
    id: uuid.UUID = field(default_factory=uuid.uuid4)
