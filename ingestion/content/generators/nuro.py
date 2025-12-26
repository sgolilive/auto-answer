from ingestion.content.generators.BaseGenerator import BaseGenerator

class Neuroscience(BaseGenerator):

    def get_topic(self) -> str:
        return "Neuroscience and Psychology"

    def get_subtopics(self) -> list[str]:
        return [
            "brain anatomy and function", "cognition and perception", "memory processes",
            "behavioral neuroscience", "neuroplasticity", "emotional regulation",
            "neural networks (biological)", "psychometrics", "learning and conditioning", "psychopathology"
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
        "Cognitive biases can distort perception and decision-making outcomes in experiments.",
        "Memory processes involve encoding, storage, and retrieval mechanisms that are context-dependent.",
        "Behavioral neuroscience experiments often require careful stimulus control and observation.",
        "Neuroplasticity studies show how experience reshapes neural pathways over time.",
        "Emotional regulation involves interactions between multiple brain regions and neurotransmitters.",
        "Psychometric assessments must balance reliability, validity, and cultural considerations."
      ]

    question_intents = [
        "cognitive bias challenge", "memory retention problem", "behavioral assessment scenario",
        "neuroplasticity adaptation issue", "emotional regulation difficulty", "neural network modeling challenge",
        "learning strategy evaluation", "psychometric measurement reliability", "neurological disorder analysis", "experimental reproducibility issue"
    ]

    openers = [
        "In practical neuroscience studies,",
        "From a cognitive psychology perspective,",
        "During behavioral experiments,",
        "Historically,",
        "When analyzing memory and learning processes,",
        "In emotional and social cognition contexts,"
    ]

    bridges = [
        "this rarely behaves as expected without careful experimental design and control.",
        "issues often propagate through multiple cognitive and neural pathways.",
        "problems often surface only under specific environmental or task conditions.",
        "small variations in stimuli or measurement methods can drastically affect outcomes.",
        "what seems intuitive can yield unexpected results due to complex brain dynamics."
    ]

    closers = [
        "which is why meticulous planning, rigorous methodology, and repeated validation are essential.",
        "and this insight usually emerges from longitudinal studies and experimental replication.",
        "making it a recurring topic in neuroscience and psychology education.",
        "and there is rarely a single universally applicable explanation for complex behaviors.",
        "a lesson reinforced by real-world clinical, experimental, and observational data."
    ]
