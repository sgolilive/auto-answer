import time
from datetime import datetime, timezone
from typing import Callable, TypeVar

from ingestion.components.base_state import BaseState
from ingestion.entities.step_time import StepTime
from logger import get_logger

S = TypeVar("S", bound=BaseState)

class Pipeline:

    def __init__(self):
        self.logger = get_logger(__name__)

    def run(self, state: S, steps: list[Callable[[S], S]]) -> S:

        for step in steps:
            step_name = getattr(step, "__name__", step.__class__.__name__)
            self.logger.info(f"starting step: {step_name}")

            state.steps_ran[step_name] = StepTime(
                start=datetime.now(tz=timezone.utc)
            )

            start_perf = time.perf_counter()

            try:
                state = step(state)
            except Exception as e:
                self.logger.exception(f"step failed: {step_name}")
                state.errors.append(str(e))
                break

            end_perf = time.perf_counter()

            step_time = state.steps_ran[step_name]
            step_time.end = datetime.now(tz=timezone.utc)
            step_time.duration_ms = (end_perf - start_perf) * 1000

            self.logger.info(f"completed step: {step_name}")

            if state.errors:
                break

        return state
