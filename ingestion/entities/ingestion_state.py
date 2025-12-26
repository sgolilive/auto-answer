from dataclasses import dataclass, field

from ingestion.components.base_state import BaseState
from ingestion.content.generators.BaseGenerator import BaseGenerator
from ingestion.entities.step_time import StepTime
from ingestion.entities.ingestion_deps import IngestionDeps
from typing import Any, Dict, Iterator

@dataclass
class IngestionState(BaseState):

    start_id: int = 0
    end_id: int = 0

    deps: IngestionDeps = field(default_factory=IngestionDeps)

    generator: BaseGenerator = field(default_factory=BaseGenerator)

    qas: Iterator[Dict[str, Any]] = None
    chunks: Iterator[Dict[str, Any]] = None
    dedupe_chunks: Iterator[Dict[str, Any]] = None

    steps_ran: Dict[str, StepTime] = field(default_factory=dict[str, StepTime])

    errors: list = field(default_factory=list)