
from typing import Callable


def mage_counter() -> Callable:
    count = 0

    def incremente(*args):
        nonlocal count
        count += 1
        return count
    return incremente


def spell_accumulator(initial_power):
    count = initial_power

    def accumulator(*args):
        nonlocal count
        count += args[0]
        return count
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchantment(item):
        return enchantment_type + " " + item
    return enchantment


def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key, value):
        memory[key] = value

    def recall(key):
        value = memory.get(key)
        if value is None:
            return "Memory not found"
        return value

    return {'store': store, 'recall': recall}


def main() -> None:
    print("Testing mage counter...")
    increment: Callable = mage_counter()
    print("Call 1:", increment())
    print("Call 2:", increment())
    print("Call 3:", increment())
    print()
    print("Testing enchantment factory...")
    enchantment: Callable = enchantment_factory("Flaming")
    print(enchantment("Sword"))
    enchantment = enchantment_factory("Frozen")
    print(enchantment("Shield"))


if __name__ == "__main__":
    main()
