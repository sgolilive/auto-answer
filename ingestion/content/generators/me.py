from ingestion.content.generators.BaseGenerator import BaseGenerator

class MaterialEngineering(BaseGenerator):

    def get_topic(self) -> str:
        return "Material Engineering & Nanotechnology"

    def get_subtopics(self) -> list[str]:
        return [
            "advanced alloys and composites", "nanofabrication techniques", "functional nanomaterials",
            "surface engineering and coatings", "mechanical property optimization", "thermal and electrical properties",
            "materials characterization methods", "polymeric materials", "ceramics and biomaterials", "materials failure analysis"
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
        "mechanical testing challenge", "nanostructure synthesis problem", "surface property evaluation scenario",
        "thermal management issue", "electrical performance assessment", "material selection difficulty",
        "degradation and corrosion analysis", "process optimization challenge", "characterization technique problem", "failure prevention scenario"
    ]

    openers = [
        "In practical material engineering exercises,",
        "From a nanotechnology perspective,",
        "During fabrication and characterization sessions,",
        "Historically,",
        "When analyzing material properties and performance,",
        "In advanced materials design contexts,"
    ]

    bridges = [
        "this rarely behaves as expected without precise synthesis and testing.",
        "issues often propagate through microstructural and environmental factors.",
        "problems often surface only under extreme stress, temperature, or loading conditions.",
        "small variations in processing can drastically affect material performance.",
        "what seems optimal in theory can fail under real operational conditions."
    ]

    closers = [
        "which is why rigorous testing, modeling, and process control are essential.",
        "and this insight usually emerges from microscopy, spectroscopy, and mechanical evaluation.",
        "making it a recurring topic in materials science and nanotechnology education.",
        "and there is rarely a single universally optimal material solution.",
        "a lesson reinforced by experimental studies, simulations, and application testing."
    ]

    middle_sentences = [
        "Advanced alloys and composites require careful composition control, processing, and performance testing.",
        "Nanofabrication techniques include lithography, self-assembly, and deposition methods.",
        "Functional nanomaterials exhibit unique electrical, thermal, and mechanical properties.",
        "Surface engineering and coatings improve wear resistance, corrosion protection, and adhesion.",
        "Polymeric materials and ceramics require processing optimization to achieve desired properties.",
        "Materials characterization methods include microscopy, spectroscopy, mechanical testing, and thermal analysis."
      ]
