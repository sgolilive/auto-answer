from ingestion.content.generators.BaseGenerator import BaseGenerator

class HealthCare(BaseGenerator):

    def get_topic(self) -> str:
        return "healthcare and medical sciences"

    def get_subtopics(self) -> list[str]:
        return [
            "human anatomy and physiology", "pathophysiology", "pharmacology", "clinical diagnostics",
            "epidemiology", "medical imaging", "genetics and genomics", "public health",
            "therapeutics and treatment strategies", "healthcare systems and management"
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
        "diagnostic challenge", "treatment planning problem", "disease progression scenario",
        "therapeutic intervention assessment", "epidemiological modeling issue", "genetic interpretation problem",
        "pharmacological optimization challenge", "clinical decision-making difficulty", "healthcare management scenario", "public health policy evaluation"
    ]

    openers = [
        "In practical medical and healthcare exercises,",
        "From a clinical perspective,",
        "During patient management and diagnostic sessions,",
        "Historically,",
        "When analyzing disease mechanisms and treatments,",
        "In public health and healthcare systems contexts,"
    ]

    bridges = [
        "this rarely behaves as expected without comprehensive assessment and monitoring.",
        "issues often propagate through multiple organ systems, clinical variables, and patient conditions.",
        "problems often surface only under comorbidities or atypical presentations.",
        "small variations in treatment or diagnosis can drastically affect outcomes.",
        "what seems theoretically effective can fail under real-world healthcare constraints."
    ]

    closers = [
        "which is why careful diagnosis, evidence-based interventions, and continuous monitoring are essential.",
        "and this insight usually emerges from clinical trials, case studies, and epidemiological data.",
        "making it a recurring topic in medical education and healthcare research.",
        "and there is rarely a single universally optimal treatment or management approach.",
        "a lesson reinforced by patient outcomes, research evidence, and system-level evaluations."
    ]

    middle_sentences = [
        "Human anatomy and physiology understanding is crucial for accurate diagnosis and intervention.",
        "Pathophysiology involves interpreting disease mechanisms and clinical manifestations.",
        "Pharmacology requires careful dosing, drug interactions, and therapeutic monitoring.",
        "Clinical diagnostics depend on test accuracy, timing, and patient variability.",
        "Epidemiology studies disease patterns, risk factors, and prevention strategies.",
        "Genetics and genomics inform personalized medicine and treatment approaches."
      ]
