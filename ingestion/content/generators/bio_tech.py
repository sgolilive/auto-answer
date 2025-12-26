from ingestion.content.generators.BaseGenerator import BaseGenerator

class BioTechnologyAndGeneticEngineering(BaseGenerator):

    def get_topic(self) -> str:
        return "biotechnology and genetic engineering"

    def get_subtopics(self) -> list[str]:
        return [
            "CRISPR gene editing", "gene therapy", "synthetic biology", "protein engineering",
            "genomic sequencing", "stem cell applications", "bioinformatics pipelines", "genetic regulation",
            "microbial engineering", "biopharmaceutical development", "stem cell research", "genomics",
            "proteomics",  "bioinformatics", "molecular cloning", "bioreactor optimization"
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
        "gene modification challenge", "therapeutic application scenario", "protein design optimization",
        "sequencing error mitigation", "bioinformatics data processing", "stem cell differentiation control",
        "regulatory compliance issue", "microbial production efficiency", "ethical concern evaluation", "biopharmaceutical scaling problem"
        "gene editing challenge", "ethical dilemma", "experimental reproducibility issue",
        "data analysis complexity", "therapy efficacy problem",
        "synthetic pathway bottleneck", "regulatory compliance scenario", "genomic sequencing error", "bioreactor scale-up problem"
    ]

    openers = [
        "In practical biotechnology experiments,",
        "From a genetic engineering perspective,",
        "During CRISPR or gene therapy trials,",
        "Historically,",
        "When designing synthetic biology constructs,",
        "In biopharmaceutical development contexts,"
        "During laboratory-based gene editing studies,",
        "When analyzing genomic data,",
        "In synthetic biology applications,"
    ]

    bridges = [
        "this rarely behaves as expected without careful experimental design and validation.",
        "issues often propagate through multiple molecular or computational steps.",
        "problems often surface only under variable cell lines or sequencing conditions.",
        "small deviations in protocols can drastically affect experimental outcomes.",
        "what seems theoretically feasible can fail under real-world lab constraints."
        ]

    closers = [
        "which is why meticulous planning, ethical considerations, and iterative testing are essential.",
        "and this insight usually emerges from repeated experiments and bioinformatic analyses.",
        "making it a recurring topic in biotechnology research and genetic engineering courses.",
        "and there is rarely a single universally optimal approach for complex gene manipulations.",
        "a lesson reinforced by real-world laboratory practices and regulatory compliance."
    ]

    middle_sentences = [
        "CRISPR gene editing requires precise targeting and off-target effect minimization.",
        "Stem cell differentiation outcomes can vary with culture conditions and genetic background.",
        "Synthetic biology pathway design demands careful enzyme and promoter selection.",
        "Genomics and proteomics data need rigorous statistical and computational validation.",
        "Protein engineering challenges include stability, folding, and functional activity optimization.",
        "Gene therapy experiments must consider delivery mechanisms, immune response, and long-term safety."
    ]