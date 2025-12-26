from ingestion.content.generators.BaseGenerator import BaseGenerator

class AstrophysicsAndSpaceExploration(BaseGenerator):

    def get_topic(self) -> str:
        return "Astrophysics and Space Exploration"

    def get_subtopics(self) -> list[str]:
        return [
            "stellar evolution and lifecycle", "galaxies and cosmology", "planetary formation and dynamics",
            "exoplanet detection and characterization", "black holes and neutron stars", "space missions and exploration",
            "astronomical observation techniques", "astrochemistry and interstellar medium", "cosmic radiation and particle physics", "space policy and technology development"
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
        "observational challenge", "mission planning problem", "theoretical modeling scenario",
        "data interpretation issue", "instrument calibration difficulty", "simulation and prediction challenge",
        "celestial dynamics analysis", "exoplanetary system assessment", "high-energy astrophysics problem", "technology deployment scenario"
    ]

    openers = [
        "In practical astrophysics exercises,",
        "From a space exploration perspective,",
        "During observational and mission planning sessions,",
        "Historically,",
        "When analyzing stellar and planetary systems,",
        "In cosmology and high-energy astrophysics contexts,"
    ]

    bridges = [
        "this rarely behaves as expected without precise measurements and modeling.",
        "issues often propagate through gravitational interactions, observational limitations, and instrument sensitivity.",
        "problems often surface only under extreme conditions or over astronomical timescales.",
        "small errors in observation or simulation can drastically affect conclusions.",
        "what seems theoretically consistent can fail under real astrophysical complexity."
    ]

    closers = [
        "which is why rigorous observation, simulation, and adaptive mission planning are essential.",
        "and this insight usually emerges from telescopic data, spectroscopic analysis, and computational modeling.",
        "making it a recurring topic in astrophysics and space exploration education.",
        "and there is rarely a single universally applicable method for studying cosmic phenomena.",
        "a lesson reinforced by multi-wavelength observations, space missions, and theoretical modeling."
    ]

    middle_sentences = [
                "Stellar evolution studies require understanding nuclear fusion, mass loss, and lifecycle stages.",
                "Galaxies and cosmology involve dark matter, dark energy, and large-scale structure analysis.",
                "Planetary formation and dynamics examine accretion processes, orbital mechanics, and disk evolution.",
                "Exoplanet detection includes transit photometry, radial velocity, and direct imaging methods.",
                "Black holes and neutron stars present extreme physics challenges, including relativistic effects and accretion phenomena.",
                "Space missions and exploration involve trajectory planning, spacecraft design, and instrumentation."
            ]