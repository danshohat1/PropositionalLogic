from .logical_connective import LogicalConnective, Model
from ._or import Or
from ._not import Not

class Implication(LogicalConnective):
    def __init__(self, *args):
        assert len(args) == 2, "Implication must have exactly two arguments"
        super().__init__(*args)
    
    def check_condition(self, model: Model) -> bool:
        implimication_elimination = Or(Not(self.args[0]),self.args[1])

        return implimication_elimination.check_condition(model)

    def __repr__(self) -> str:
        return f"({str(self.args[0])} -> {str(self.args[1])})"
    