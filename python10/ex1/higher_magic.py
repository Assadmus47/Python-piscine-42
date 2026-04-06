
from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(*args):
        return (spell1(*args), spell2(*args))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def power(target: str, pw: int) -> str:
        return base_spell(target, pw * multiplier)
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
    print("Testing spell combiner...")
    combined = spell_combiner(
        lambda target, pw: f"Fireball hits {target} for {pw}",
        lambda target, pw: f"Heals {target} for {pw}"
    )
    print("Combined spell result:", combined("Dragon", 10))

    print()
    print("Testing power amplifier...")
    amplified = power_amplifier(
        lambda target, pw: f"Fireball hits {target} for {pw}", 3
    )
    print("Original: 10, Amplified:", amplified("Dragon", 10))

    print()
    print("Testing conditional caster...")
    strong_enough = conditional_caster(
        lambda target, pw: pw >= 50,
        lambda target, pw: f"Fireball hits {target} for {pw}"
    )
    print("Power 80:", strong_enough("Dragon", 80))
    print("Power 20:", strong_enough("Dragon", 20))

    print()
    print("Testing spell sequence...")
    sequence = spell_sequence([
        lambda target, pw: f"Fireball hits {target} for {pw}",
        lambda target, pw: f"Heals {target} for {pw}",
        lambda target, pw: f"Shield protects {target}"
    ])
    print("Sequence results:", sequence("Dragon", 10))


if __name__ == "__main__":
    main()
