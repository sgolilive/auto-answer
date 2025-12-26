from ingestion.content.generators.BaseGenerator import BaseGenerator

class PhysicsGenerator(BaseGenerator):

    def get_sentence_pool(self) -> list[str]:
        pass

    def get_intro_options(self, subtopic: str) -> list[str]:
        pass

    def generate_question(self, subtopic: str) -> str:
        return super().generate_question(subtopic)

    def generate_answer(self, subtopic: str) -> str:
        return super().generate_answer(subtopic)

    def get_topic(self) -> str:
        return "physics"

    def get_subtopics(self) -> list[str]:
        return [
                "mechanics", "thermodynamics", "electromagnetism", "quantum physics",
                "relativity", "optics", "nuclear physics", "particle physics",
                "statistical physics", "astrophysics"
            ]

    question_intents = [
        "experimental measurement challenge", "theoretical derivation problem", "energy conservation scenario",
        "particle interaction complexity", "relativistic effect calculation", "wave propagation issue",
        "quantum state interpretation", "thermodynamic equilibrium challenge", "electromagnetic field analysis", "statistical distribution anomaly"
    ]

    openers = [
        "In practical physics experiments,",
        "From a theoretical physics perspective,",
        "During laboratory measurements,",
        "Historically,",
        "When analyzing complex systems,",
        "In astrophysical observations contexts,"
    ]

    bridges = [
        "this rarely behaves as expected without precise instrumentation and modeling.",
        "issues often propagate through measurement, calculation, and interpretation steps.",
        "problems often surface only under extreme or high-precision conditions.",
        "small variations can drastically affect outcomes and theoretical validation.",
        "what seems straightforward theoretically may yield unexpected experimental results."
    ]

    closers = [
        "which is why meticulous experimentation and theoretical cross-checks are essential.",
        "and this insight usually emerges from repeated experiments and model simulations.",
        "making it a recurring topic in physics education and research.",
        "and there is rarely a single universally correct approach in complex systems.",
        "a lesson reinforced by real-world laboratory and observational data."
    ]

    middle_sentences = [
            "Mechanics experiments require careful control of forces, friction, and boundary conditions.",
            "Thermodynamics problems often involve understanding energy exchange and entropy variations.",
            "Electromagnetic field calculations can be sensitive to boundary and initial conditions.",
            "Quantum physics introduces probabilistic interpretations and non-intuitive phenomena.",
            "Relativity demands precise consideration of space-time effects at high velocities.",
            "Astrophysical systems involve extreme scales, requiring approximation and modeling techniques."
    ]