from .logical_connective import LogicalConnective, Model

class And(LogicalConnective):
    def __init__(self, *args):
        super().__init__(*args)


    def check_condition(self, model: Model) -> bool:
       return all(arg.check_condition(model) for arg in self.args)