from logical_connectives import *
from knowledge import KnowledgeBase
from logical_connectives.proposition_symbol import Symbol
from typing import Set, Dict


def check_logic(knowledge_base: KnowledgeBase, query: KnowledgeBase) -> bool:
    def check_all(knowledge_base: KnowledgeBase, query: KnowledgeBase, symbols: Set[Symbol], model: Dict = dict(), results=[]):
        if not symbols:
            if knowledge_base.check_knowledge(model):
                result = query.check_knowledge(model)
                results.append(result)
                return result
            return True

        remaining = symbols.copy()
        symbol = remaining.pop()

        model_true = model.copy()
        model_true[symbol] = True

        model_false = model.copy()
        model_false[symbol] = False

        true_check = check_all(knowledge_base, query, remaining, model_true, results)
        false_check = check_all(knowledge_base, query, remaining, model_false, results)
        return true_check and false_check


    symbols = set.union(knowledge_base.symbols, query.symbols)
    return check_all(knowledge_base, query, symbols)