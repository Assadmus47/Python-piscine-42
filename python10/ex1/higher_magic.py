
from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(*args):
        return (spell1(*args), spell2(*args))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def power(*args):
        return base_spell(*args) * multiplier
    return power


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def rtr_function(*args):
        if condition(*args):
            return spell(*args)
        else:
            return "Spell fizzled"

    return rtr_function


def spell_sequence(spells: list[Callable]) -> Callable:
    def browse_funct(*arg):
        result: list = []
        for func in spells:
            result.append(func(*arg))
        return result
    return browse_funct


def main() -> None:
    print()
    print("Testing spell combiner...")
    result: Callable = spell_combiner(
        lambda: "Fireball hits Dragon", lambda: "Heals Dragon"
        )
    print("Combined spell result:", ", ".join(result()))
    print()
    print("Testing power amplifier...")
    result = power_amplifier(lambda: 10, 3)
    print("Original: 10, Amplified:", result())


if __name__ == "__main__":
    main()
