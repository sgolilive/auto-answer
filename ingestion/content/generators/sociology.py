from ingestion.content.generators.BaseGenerator import BaseGenerator

class Sociology(BaseGenerator):

    def get_topic(self) -> str:
        return "sociology and psychology"

    def get_subtopics(self) -> list[str]:
        return [
            "social behavior and norms", "cultural studies", "cognitive psychology", "behavioral psychology",
            "developmental psychology", "organizational behavior", "social research methods", "group dynamics",
            "personality theories", "mental health and therapy"
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
        "Social behavior and norms require understanding cultural, societal, and situational influences.",
        "Cognitive psychology involves perception, memory, learning, and decision-making processes.",
        "Behavioral psychology studies reinforcement, motivation, and habit formation.",
        "Developmental psychology examines changes across the lifespan and environmental interactions.",
        "Organizational behavior investigates teamwork, leadership, and decision-making dynamics.",
        "Mental health and therapy involve diagnosis, treatment planning, and patient-centered approaches."
      ]

    question_intents = [
        "behavior analysis challenge", "cultural interpretation problem", "cognitive modeling scenario",
        "psychological assessment issue", "developmental evaluation problem", "organizational problem-solving",
        "research methodology question", "group interaction analysis", "personality evaluation challenge", "therapy planning scenario"
    ]

    openers = [
        "In practical sociology and psychology exercises,",
        "From a behavioral science perspective,",
        "During research and observational sessions,",
        "Historically,",
        "When analyzing individual and group behavior,",
        "In cognitive and developmental contexts,"
    ]

    bridges = [
        "this rarely behaves as expected without careful observation and interpretation.",
        "issues often propagate through cultural, social, and individual variables.",
        "problems often surface only under stress, complexity, or conflicting motivations.",
        "small differences in perception or context can drastically affect outcomes.",
        "what seems obvious behaviorally can fail under nuanced social or psychological conditions."
    ]

    closers = [
        "which is why careful study, analysis, and evidence-based interpretation are essential.",
        "and this insight usually emerges from research studies, experiments, and longitudinal observation.",
        "making it a recurring topic in sociology and psychology education.",
        "and there is rarely a single universally applicable behavioral explanation.",
        "a lesson reinforced by cross-cultural studies, therapy outcomes, and organizational research."
    ]
