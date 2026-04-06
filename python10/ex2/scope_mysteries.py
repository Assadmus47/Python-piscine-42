
from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0

    def incremente():
        nonlocal count
        count += 1
        return count
    return incremente


def spell_accumulator(initial_power: int) -> Callable:
    count = initial_power

    def accumulator(amount: int):
        nonlocal count
        count += amount
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
    counter_a: Callable = mage_counter()
    counter_b: Callable = mage_counter()
    print("counter_a call 1:", counter_a())
    print("counter_a call 2:", counter_a())
    print("counter_b call 1:", counter_b())

    print()
    print("Testing spell accumulator...")
    acc = spell_accumulator(100)
    print("Base 100, add 20:", acc(20))
    print("Base 100, add 30:", acc(30))

    print()
    print("Testing enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print()
    print("Testing memory vault...")
    vault = memory_vault()
    vault['store']('secret', 42)
    print("Store 'secret' = 42")
    print("Recall 'secret':", vault['recall']('secret'))
    print("Recall 'unknown':", vault['recall']('unknown'))


if __name__ == "__main__":
    main()
