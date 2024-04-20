class KnowledgeBase:
    def __init__(self, *connectives) -> None:
        self.connectives = set(connectives)

    @property
    def symbols(self) -> set:
        return {symbol for connective in self.connectives for symbol in connective.symbols}

    def add(self, connective) -> None:
        self.connectives.add(connective)
    def check_knowledge(self, model: dict) -> bool:
        return all(connective.check_condition(model) for connective in self.connectives)
    def remove(self, connective) -> None:
        self.connectives.remove(connective)
    
    def __repr__(self) -> str:
        return " ∧ ".join(str(connective) for connective in self.connectives)