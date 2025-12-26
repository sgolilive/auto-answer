from ingestion.content.generators.BaseGenerator import BaseGenerator

class AIML(BaseGenerator):

    def get_subtopics(self) -> list[str]:
        return [
            "artificial intelligence", "machine learning", "supervised learning",
            "unsupervised learning", "reinforcement learning", "classification",
            "regression", "clustering", "overfitting", "underfitting",
            "bias-variance tradeoff", "feature engineering", "model evaluation"
            ]

    def get_sentence_pool(self) -> list[str]:
        pass

    def get_intro_options(self, subtopic: str) -> list[str]:
        pass

    def generate_question(self, subtopic: str) -> str:
        return super().generate_question(subtopic)

    def generate_answer(self, subtopic: str) -> str:
        return super().generate_answer(subtopic)

    def get_topic(self) -> str:
        return "AI & ML"

    question_intents = [
        "model failure analysis",
        "trade-off evaluation",
        "performance optimization",
        "bias and variance reasoning",
        "real-world deployment debugging",
        "feature impact assessment",
        "historical evolution of methods",
        "misconception clarification",
        "hyperparameter tuning scenario",
        "interpretability challenge"
    ]

    openers = [
        "In real-world ML deployments,",
        "From an AI engineering perspective,",
        "When training models on large datasets,",
        "During production incidents,",
        "Historically,",
        "In research-to-production transitions,"
    ]

    bridges = [
        "this rarely occurs in isolation.",
        "the implications often propagate across pipelines.",
        "teams often notice it only after deployment at scale.",
        "small preprocessing choices can amplify model errors.",
        "what seems trivial in lab settings can fail in production."
    ]

    closers = [
        "which is why practitioners continually refine model pipelines.",
        "and this insight usually comes from operational experience.",
        "making it a recurring topic in postmortem analyses.",
        "and there is rarely a single universally correct approach.",
        "a lesson reinforced by repeated deployment incidents."
    ]

    middle_sentences = [
        "Lab performance can be misleading; real data distributions often differ.",
        "Minor feature engineering choices can significantly impact results.",
        "Overfitting and underfitting trade-offs are rarely straightforward.",
        "Bias-variance considerations frequently reveal hidden constraints.",
        "Hyperparameter choices can amplify unintended model behavior.",
        "Monitoring predictions usually uncovers subtle failure modes."
    ]