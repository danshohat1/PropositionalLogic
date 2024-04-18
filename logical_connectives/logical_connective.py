from abc import ABC, abstractmethod
from typing import Dict
from .proposition_symbol import Symbol

Model = Dict[str, bool]

class LogicalConnective(ABC):
    def __init__(self, *args):
        self.args = args
    
    @property
    def symbols(self) -> set:
        # return a set of all the args that are symbols
       return {arg for arg in self.args if isinstance(arg, Symbol)} 
    
    @abstractmethod
    def check_condition(self, model: Model) -> bool:
        pass