from ingestion.content.generators.BaseGenerator import BaseGenerator

class MarineBiology(BaseGenerator):

    def get_topic(self) -> str:
        return "marine biology and oceanography"

    def get_subtopics(self) -> list[str]:
        return [
            "coral reef ecosystems", "marine food webs", "ocean currents and circulation", "deep-sea biology",
            "coastal ecology", "marine biodiversity conservation", "ocean chemistry", "fisheries management",
            "marine pollution and remediation", "climate change impact on oceans"
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
        "ecosystem assessment challenge", "species interaction problem", "habitat modeling scenario",
        "pollution mitigation issue", "fisheries sustainability problem", "oceanographic data analysis",
        "climate impact evaluation", "marine conservation planning", "resource management difficulty", "biodiversity monitoring challenge"
    ]

    openers = [
        "In practical marine biology exercises,",
        "From an oceanographic perspective,",
        "During ecosystem and habitat analysis sessions,",
        "Historically,",
        "When analyzing marine ecosystems and ocean processes,",
        "In coastal and deep-sea study contexts,"
    ]

    bridges = [
        "this rarely behaves as expected without comprehensive field measurements and modeling.",
        "issues often propagate through multiple trophic levels and environmental factors.",
        "problems often surface only under extreme weather or anthropogenic stress.",
        "small environmental changes can drastically affect population dynamics and ecosystem stability.",
        "what seems predictable theoretically can fail under complex ocean conditions."
    ]

    closers = [
        "which is why detailed monitoring, modeling, and conservation strategies are essential.",
        "and this insight usually emerges from field studies, remote sensing, and lab analysis.",
        "making it a recurring topic in marine biology and oceanography education.",
        "and there is rarely a single universally effective conservation or management approach.",
        "a lesson reinforced by ecological surveys, simulations, and long-term monitoring programs."
    ]

    middle_sentences = [
        "Coral reef ecosystems depend on symbiotic relationships, water quality, and temperature stability.",
        "Marine food webs involve complex predator-prey dynamics and energy transfer.",
        "Ocean currents and circulation influence nutrient transport, climate, and ecosystem connectivity.",
        "Deep-sea biology studies unique adaptations, biodiversity, and extreme environmental conditions.",
        "Coastal ecology focuses on estuarine habitats, mangroves, and shoreline dynamics.",
        "Marine pollution and remediation examine contaminants, mitigation strategies, and ecosystem recovery."
      ]
