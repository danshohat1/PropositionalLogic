from typing import Set
class Symbol:
    def __init__(self, name: str):
        self.name = name

    def check_condition(self, model:dict):
        return model.get(self, False)
    
    @property
    def symbols(self) -> Set:
        return {self}

    def __repr__(self):
        return self.name
    def __str__(self):
        return self.name