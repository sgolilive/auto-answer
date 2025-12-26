from ingestion.content.generators.BaseGenerator import BaseGenerator

class AstronomyAndAstrophysics(BaseGenerator):

    def get_topic(self) -> str:
        return "Astronomy and Astrophysics"

    def get_subtopics(self) -> list[str]:
        return [
            "stellar evolution", "exoplanets", "galaxies and dark matter", "cosmology",
            "black holes and neutron stars", "observational astronomy", "planetary science",
            "space missions and telescopes", "astrochemistry", "astrophysical simulations"
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
        "observation challenge", "data analysis problem", "theoretical modeling scenario",
        "mission planning issue", "instrumentation calibration problem", "stellar dynamics analysis",
        "cosmological parameter estimation", "exoplanet detection difficulty", "astrochemical interpretation challenge", "simulation validation problem"
    ]

    openers = [
        "In practical astronomy exercises,",
        "From an astrophysical perspective,",
        "During observational and theoretical sessions,",
        "Historically,",
        "When analyzing celestial phenomena,",
        "In space mission and telescope contexts,"
    ]

    bridges = [
        "this rarely behaves as expected without precise measurement and modeling.",
        "issues often propagate through multiple scales from stellar to cosmological phenomena.",
        "problems often surface only under extreme physical conditions or observational limits.",
        "small deviations in instrument calibration can drastically affect interpretations.",
        "what seems theoretically simple can fail under real observational constraints."
    ]

    closers = [
        "which is why careful data analysis, simulation, and cross-validation are essential.",
        "and this insight usually emerges from telescope observations, spectroscopy, and computational models.",
        "making it a recurring topic in astrophysics education and research.",
        "and there is rarely a single universally applicable model for complex celestial systems.",
        "a lesson reinforced by observational campaigns, simulations, and multi-wavelength studies."
    ]

    middle_sentences = [
                "Stellar evolution involves nuclear fusion, life cycles, and end-stage phenomena.",
                "Exoplanet studies require precise transit, radial velocity, and direct imaging observations.",
                "Galaxies and dark matter research examines mass distribution, dynamics, and structure formation.",
                "Cosmology investigates the expansion of the universe, cosmic microwave background, and dark energy.",
                "Black holes and neutron stars challenge understanding of extreme gravity, accretion, and relativistic physics.",
                "Observational astronomy depends on telescope instrumentation, spectral analysis, and multi-wavelength data."
            ]