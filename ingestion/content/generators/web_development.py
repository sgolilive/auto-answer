from ingestion.content.generators.BaseGenerator import BaseGenerator

class WebDevelopment(BaseGenerator):

    def get_topic(self) -> str:
        return "web development"

    def get_subtopics(self) -> list[str]:
        return [
            "HTTP protocol", "REST APIs", "GraphQL", "client-server architecture",
            "cookies", "sessions", "authentication", "authorization", "CORS",
            "web security", "HTML", "CSS", "JavaScript",
            "single page applications", "server-side rendering"
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
        "Theoretical understanding helps initially, but real usage exposes hidden assumptions.",
        "Small design decisions can amplify into significant operational constraints.",
        "What looks clean in isolation can become fragile once multiple systems interact.",
        "Debugging usually reveals that the root cause is spread across layers.",
        "Performance and security concerns tend to surface simultaneously.",
        "Teams frequently realize the cost of earlier shortcuts at this stage."
      ]

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
        "In real production web systems,",
        "When web applications move beyond prototypes,",
        "From a system design perspective,",
        "In many mature web platforms,",
        "From the viewpoint of long-term maintainability,",
        "In high-traffic environments,",
        "Historically, web development practices have shown that",
        "In day-to-day frontend and backend collaboration,"
    ]

    bridges = [
        "this is rarely an isolated concern.",
        "the implications often surface indirectly.",
        "teams usually encounter this only after deployment.",
        "the behavior becomes visible under real user load.",
        "this tends to interact with multiple layers of the stack.",
        "the complexity is often underestimated initially."
    ]

    closers = [
        "which is why teams often refine their approach over time.",
        "and this realization usually comes from operational experience.",
        "making it a recurring topic in post-incident reviews.",
        "which explains why best practices keep evolving.",
        "and this trade-off has no universally correct answer.",
        "a lesson reinforced by repeated production issues."
    ]
