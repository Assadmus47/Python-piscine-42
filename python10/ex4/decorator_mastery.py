
from functools import wraps

from typing import Callable

import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        elapsed = round(end - start, 3)
        print(f"Spell completed in {elapsed} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs.get('power', args[0])
            if power >= min_power:
                result = func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
            return result
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        "Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})"
                        )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str):
        return len(name) >= 3 and name.replace(" ", "").isalpha()

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int):
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball():
    return "Fireball cast!"


def main() -> None:
    print("Testing spell timer...")
    result: str = fireball()
    print("Result:", result)
    print()
    print("Testing MageGuild...")
    guild = MageGuild()
    print(guild.validate_mage_name("mkacemi"))
    print(guild.validate_mage_name("mkacemi3"))
    print(guild.cast_spell("Lightning", power=15))
    print(guild.cast_spell("Lightning", power=5))


if __name__ == "__main__":
    main()
