
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        return reduce(add, spells)
    elif operation == "multiply":
        return reduce(mul, spells)
    elif operation == "max":
        return reduce(lambda a, b: a if a > b else b, spells)
    elif operation == "min":
        return reduce(lambda a, b: a if a < b else b, spells)
    return 0


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        'fire_enchant': partial(base_enchantment, power=50, element="fire"),
        'ice_enchant': partial(base_enchantment, power=50, element="ice"),
        'lightning_enchant':
            partial(base_enchantment, power=50, element="lightning")
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable:
    @singledispatch
    def cast_spell(arg):
        return "Unknown spell"

    @cast_spell.register(int)
    def _(arg):
        return f"Damage spell: {arg}"

    @cast_spell.register(str)
    def _(arg):
        return f"Enchantment: {arg}"

    @cast_spell.register(list)
    def _(arg):
        return f"Multi-cast: {arg}"

    return cast_spell


def main() -> None:
    print("Testing spell reducer...")
    print()
    spell: list[int] = [10, 20, 30, 40]
    print("Sum:", spell_reducer(spell, "add"))
    print("Product:", spell_reducer(spell, "multiply"))
    print("Max:", spell_reducer(spell, "max"))
    print()
    print("Testing memoized fibonacci...")
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))


if __name__ == "__main__":
    main()
