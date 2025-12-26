from ingestion.content.generators.BaseGenerator import BaseGenerator

class Science(BaseGenerator):

    def get_topic(self) -> str:
        return "Science"

    def get_subtopics(self) -> list[str]:
        return [
            "force", "work", "energy", "power", "gravity", "motion",
            "thermodynamics", "atom", "molecule", "chemical reaction",
            "photosynthesis", "respiration", "cell structure", "DNA", "evolution"
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
        "Measurement errors can propagate and affect conclusions.",
        "Interactions between components often produce unexpected behaviors.",
        "Theoretical models may not fully capture real-world conditions.",
        "Experimental setups sometimes fail to isolate relevant variables.",
        "Observed patterns may differ from predicted ones due to hidden factors.",
        "Historical studies often highlight edge cases that challenge assumptions."
      ]

    question_intents = [
        "experimental observation analysis",
        "conceptual understanding challenge",
        "real-world application reasoning",
        "cause-effect relationship evaluation",
        "measurement error scenario",
        "system interaction analysis",
        "historical discovery implications",
        "hypothetical experiment design",
        "theoretical model limitation",
        "unexpected result investigation"
    ]

    openers = [
        "In real-world scientific observations,",
        "From a theoretical perspective,",
        "During experimental studies,",
        "Historically,",
        "In applied science contexts,",
        "When analyzing complex systems,"
    ]

    bridges = [
        "this rarely behaves as expected without careful consideration.",
        "effects often propagate through interconnected systems.",
        "unexpected results often surface only after repeated measurements.",
        "small errors can amplify and affect the entire system.",
        "what seems straightforward in theory can be complex in practice."
    ]

    closers = [
        "which is why scientists rigorously test hypotheses and models.",
        "and this insight usually comes from repeated experimentation.",
        "making it a recurring topic in research studies.",
        "and there is rarely a universally simple explanation.",
        "a lesson reinforced by extensive observation and analysis."
    ]