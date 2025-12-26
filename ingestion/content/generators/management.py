from ingestion.content.generators.BaseGenerator import BaseGenerator

class Management(BaseGenerator):

    def get_topic(self) -> str:
        return "Management"

    def get_subtopics(self) -> list[str]:
        return [
            "leadership", "teamwork", "time management", "decision making",
            "conflict resolution", "communication skills", "goal setting",
            "performance management", "risk management"
        ]

    def get_sentence_pool(self) -> list[str]:
        pass

    def get_intro_options(self, subtopic: str) -> list[str]:
        pass

    def generate_question(self, subtopic: str) -> str:
        return super().generate_question(subtopic)

    def generate_answer(self, subtopic: str) -> str:
        return super().generate_answer(subtopic)

    question_intents = [
        "complex project scenario analysis",
        "team conflict challenge",
        "time allocation and prioritization",
        "strategic decision-making edge case",
        "risk assessment in uncertain conditions",
        "performance evaluation difficulty",
        "goal alignment scenario",
        "communication breakdown analysis",
        "leadership effectiveness evaluation",
        "cross-functional coordination problem"
    ]

    openers = [
        "In real-world management scenarios,",
        "From a leadership perspective,",
        "During team operations,",
        "Historically,",
        "When overseeing projects,",
        "In complex organizational contexts,"
    ]

    bridges = [
        "this rarely unfolds as expected without careful planning.",
        "implications often cascade across multiple teams.",
        "issues often surface only after project execution begins.",
        "small miscommunications can escalate into larger conflicts.",
        "what seems straightforward can have hidden organizational subtleties."
    ]

    closers = [
        "which is why managers continually refine strategies and communication.",
        "and this insight usually emerges from repeated leadership experience.",
        "making it a recurring topic in organizational studies.",
        "and there is rarely a single universally correct approach.",
        "a lesson reinforced by repeated team management scenarios."
    ]

    middle_sentences = [
        "Conflict resolution requires balancing competing interests and perspectives.",
        "Time management challenges often arise due to overlapping priorities.",
        "Strategic decision-making must account for uncertainty and incomplete information.",
        "Performance management can uncover unexpected skill gaps or bottlenecks.",
        "Effective communication is critical to ensure alignment across teams.",
        "Leadership effectiveness is often context-dependent and varies by situation."
      ]
