from collections.abc import Callable
def test_condition(power:int)->bool:
    return power >= 40

def flower(target: str, power: int) -> str:
    return f"flower is growing for {target} with power{power}"

def tree(target: str, power: int) -> str:
    return f"tree is growing for {target} with power {power} "

def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def calling_spells(target:str,power:int):
        return (
            spell1(target,power),
            spell2(target,power)
        )
    return calling_spells
# base spell is the tree
def power_amplifier(base_spell: Callable, multiplier: int) ->Callable:
    def amplified_spells(target,power) ->str:
        return base_spell(
            target,
            (lambda power : power * multiplier)(power)
        )
    return amplified_spells
#spell->flower
def conditional_caster(condition: Callable, spell: Callable) ->Callable:
    return(test_condition())
    


   
flower("garden",20)
tree("garden",10)
print("Testing spell combiner...")
combined = spell_combiner(flower,tree)
result = combined("garden",10)
print(result)
mege_tree=power_amplifier(tree,3) 
result2=mege_tree("garden",20)
print(result2)




