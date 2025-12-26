from ingestion.content.generators.BaseGenerator import BaseGenerator

class HCI(BaseGenerator):

    def get_topic(self) -> str:
        return "HCI and UX design"

    def get_subtopics(self) -> list[str]:
        return [
            "user interface design", "interaction patterns", "usability testing", "information architecture",
            "accessibility", "visual design principles", "cognitive load optimization", "user research methods",
            "prototyping", "responsive and adaptive design"
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
        "navigation complexity challenge", "accessibility compliance issue", "cognitive overload scenario",
        "interface consistency problem", "usability testing anomaly", "responsive design adjustment",
        "interaction feedback latency", "user behavior prediction challenge", "prototyping iteration issue", "visual hierarchy optimization"
    ]

    openers = [
        "In practical UX design projects,",
        "From a human-computer interaction perspective,",
        "During usability testing sessions,",
        "Historically,",
        "When designing responsive and adaptive interfaces,",
        "In accessibility-focused design contexts,"
    ]

    bridges = [
        "this rarely behaves as expected without careful attention to user behavior.",
        "issues often propagate across navigation, interaction, and visual design components.",
        "problems often surface only under diverse user demographics and device contexts.",
        "small inconsistencies can significantly affect user satisfaction and task efficiency.",
        "what seems intuitive to designers can confuse real users."
    ]

    closers = [
        "which is why iterative testing and user-centered design practices are essential.",
        "and this insight usually emerges from repeated prototyping and field studies.",
        "making it a recurring topic in HCI and UX design research.",
        "and there is rarely a single universally correct interface design.",
        "a lesson reinforced by real-world user feedback and analytics."
    ]

    middle_sentences = [
        "Navigation complexity can hinder users from efficiently accessing content and features.",
        "Accessibility considerations must account for visual, auditory, and motor impairments.",
        "Cognitive load optimization ensures users can perform tasks without unnecessary strain.",
        "Interface consistency across screens improves learnability and reduces errors.",
        "Prototyping iterations help uncover usability issues before full-scale deployment.",
        "Visual hierarchy and interaction feedback are key to guiding user attention effectively."
      ]