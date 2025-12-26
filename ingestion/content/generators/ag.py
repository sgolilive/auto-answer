from ingestion.content.generators.BaseGenerator import BaseGenerator

class AgriSciAndFoodTech(BaseGenerator):

    def generate_question(self, subtopic: str) -> str:
        return super().generate_question(subtopic)

    def generate_answer(self, subtopic: str) -> str:
        return super().generate_answer(subtopic)

    def get_topic(self) -> str:
        return 'Agricultural Sciences and Food Technology'

    def get_subtopics(self) -> list[str]:
        return [
                "crop genetics and breeding", "soil science", "precision agriculture", "plant pathology",
                "agroforestry systems", "post-harvest technology", "food processing techniques", "sustainable farming practices",
                "irrigation and water management", "agricultural supply chain and logistics"
                ]

    def get_sentence_pool(self) -> list[str]:
        pass

    def get_intro_options(self, subtopic: str) -> list[str]:
        pass

    question_intents = [
        "yield optimization challenge", "disease management problem", "soil fertility assessment scenario",
        "irrigation planning issue", "food safety evaluation", "processing efficiency problem",
        "sustainability strategy challenge", "crop rotation modeling", "harvest storage optimization", "supply chain efficiency problem"
    ]

    openers = [
        "In practical agricultural science exercises,",
        "From a crop and soil management perspective,",
        "During precision farming and food processing sessions,",
        "Historically,",
        "When analyzing plant growth and food systems,",
        "In agroforestry and sustainable agriculture contexts,"
    ]

    bridges = [
        "this rarely behaves as expected without careful monitoring and planning.",
        "issues often propagate through environmental factors, pests, and resource constraints.",
        "problems often surface only under variable climatic conditions or seasonal changes.",
        "small deviations in soil, nutrient, or irrigation management can drastically affect yields.",
        "what seems optimal theoretically can fail under field conditions."
    ]

    closers = [
        "which is why detailed analysis, experimentation, and adaptive management are essential.",
        "and this insight usually emerges from field trials, laboratory studies, and post-harvest monitoring.",
        "making it a recurring topic in agricultural science and food technology education.",
        "and there is rarely a single universally applicable farming or processing strategy.",
        "a lesson reinforced by crop performance studies, sustainability assessments, and technological innovations."
    ]

    middle_sentences = [
                "Crop genetics and breeding involve selecting traits, hybridization, and genomic analysis.",
                "Soil science examines nutrient cycles, texture, and fertility management.",
                "Precision agriculture uses sensors, drones, and data analytics for optimized farming.",
                "Plant pathology investigates disease etiology, control measures, and resistance breeding.",
                "Post-harvest technology focuses on storage, shelf-life, and processing efficiency.",
                "Food processing techniques include thermal, enzymatic, and preservation methods."
            ]