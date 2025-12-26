from ingestion.content.generators.BaseGenerator import BaseGenerator

class Ethics(BaseGenerator):

    def get_topic(self) -> str:
        return "Ethics and AI Governance"

    def get_subtopics(self) -> list[str]:
        return [
            "bias and fairness", "explainability", "privacy compliance", "responsible AI deployment",
            "algorithmic accountability", "auditability", "transparency", "ethical risk assessment",
            "regulatory compliance", "human-in-the-loop decision making"
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
        "bias detection scenario", "explainability challenge", "privacy violation risk",
        "AI system audit requirement", "decision accountability issue", "transparency gap analysis",
        "ethical risk evaluation", "regulatory compliance enforcement", "human oversight failure",
        "model interpretability problem"
    ]

    openers = [
        "In practical AI governance scenarios,",
        "From an ethical AI perspective,",
        "During system audit exercises,",
        "Historically,",
        "When deploying AI responsibly,",
        "In human-centric AI decision contexts,"
    ]

    bridges = [
        "this rarely behaves as expected without careful oversight.",
        "issues often propagate across datasets, models, and stakeholders.",
        "problems often surface only when AI is deployed at scale.",
        "small biases can result in significant ethical or legal consequences.",
        "what seems fair in simulation can fail in real-world deployment."
    ]

    closers = [
        "which is why continuous auditing and transparency are essential.",
        "and this insight usually emerges from repeated governance reviews.",
        "making it a recurring topic in AI ethics studies.",
        "and there is rarely a single universally correct governance approach.",
        "a lesson reinforced by real-world AI deployment challenges."
    ]

    middle_sentences = [
        "Bias in training data can propagate into unfair AI predictions if not properly mitigated.",
        "Explainability challenges may prevent stakeholders from trusting AI decisions.",
        "Privacy compliance violations can result from improper data handling or model outputs.",
        "Human-in-the-loop oversight is critical for high-stakes automated decision-making.",
        "Audit logs and model documentation support accountability and traceability.",
        "Transparency gaps can erode public trust and invite regulatory scrutiny."
      ]