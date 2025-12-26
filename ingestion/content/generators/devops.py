from ingestion.content.generators.BaseGenerator import BaseGenerator

class CloudDevOps(BaseGenerator):

    def get_topic(self) -> str:
        return "cloud and devops"

    def get_subtopics(self) -> list[str]:
        return [
            "virtualization", "containers", "Docker", "Kubernetes",
            "CI/CD pipelines", "infrastructure as code", "load balancing",
            "auto scaling", "monitoring", "logging", "high availability",
            "disaster recovery"
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
        "production failure analysis",
        "architecture trade-off evaluation",
        "security incident reasoning",
        "performance optimization perspective",
        "scalability concern discussion",
        "developer experience comparison",
        "historical evolution explanation",
        "misconception clarification",
        "real-world debugging scenario",
        "system design implication"
    ]

    openers = [
        "In real production environments,",
        "From an engineering standpoint,",
        "Historically,",
        "When scaling systems,",
        "During operational incidents,",
        "In large cloud deployments,"
    ]

    bridges = [
        "this is rarely an isolated concern.",
        "the implications usually surface indirectly.",
        "teams often encounter this only after deployment.",
        "complex interactions tend to magnify its effects.",
        "what looks trivial in theory often fails in practice.",
    ]

    closers = [
        "which is why teams often revisit their design over time.",
        "and this insight typically comes from operational experience.",
        "making it a recurring topic in postmortems and reviews.",
        "and this trade-off rarely has a universally correct answer.",
        "a lesson reinforced by repeated production incidents."
    ]

    middle_sentences = [
        "Theoretical understanding helps initially, but real usage exposes hidden assumptions.",
        "Small design decisions can amplify into significant operational constraints.",
        "What looks clean in isolation can become fragile once multiple systems interact.",
        "Debugging usually reveals that the root cause is spread across layers.",
        "Performance and security concerns tend to surface simultaneously.",
        "Teams frequently realize the cost of earlier shortcuts at this stage."
      ]