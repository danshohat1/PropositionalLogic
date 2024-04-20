from .logical_connective import LogicalConnective, Model

class Not(LogicalConnective):

    def __init__(self, *args):
        assert len(args) == 1, "Not must have exactly one argument"
        super().__init__(*args)

    def check_condition(self, model: Model) -> bool:
        return not self.args[0].check_condition(model)

    def __repr__(self) -> str:
        return f"(¬{str(self.args[0])})"