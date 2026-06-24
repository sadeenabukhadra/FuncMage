from typing import Callable, Any
from functools import wraps
import time


def spell_timer(func: Callable) -> Callable[[Any], str]:

    @wraps(func)
    def wrapper() -> str:
        print("Testing spell timer...")
        print(f"Casting {func.__name__} ...")
        start = time.time()
        result = func()
        end = time.time()
        duration = end - start
        print(f"Spell completed in  {duration: .3f} seconds")
        return result

    return wrapper


@spell_timer
def fireball() -> str:
    time.sleep(0.101)
    return "Casting fireball..."


def power_validator(min_power: int) -> Callable[[Any], str]:
    def decorator(func: Callable) -> Callable[[Any], str]:
        @wraps(func)
        def wrapper(*args) -> str:
            power = args[-1]
            if power < min_power:
                return "Insufficient power for this spell"
            else:
                return func(*args)

        return wrapper

    return decorator


@power_validator(10)
def fireball_validator(power: int) -> str:
    return f"the power is {power} power "


# not completed
def retry_spell(max_attempts: int) -> Callable[[Any], str]:
    def decorator(func: Callable[[Any], str]) -> Callable[[Any], str]:
        @wraps(func)
        def wrapper(attempts: int) -> str:
            for i in range(1, max_attempts + 1):
                try:
                    return func(attempts)

                except Exception:
                    if i < max_attempts:
                        print(f"Spell failed, retrying...\
(attempt {i}/{max_attempts})")
                    else:
                        return f"Spell casting failed \
                        after {max_attempts} attempts"

        return wrapper

    return decorator


@retry_spell(3)
def retry_test(attempts: int) -> None:
    raise ValueError()


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3:
            for char in name:
                if not (char.isalpha() or char.isspace()):
                    return False
            return True
        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print(fireball())
    valid = fireball_validator(5)
    print(valid)
    invlid = fireball_validator(12)
    print(invlid)
    print("Testing retrying spell...")
    print(retry_test(3))
    print("Waaaaaaagh spelled !")
    print("Testing MageGuild...")
    g = MageGuild()
    print("valid name")
    print(g.validate_mage_name("MeGe"))
    print("invalid name")
    print(g.validate_mage_name("me12"))
    print("testing of insufficient power")
    print(g.cast_spell("Fireball", 5))
    print("print valid cast fireball")
    print(g.cast_spell("Fireball", 20))
