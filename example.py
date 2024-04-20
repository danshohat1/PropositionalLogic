"""
Example:


1. If it's rainy, then you should take an umbrella
2. If it's rainy and foggy, then you should stay at home
3. It's foggy if it's under 20C°.
4. It's rainy
5. It's 25C°.

should you stay at home today?

Soulution:
"""

from logic import *

# weathers
rainy = Symbol("rainy")
foggy = Symbol("foggy")
under_20_temp = Symbol("under_20_temp")

# causes
umbrella = Symbol("umbrella")
stay_at_home = Symbol("stay_at_home")


knowledge = KnowledgeBase(
   Implication(rainy, umbrella), # If it's rainy, then you should take an umbrella
   Implication(And(rainy, foggy), stay_at_home), # If it's rainy and foggy, then you should stay at home
   Implication(under_20_temp, foggy), # It's foggy if it's under 20C°.
   rainy,  # It's rainy
   Not(under_20_temp) # It's not under 20C°.
)

print(knowledge) # prints: (¬under_20_temp) ∧ (rainy -> umbrella) ∧ rainy ∧ ((rainy ∧ foggy) -> stay_at_home) ∧ (under_20_temp -> foggy)

query = KnowledgeBase(
    stay_at_home
) # should you stay at home?

print(check_logic(knowledge, query)) # prints: False

