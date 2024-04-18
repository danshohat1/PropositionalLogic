from .logical_connective import LogicalConnective, Model
class Not(LogicalConnective):

    def __init__(self, *args):
        super().__init__(*args)

    def check_condition(self, model: Model) -> bool:
        if len(self.args)!= 1:
            raise Exception("Not must have exactly one argument")

        return not self.args[0].check_condition(model)