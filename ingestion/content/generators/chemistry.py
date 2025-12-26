from ingestion.content.generators.BaseGenerator import BaseGenerator

class Chemistry(BaseGenerator):

    def get_topic(self) -> str:
        return "Chemistry"

    def get_subtopics(self) -> list[str]:
        return [
            "reaction mechanisms", "stereochemistry", "spectroscopy", "catalysis",
            "coordination chemistry", "polymers", "acids and bases", "redox reactions",
            "kinetics", "thermochemistry"
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
        "reaction rate challenge", "stereochemical outcome problem", "spectral interpretation scenario",
        "catalytic efficiency issue", "coordination complex stability problem", "polymerization control challenge",
        "acid-base titration anomaly", "redox potential calculation", "kinetic modeling complexity", "thermodynamic analysis difficulty"
    ]

    openers = [
        "In practical chemistry experiments,",
        "From an organic chemistry perspective,",
        "During inorganic synthesis exercises,",
        "Historically,",
        "When analyzing reaction pathways,",
        "In catalysis and polymer chemistry contexts,"
    ]

    bridges = [
        "this rarely behaves as expected without careful control of reaction conditions.",
        "issues often propagate through multiple reaction steps or analytical methods.",
        "problems often surface only under sensitive temperature, pressure, or concentration conditions.",
        "small variations in reagents or catalysts can drastically affect outcomes.",
        "what seems straightforward theoretically can yield unexpected experimental results."
    ]

    closers = [
        "which is why meticulous planning, monitoring, and analytical verification are essential.",
        "and this insight usually emerges from repeated experiments and spectral analysis.",
        "making it a recurring topic in chemistry education and research.",
        "and there is rarely a single universally correct synthetic pathway.",
        "a lesson reinforced by real-world laboratory practices and chemical safety considerations."
    ]

    middle_sentences = [
                "Reaction mechanisms may involve competing pathways and side products that complicate interpretation.",
                "Stereochemistry outcomes depend on subtle spatial arrangements and chiral centers.",
                "Spectroscopy requires careful calibration and understanding of molecular signals.",
                "Catalysis efficiency can vary dramatically with temperature, pressure, and catalyst loading.",
                "Coordination chemistry stability is sensitive to ligand effects and electronic configuration.",
                "Kinetic and thermodynamic considerations often influence reaction yield and selectivity."
            ]