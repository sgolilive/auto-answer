import random
from ingestion.content.generators.BaseGenerator import BaseGenerator

class ProgGenerator(BaseGenerator):

    def generate_answer(self, subtopic: str) -> str:
        intro_options = self.get_intro_options(subtopic)

        sentence_count = random.randint(3, 7)
        sentences = [random.choice(intro_options)]
        sentences.extend(random.sample(self.get_sentence_pool(), k=sentence_count - 1))

        return " ".join(sentences)

    def generate_question(self, subtopic: str) -> str:
        return random.choice(self.get_question_templates(subtopic))

    question_templates = {
            "function": [
                "What is a function in programming and why is it commonly used?",
                "In large codebases, how do functions contribute to maintainability, readability, and reuse across teams and modules?",
                "How does defining clear function responsibilities influence long-term software evolution and debugging efforts?",
                "Why do poorly designed functions often become sources of bugs and technical debt over time?"
            ],
            "class": [
                "What problem does a class solve in object-oriented programming?",
                "Why are classes considered a foundational abstraction in object-oriented design?",
                "How do class boundaries affect collaboration in large engineering teams?"
            ],
            "object": [
                "What is an object and how does it relate to a class?",
                "Why are objects useful for representing real-world behavior in software systems?",
                "How does object interaction shape overall system behavior?"
            ],
            "inheritance": [
                "Why is inheritance used in object-oriented programming?",
                "What risks does inheritance introduce in evolving systems?",
                "When does inheritance become more harmful than helpful?"
            ],
            "polymorphism": [
                "What is polymorphism and why is it useful?",
                "How does polymorphism reduce the need for conditional logic?",
                "Why does polymorphism improve extensibility in large systems?"
            ],
            "encapsulation": [
                "What is encapsulation and why does it matter?",
                "How does encapsulation reduce unintended side effects?",
                "Why does poor encapsulation slow down system evolution?"
            ],
            "abstraction": [
                "What is abstraction in programming?",
                "How does abstraction help manage complexity?",
                "Why do leaky abstractions cause long-term problems?"
            ],
            "exception handling": [
                "What is exception handling?",
                "Why is exception handling preferred over error codes?",
                "How can exception misuse make debugging harder?"
            ],
            "memory management": [
                "What is memory management?",
                "Why does memory behavior affect performance stability?",
                "How can memory leaks remain hidden for long periods?"
            ],
            "garbage collection": [
                "What is garbage collection?",
                "Why do garbage collection pauses impact latency-sensitive systems?",
                "How does GC tuning influence throughput?"
            ],
            "immutability": [
                "What does immutability mean?",
                "Why does immutability simplify concurrent programming?",
                "How does immutability affect system design choices?"
            ],
            "concurrency": [
                "What is concurrency?",
                "Why is concurrency hard to get right?",
                "How do concurrency bugs evade testing?"
            ],
            "multithreading": [
                "What is multithreading?",
                "Why do race conditions occur in multithreaded programs?",
                "How does thread contention degrade performance?"
            ],
            "asynchronous programming": [
                "What is asynchronous programming?",
                "Why does async programming scale better for I/O workloads?",
                "How does async code change control flow reasoning?"
            ]
        }

    def get_topic(self) -> str:
        return 'programming'

    def get_subtopics(self) -> list[str]:
        return [
                "function","class","object","inheritance","polymorphism","encapsulation","abstraction",
                "exception handling","memory management","garbage collection","immutability",
                "concurrency","multithreading","asynchronous programming"
                ]

    def get_sentence_pool(self) -> list[str]:
        return [
            "Its real impact often emerges only after the system has been in use for some time.",
            "Developers usually encounter issues here indirectly rather than through immediate failures.",
            "Small design shortcuts in this area can have disproportionate effects later.",
            "Production workloads tend to expose weaknesses that tests rarely catch.",
            "What seems intuitive at first can behave unpredictably under scale.",
            "Many outages trace back to decisions made in this area long before.",
            "Operational complexity grows faster when this aspect is neglected.",
            "Teams often adapt workarounds instead of addressing root causes.",
            "The cost of fixing mistakes here increases sharply over time.",
            "Early success can mask deeper structural problems.",
            "Changes that appear local frequently have system-wide consequences.",
            "Debugging issues related to this often requires deep system knowledge.",
            "Performance degradation is usually gradual rather than sudden.",
            "Monitoring data often provides the first signal of trouble.",
            "Design assumptions tend to break under real user behavior.",
            "Scaling amplifies inefficiencies that were previously invisible.",
            "Engineers often develop intuition here through repeated failures.",
            "The impact of this decision is rarely confined to a single module.",
            "Maintenance effort grows when boundaries are unclear.",
            "Seemingly unrelated bugs often share a common root here.",
            "This is an area where theory and practice diverge significantly.",
            "Systems with heavy usage patterns feel the effects most strongly.",
            "Refactoring becomes harder as dependencies accumulate.",
            "The symptoms usually appear far from the original cause.",
            "Reliability issues often surface during peak load.",
            "Architectural constraints magnify poor decisions here.",
            "Design clarity reduces the cognitive load on engineers.",
            "Teams pay the price long after the original authors have moved on.",
            "Subtle inefficiencies accumulate over repeated executions.",
            "Failure modes are often non-deterministic.",
            "Testing rarely simulates the full range of real conditions.",
            "Documentation alone cannot compensate for weak design here.",
            "Operational incidents frequently expose hidden coupling.",
            "This area benefits more from discipline than cleverness.",
            "Performance tuning often circles back to this concern.",
            "System evolution slows when this is poorly handled.",
            "Complexity grows faster than expected when shortcuts are taken.",
            "Root cause analysis often leads back to early design trade-offs.",
            "Reliability engineering places special emphasis here.",
            "Production metrics often contradict lab assumptions.",
            "High-traffic systems experience the downsides first.",
            "Engineering velocity drops when this becomes fragile.",
            "Incremental fixes tend to compound the problem.",
            "Long-running processes reveal issues faster.",
            "Load patterns expose behavior that unit tests miss.",
            "Operational maturity highlights weaknesses clearly.",
            "Systems under stress amplify design flaws.",
            "Scaling forces implicit assumptions into the open.",
            "Engineering teams often underestimate its long-term cost.",
            "Seemingly benign changes can trigger cascading failures.",
            "The feedback loop here is often slow and indirect.",
            "Design debt accumulates silently until it becomes unavoidable.",
            "This concern influences how safely systems can change.",
            "Observability often provides delayed but crucial insight.",
            "Architectural reviews frequently surface issues here.",
            "Stability issues tend to cluster around this area.",
            "Performance regressions often originate upstream.",
            "Operational incidents rarely have a single cause.",
            "This is an area where conservative design pays off.",
            "Systems optimized too early often struggle later.",
            "The long tail of bugs is usually rooted here.",
            "Growth magnifies the cost of early assumptions.",
            "Production failures teach lessons documentation cannot.",
            "Engineering discipline matters more than tooling.",
            "The impact is often felt more by operators than developers.",
            "Teams gradually learn to recognize warning signs.",
            "Design simplicity reduces failure probability.",
            "Maintenance becomes reactive rather than proactive.",
            "The system’s behavior drifts as usage evolves.",
            "Load testing rarely captures full complexity.",
            "Operational pressure exposes hidden dependencies.",
            "This concern affects both correctness and performance.",
            "Failures often appear intermittent and hard to trace.",
            "Design rigidity slows response to change.",
            "System resilience depends heavily on choices made here.",
            "Minor inefficiencies multiply under repetition.",
            "Operational experience reshapes design priorities.",
            "This area often defines the ceiling for scalability.",
            "Engineering trade-offs become irreversible over time.",
            "High availability amplifies the consequences of mistakes.",
            "Design oversights tend to surface during growth spurts.",
            "The system’s weakest assumptions usually fail first.",
            "Production behavior frequently surprises designers.",
            "Complex systems punish inconsistency here.",
            "Engineering maturity shows in how this is handled.",
            "Systems degrade gracefully only with careful design.",
            "The cost of change grows faster than expected.",
            "Operational confidence depends on robustness here.",
            "This aspect often determines how debuggable a system is.",
            "Engineering intuition develops slowly in this area.",
            "The long-term cost far outweighs initial convenience.",
            "Design clarity improves both velocity and safety."
        ]

    def get_intro_options(self, subtopic: str) -> list[str]:
        return [
                f"{subtopic.capitalize()} influences how systems behave once they move beyond trivial scenarios.",
                f"When software operates under real workloads, {subtopic} becomes a defining factor.",
                f"{subtopic.capitalize()} affects not just correctness but also long-term system behavior.",
                f"In production environments, {subtopic} often determines how predictable a system feels."
                ]