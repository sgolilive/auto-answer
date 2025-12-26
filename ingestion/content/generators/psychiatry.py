from ingestion.content.generators.BaseGenerator import BaseGenerator

class Psychiatry(BaseGenerator):

    def get_topic(self) -> str:
        return "psychiatry and behavioral health"

    def get_subtopics(self) -> list[str]:
        return [
            "mood disorders", "anxiety and stress-related disorders", "psychotic disorders",
            "cognitive behavioral therapy techniques", "neurodevelopmental disorders", "substance use disorders",
            "psychopharmacology", "diagnostic assessment and screening", "behavioral interventions",
            "mental health policy and ethics"
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
        "Mood disorders require careful assessment of symptoms, triggers, and therapeutic interventions.",
        "Anxiety and stress-related disorders involve behavioral, cognitive, and pharmacological strategies.",
        "Psychotic disorders necessitate early detection, medication management, and psychosocial support.",
        "Cognitive behavioral therapy techniques are applied to modify thought patterns and behaviors.",
        "Substance use disorders demand integrated treatment plans addressing both psychological and physiological aspects.",
        "Neurodevelopmental disorders require multi-disciplinary evaluation, intervention, and family involvement."
      ]

    question_intents = [
        "treatment planning challenge", "diagnostic assessment problem", "therapy technique scenario",
        "medication management issue", "risk assessment and intervention planning", "behavioral modification challenge",
        "patient adherence problem", "clinical evaluation difficulty", "co-morbidity management scenario", "policy implementation issue"
    ]

    openers = [
        "In practical psychiatric exercises,",
        "From a behavioral health perspective,",
        "During therapy and clinical assessment sessions,",
        "Historically,",
        "When analyzing mental health interventions,",
        "In cognitive and behavioral treatment contexts,"
    ]

    bridges = [
        "this rarely behaves as expected without comprehensive evaluation and individualized planning.",
        "issues often propagate through comorbid conditions, social factors, and patient variability.",
        "problems often surface only under complex clinical scenarios or environmental stressors.",
        "small changes in therapeutic approach or medication can drastically affect outcomes.",
        "what seems effective theoretically can fail under real-world patient variability."
    ]

    closers = [
        "which is why rigorous assessment, tailored therapy, and continuous monitoring are essential.",
        "and this insight usually emerges from clinical observation, patient interviews, and validated screening tools.",
        "making it a recurring topic in psychiatry and behavioral health education.",
        "and there is rarely a single universally effective treatment approach.",
        "a lesson reinforced by longitudinal studies, clinical trials, and evidence-based practice."
    ]
