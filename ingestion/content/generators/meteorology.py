from ingestion.content.generators.BaseGenerator import BaseGenerator

class Meteorology(BaseGenerator):

    def get_topic(self) -> str:
        return "Meteorology and Climate Science"

    def get_subtopics(self) -> list[str]:
        return [
            "weather forecasting models", "climate variability and change", "extreme weather events",
            "atmospheric dynamics", "hydrological cycles", "tropical cyclones", "monsoon systems",
            "climate modeling and simulation", "aerosol and cloud interactions", "climate mitigation strategies"
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
        "forecasting challenge", "data assimilation problem", "simulation scenario",
        "extreme event analysis", "climate impact assessment", "policy evaluation problem",
        "hydrological modeling difficulty", "atmospheric measurement challenge", "prediction validation issue", "mitigation planning scenario"
    ]

    openers = [
        "In practical meteorology exercises,",
        "From a climate science perspective,",
        "During weather modeling and prediction sessions,",
        "Historically,",
        "When analyzing atmospheric phenomena,",
        "In climate impact and policy contexts,"
    ]

    bridges = [
        "this rarely behaves as expected without accurate data and model calibration.",
        "issues often propagate across temporal and spatial scales.",
        "problems often surface only under complex environmental interactions.",
        "small changes in parameters can drastically affect forecasts and simulations.",
        "what seems straightforward theoretically can fail under real-world atmospheric variability."
    ]

    closers = [
        "which is why careful observation, modeling, and validation are essential.",
        "and this insight usually emerges from satellite data, ground-based measurements, and simulation outputs.",
        "making it a recurring topic in meteorology and climate science education.",
        "and there is rarely a single universally accurate forecast model.",
        "a lesson reinforced by long-term climate studies and extreme event analyses."
    ]

    middle_sentences = [
        "Weather forecasting models rely on numerical simulations, parameterization, and real-time data.",
        "Climate variability and change involve natural cycles, anthropogenic effects, and feedback mechanisms.",
        "Extreme weather events require rapid analysis, prediction, and risk assessment.",
        "Atmospheric dynamics examines wind patterns, pressure systems, and jet streams.",
        "Hydrological cycles study precipitation, evaporation, runoff, and groundwater interactions.",
        "Climate mitigation strategies include emission reduction, adaptation planning, and policy evaluation."
      ]