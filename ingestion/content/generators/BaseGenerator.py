import random
from abc import ABC, abstractmethod
from typing import Any, Iterator, Dict


class BaseGenerator(ABC):

    random.seed(42)

    question_templates: dict[str, list[str]]

    question_intents: list[str]

    openers: list[str]

    middle_sentences: list[str]

    bridges: list[str]

    closers: list[str]

    def question_id(self, qid) -> str:
        return f'Q{qid:07d}'

    def get_question_templates(self, subtopic: str) -> list[str]:
        return self.question_templates[subtopic]

    @abstractmethod
    def get_topic(self) -> str:
        pass

    @abstractmethod
    def get_subtopics(self) -> list[str]:
        pass

    @abstractmethod
    def get_sentence_pool(self) -> list[str]:
        pass

    @abstractmethod
    def get_intro_options(self, subtopic: str) -> list[str]:
        pass

    @abstractmethod
    def generate_question(self, subtopic: str) -> str:
        topic = random.choice(subtopic)
        intent = random.choice(self.question_intents)
        templates = [
            f"Why does {topic} present challenges in {intent}?",
            f"How should physicists approach {topic} in scenarios involving {intent}?",
            f"What are common pitfalls of {topic} during {intent}?",
            f"In practical physics exercises, how does {topic} affect {intent} outcomes?",
            f"What lessons can be learned from {topic} when dealing with {intent}?"
        ]
        return random.choice(templates)

    @abstractmethod
    def generate_answer(self, subtopic: str) -> str:
        para_count = random.choices([1,2,3,4], weights=[0.15,0.4,0.35,0.1])[0]
        paragraphs = []

        for _ in range(para_count):
            sentence_count = random.randint(2,6)
            sentences = [
                random.choice(self.openers) + f" {subtopic} often reveals hidden complexities in system behavior and measurement."]

            for _ in range(sentence_count - 2):
                middle_sentence = random.choice(self.middle_sentences) + " " + random.choice(self.bridges)
                sentences.append(middle_sentence)

            sentences.append(random.choice(self.closers))
            paragraphs.append(" ".join(sentences))

        return "\n\n".join(paragraphs)

    def get_qas(self, start: int, end: int) -> Iterator[Dict[str, Any]]:

        for qid in range(start, end):
            sub = random.choice(self.get_subtopics())

            yield {
                'qid': self.question_id(qid),
                'answer': self.generate_answer(sub),
                'subtopic': sub,
                'topic': self.get_topic(),
                'question': self.generate_question(sub)
            }