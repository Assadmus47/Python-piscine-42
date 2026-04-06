from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from collections.abc import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    operations = {
        "add": add,
        "multiply": mul,
        "max": lambda a, b: a if a > b else b,
        "min": lambda a, b: a if a < b else b
    }
    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")
    return reduce(operations[operation], spells)


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
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    @singledispatch
    def cast_spell(arg):
        return "Unknown spell type"

    @cast_spell.register(int)
    def _(arg):
        return f"Damage spell: {arg} damage"

    @cast_spell.register(str)
    def _(arg):
        return f"Enchantment: {arg}"

    @cast_spell.register(list)
    def _(arg):
        return f"Multi-cast: {len(arg)} spells"

    return cast_spell


def main() -> None:
    print("Testing spell reducer...")
    spell: list[int] = [10, 20, 30, 40]
    print("Sum:", spell_reducer(spell, "add"))
    print("Product:", spell_reducer(spell, "multiply"))
    print("Max:", spell_reducer(spell, "max"))

    print()
    print("Testing partial enchanter...")

    enchanters = partial_enchanter(
        lambda power, element, target:
        f"{element} enchantment on {target} with power {power}"
    )
    print(enchanters['fire_enchant'](target="Sword"))
    print(enchanters['ice_enchant'](target="Shield"))
    print(enchanters['lightning_enchant'](target="Staff"))

    print()
    print("Testing memoized fibonacci...")
    print("Fib(0):", memoized_fibonacci(0))
    print("Fib(1):", memoized_fibonacci(1))
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))

    print()
    print("Testing spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher(["fire", "ice", "lightning"]))
    print(dispatcher(3.14))


if __name__ == "__main__":
    main()
