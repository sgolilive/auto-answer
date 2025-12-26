from ingestion.content.generators.BaseGenerator import BaseGenerator

class Philosophy(BaseGenerator):

    def get_topic(self) -> str:
        return "philosophy and ethics"

    def get_subtopics(self) -> list[str]:
        return [
            "moral philosophy", "applied ethics", "epistemology", "metaphysics",
            "political philosophy", "virtue ethics", "deontology", "utilitarianism",
            "existentialism", "ethical dilemmas in technology"
        ]

    def get_sentence_pool(self) -> list[str]:
        pass

    def get_intro_options(self, subtopic: str) -> list[str]:
        pass

    def generate_question(self, subtopic: str) -> str:
        return super().generate_question(subtopic)

    def generate_answer(self, subtopic: str) -> str:
        return super().generate_answer(subtopic)

    middle_sentences = [
        "Moral philosophy examines what is right and wrong, often under conflicting frameworks.",
        "Applied ethics requires balancing principles with practical consequences in real-world scenarios.",
        "Epistemology explores the nature and limits of knowledge and belief.",
        "Metaphysical inquiries challenge assumptions about reality, existence, and causality.",
        "Political philosophy examines governance, justice, and societal obligations.",
        "Virtue ethics, deontology, and utilitarianism offer differing perspectives on moral action."
      ]

    question_intents = [
        "moral reasoning challenge", "ethical dilemma problem", "philosophical debate scenario",
        "decision-making complexity", "normative principle evaluation", "applied ethical judgment",
        "conceptual analysis problem", "argument critique difficulty", "existential question analysis", "technology ethics issue"
    ]

    openers = [
        "In practical philosophical inquiry,",
        "From an ethics perspective,",
        "During applied ethical reasoning exercises,",
        "Historically,",
        "When analyzing moral and philosophical problems,",
        "In debates on technology and ethics contexts,"
    ]

    bridges = [
        "this rarely yields a straightforward answer without considering multiple perspectives and arguments.",
        "issues often propagate through competing philosophical frameworks and interpretations.",
        "problems often surface only when principles conflict or assumptions are challenged.",
        "small nuances in reasoning can drastically change moral or logical outcomes.",
        "what seems intuitively correct can fail under rigorous philosophical scrutiny."
    ]

    closers = [
        "which is why careful argumentation, critical thinking, and reflection are essential.",
        "and this insight usually emerges from comparative analysis of theories and case studies.",
        "making it a recurring topic in philosophy and ethics education.",
        "and there is rarely a single universally correct solution to complex ethical dilemmas.",
        "a lesson reinforced by historical debates and contemporary ethical challenges."
    ]
