from typing import Callable, Any
from functools import wraps
import time


def spell_timer(func: Callable) -> Callable[[Any]str]:

    @wraps(func)
    def wrapper() -> str:
        print("Testing spell timer...")
        print(f"Casting {func.__name__} ...")
        start = time.time()
        result = func()
        end = time.time()
        duration = end - start
        print(f"Spell completed in  {duration :.3f} seconds")
        return result

    return wrapper


@spell_timer
def fireball() -> str:
    time.sleep(0.101)
    return "Casting fireball..."


def power_validator(min_power: int) -> Callable[[Any], str]:
    def decorator(func: Callable) -> Callable[[Any], str]:
        @wraps(func)
        def wrapper(power: int) -> str:
            if power < min_power:
                return "Insufficient power for this spell"
            else:
                return func(power)

        return wrapper

    return decorator


@power_validator(10)
def fireball_validator(power: int) -> str:
    return f"the power is {power} power "
# not completed
def retry_spell(max_attempts: int) -> Callable[[Any],str]:
    def decorator(func:Callable[[Any],str])->Callable[[Any],str]:     
    @wraps(func)
    def wrapper()->str:
        for i in range(1,max_attempts+1):
            try:


if __name__ == "__main__":
    print(fireball())
    valid = fireball_validator(5)
    print(valid)
    invlid = fireball_validator(12)
    print(invlid)
