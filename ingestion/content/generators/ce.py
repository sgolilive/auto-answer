from ingestion.content.generators.BaseGenerator import BaseGenerator

class ChemicalEngineering(BaseGenerator):

    def get_topic(self) -> str:
        return "Chemistry & Chemical Engineering"

    def get_subtopics(self) -> list[str]:
        return [
            "organic chemistry reactions", "inorganic chemistry mechanisms", "physical chemistry",
            "thermodynamics", "kinetics", "process engineering", "chemical reaction engineering",
            "material science", "analytical chemistry", "catalysis and reaction optimization"
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
        "reaction optimization challenge", "mechanism elucidation problem", "process scale-up scenario",
        "thermodynamic analysis difficulty", "kinetic modeling issue", "material characterization problem",
        "catalyst design challenge", "safety and hazard assessment", "analytical measurement reliability", "reaction selectivity evaluation"
    ]

    openers = [
        "In practical chemistry and chemical engineering experiments,",
        "From an industrial process perspective,",
        "During laboratory reaction analysis,",
        "Historically,",
        "When analyzing thermodynamic and kinetic processes,",
        "In chemical synthesis and material design contexts,"
    ]

    bridges = [
        "this rarely behaves as expected without careful monitoring and optimization.",
        "issues often propagate through reaction steps, scaling, and process variables.",
        "problems often surface only under specific temperature, pressure, or concentration conditions.",
        "small variations in experimental setup can drastically affect yield, selectivity, or safety.",
        "what seems theoretically feasible can fail under real-world chemical engineering constraints."
    ]

    closers = [
        "which is why rigorous experimental design, simulation, and process control are essential.",
        "and this insight usually emerges from repeated trials and analytical verification.",
        "making it a recurring topic in chemistry and chemical engineering education.",
        "and there is rarely a single universally optimal reaction or process condition.",
        "a lesson reinforced by industrial practice and laboratory experience."
    ]

    middle_sentences = [
        "Organic chemistry reactions may have competing pathways affecting yield and selectivity.",
        "Inorganic chemistry mechanisms require careful monitoring of coordination and electron transfer.",
        "Physical chemistry problems involve thermodynamic, kinetic, and quantum considerations.",
        "Chemical reaction engineering involves reactor design, mass transfer, and process optimization.",
        "Material science challenges include structure-property relationships and process reproducibility.",
        "Catalysis requires precise control of active sites, temperature, and pressure for optimal activity."
    ]