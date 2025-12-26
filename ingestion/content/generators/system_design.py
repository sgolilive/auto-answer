from ingestion.content.generators.BaseGenerator import BaseGenerator

class SystemDesign(BaseGenerator):

    def get_topic(self) -> str:
        return "system design"

    def get_subtopics(self) -> list[str]:
        return [
            "scalability", "latency", "throughput", "horizontal scaling", "vertical scaling",
            "caching", "rate limiting", "message queues", "event-driven architecture",
            "microservices", "monolithic architecture", "API gateway", "service discovery"
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
        "Theoretical models help initially, but real traffic exposes hidden bottlenecks.",
        "Small design shortcuts can cascade into major production issues.",
        "Service dependencies often amplify latency unexpectedly.",
        "Caching decisions can impact throughput and consistency in subtle ways.",
        "Rate limiting can reveal flaws in horizontal scaling strategies.",
        "Monitoring usually uncovers operational edge cases that were overlooked."
      ]

    question_intents = [
        "production failure analysis",
        "architecture trade-off evaluation",
        "performance optimization perspective",
        "scalability concern discussion",
        "real-world debugging scenario",
        "design decision reasoning",
        "historical evolution explanation",
        "misconception clarification",
        "system bottleneck analysis",
        "integration and dependency scenario"
    ]

    openers = [
        "In large-scale systems,",
        "When traffic grows beyond expected limits,",
        "From an architectural perspective,",
        "During production incidents,",
        "Historically,",
        "In multi-service deployments,"
    ]

    bridges = [
        "this rarely happens in isolation.",
        "the implications often ripple across components.",
        "teams often notice it only under real load.",
        "small design choices can amplify system complexity.",
        "what seems trivial in theory can fail in practice."
    ]

    closers = [
        "which is why engineers revisit their architecture decisions regularly.",
        "and this insight is typically gained through real-world experience.",
        "making it a recurring discussion in postmortems and design reviews.",
        "and there is rarely a one-size-fits-all solution.",
        "a lesson reinforced by repeated production incidents."
    ]
