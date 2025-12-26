from ingestion.content.generators.BaseGenerator import BaseGenerator


class PhysicsEngineeringMechanics(BaseGenerator):

    def get_topic(self) -> str:
        return "physics and engineering mechanics"

    def get_subtopics(self) -> list[str]:
        return [
            "classical mechanics", "thermodynamics", "fluid dynamics", "electromagnetism",
            "quantum mechanics", "solid mechanics", "vibrations and waves", "control systems",
            "mechanical design principles", "energy systems"
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
        "problem-solving challenge", "experimental analysis problem", "modeling scenario",
        "design optimization issue", "system behavior prediction", "stress-strain evaluation",
        "dynamic response analysis", "control system tuning", "energy efficiency calculation", "applied physics scenario"
    ]

    openers = [
        "In practical physics and engineering exercises,",
        "From a theoretical and applied perspective,",
        "During laboratory and modeling sessions,",
        "Historically,",
        "When analyzing complex mechanical systems,",
        "In energy and system design contexts,"
    ]

    bridges = [
        "this rarely behaves as expected without precise modeling and experimental validation.",
        "issues often propagate through multiple subsystems and physical interactions.",
        "problems often surface only under extreme conditions or nonlinear effects.",
        "small variations in design parameters can drastically affect performance or stability.",
        "what seems straightforward theoretically can fail under real-world engineering constraints."
    ]

    closers = [
        "which is why meticulous analysis, simulation, and testing are essential.",
        "and this insight usually emerges from iterative experimentation and performance evaluation.",
        "making it a recurring topic in physics and engineering education.",
        "and there is rarely a single universally optimal solution for complex systems.",
        "a lesson reinforced by practical engineering projects and laboratory results."
    ]

    middle_sentences = [
        "Classical mechanics problems often involve forces, motion equations, and energy conservation.",
        "Thermodynamics and energy systems require careful consideration of heat, work, and efficiency.",
        "Fluid dynamics challenges include turbulence, pressure variations, and flow optimization.",
        "Electromagnetism problems require understanding fields, currents, and interactions.",
        "Quantum mechanics demands comprehension of probabilistic outcomes and wavefunctions.",
        "Solid mechanics and vibrations involve stress-strain relations, natural frequencies, and damping."
      ]