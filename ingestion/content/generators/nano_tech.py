from ingestion.content.generators.BaseGenerator import BaseGenerator

class Nanotech(BaseGenerator):

    def get_topic(self) -> str:
        return "Advanced materials and nanotechnology"

    def get_subtopics(self) -> list[str]:
        return [
            "nanomaterials synthesis", "carbon nanotubes", "graphene applications", "nanocomposites",
            "self-assembling materials", "biomimetic materials", "surface functionalization", "nanofabrication techniques",
            "nanoelectronics", "mechanical properties at nanoscale"
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
        "synthesis yield optimization", "mechanical strength evaluation", "electrical conductivity issue",
        "self-assembly control", "surface modification challenge", "nanofabrication precision",
        "thermal stability problem", "scalability of production", "integration into devices", "material characterization accuracy"
    ]

    openers = [
        "In practical nanotechnology research,",
        "From a materials engineering perspective,",
        "During nanoscale fabrication experiments,",
        "Historically,",
        "When designing advanced nanocomposites,",
        "In nanoelectronics development contexts,"
    ]

    bridges = [
        "this rarely behaves as expected without precise control of conditions.",
        "issues often propagate through synthesis, characterization, and integration steps.",
        "problems often surface only under extreme nanoscale constraints.",
        "small defects can significantly affect mechanical or electrical properties.",
        "what seems optimal in lab tests can fail in device-scale applications."
    ]

    closers = [
        "which is why rigorous experimentation and characterization are essential.",
        "and this insight usually emerges from repeated fabrication and testing cycles.",
        "making it a recurring topic in nanomaterials and advanced materials studies.",
        "and there is rarely a single universally correct synthesis approach.",
        "a lesson reinforced by real-world nanotechnology research and product development."
    ]

    middle_sentences = [
        "Nanomaterials synthesis requires precise control over temperature, pressure, and chemical conditions.",
        "Carbon nanotubes exhibit exceptional mechanical and electrical properties but are sensitive to defects.",
        "Graphene integration into devices demands careful handling and layer control.",
        "Self-assembling materials need strict environmental and chemical conditions for reproducibility.",
        "Surface functionalization can affect adhesion, chemical reactivity, and device performance.",
        "Nanocomposites often face challenges in uniformity, scalability, and mechanical robustness."
      ]
