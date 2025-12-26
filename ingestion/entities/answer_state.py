from dataclasses import dataclass, field
from typing import Any

from ingestion.entities.answer_deps import AnswerDeps
from ingestion.components.base_state import BaseState

@dataclass
class SimilarQuestionDeps(AnswerDeps):
    pass

@dataclass
class SimilarQuestionState(BaseState):
    deps: SimilarQuestionDeps = field(default_factory=SimilarQuestionDeps)

    question: str = None
    embeddings: Any = None
    qa_docs: list[Any] = None
    qid_scores: list[Any] = None


@dataclass
class AnswerState(BaseState):

    question: str = None

    embeddings: Any = None
    q_docs:list[Any] = None
    deduped_chunks: list[Any] = None
    context: str = None
    prompt: str = None
    answer: str = None

    deps: AnswerDeps = field(default_factory=AnswerDeps)