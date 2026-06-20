from collections.abc import Callable
from functools import reduce, partial, lru_cache, singledispatch
from operator import mul, add
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    op = {"add": add, "multiply": mul, "min": min, "max": max}
    try:
        result = reduce(op[operation], spells)
        return result
    except KeyError:
        print("""operation is not found only 'add',
              'multiply', 'min','max' are valid""")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire": partial(base_enchantment, power=50, element="fire"),
        "ice": partial(base_enchantment, power=50, element="ice"),
        "lightning": partial(base_enchantment, power=50, element="lightning"),
    }


@lru_cache(maxsize=600)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatch(spell: Any) -> str:
        return "Unkown spell type"

    @dispatch.register
    def damage_spell(spell: int) -> int:
        return f"Damage spell: {spell} damage "

    @dispatch.register
    def enchantment(spell: str) -> str:
        return f"Enchantment {spell} "

    @dispatch.register
    def mutlti_cast(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells "

    return dispatch


if __name__ == "__main__":
    print("test spell_reduce")
    print(spell_reducer([56, 4, 45, 6, 8], "multiply"))
    print("testing partial")
    print("testing memoized fibonacci")
    print(memoized_fibonacci(5))
    print(memoized_fibonacci.cache_info())
    print("Testing spell dispatcher...")
    dis = spell_dispatcher()
    print(dis(42))
    print(dis("fireball"))
    print(dis([1, 2, 3]))
    print(dis({}))
