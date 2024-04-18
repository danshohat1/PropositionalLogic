from .logical_connective import LogicalConnective, Model
from ._or import Or
from ._not import Not

class Implication(LogicalConnective):
    def __init__(self, *args):
        super().__init__(*args)
    

    def check_condition(self, model: Model) -> bool:
        if len(self.args)!= 2:
            raise Exception("Implication must have exactly two arguments")
    
        implimication_elimination = Or(Not(self.args[0]),self.args[1])

        return implimication_elimination.check_condition(model)
    