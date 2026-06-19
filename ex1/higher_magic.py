from typing import Callable


# from data_generator import get_data
# i created the generat fucuase becuase there is no  generat_py file
def get_data() -> list[tuple[str, int]]:
    return [("garden", 10), ("dragon", 50), ("forest", 30)]


def test_condition(target: str, power: int) -> bool:
    return power >= 40


def flower(target: str, power: int) -> str:
    return f"flower is growing for {target} with power{power}"


def tree(target: str, power: int) -> str:
    return f"tree is growing for {target} with power {power} "


def spell_combiner(
    spell1: Callable[[str, int], str],
    spell2: Callable[[str, int], str],
) -> Callable[[str, int], tuple[str, str]]:
    def calling_spells(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))

    return calling_spells


# base spell is the tree
def power_amplifier(
    base_spell: Callable[[str, int], str], multiplier: int
) -> Callable[[str, int], str]:
    def amplified_spells(target: str, power: int) -> str:
        return base_spell(target, (lambda power: power * multiplier)(power))

    return amplified_spells


# spell->flower
def conditional_caster(
    condition: Callable[[str, int], bool],
    spell: Callable[[str, int], str],
) -> Callable[[str, int], str]:
    def cast(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return cast


def spell_sequence(
    spells: list[Callable[[str, int], str]],
) -> Callable[[str, int], list[str]]:
    def casts(target: str, power: int) -> list[str]:
        results = []
        for spell in spells:
            results.append(spell(target, power))
        return results

    return casts


if __name__ == "__main__":
    data = get_data()

    flower("garden", 20)
    tree("garden", 10)
    print("Testing spell combiner...")
    combined = spell_combiner(flower, tree)
    result = combined("garden", 10)
    print(result)
    mege_tree = power_amplifier(tree, 3)
    result2 = mege_tree("garden", 20)
    print(result2)
    condition_flower = conditional_caster(test_condition, flower)
    print(condition_flower("garden", 90))
    print(condition_flower("garden", 33))
    sequence = spell_sequence([flower, tree])
    print("Testing spell sequence with data...")
    for target, power in data:
        print(sequence(target, power))
