from typing import Callable


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    totalpower = initial_power

    def accumulator(amount: int) -> int:
        nonlocal totalpower
        totalpower += amount
        return totalpower
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def adding_enchantment(item_name: str):
        return f"{enchantment_type} {item_name}"
    return adding_enchantment


def memory_vault() -> dict[str, Callable]:
    memory: dict[str, object] = {}

    def store(key: str, value: object):
        memory[key] = value

    def recall(key: str):
        return memory.get(key, "Memory not found")

    return {
            "store": store,
            "recall": recall
            }


def main():
    # testing mage counter

    print("Testing mage counter ...")
    count_a = mage_counter()
    count_b = mage_counter()

    print(f"counter_a call: {count_a()}")
    print(f"counter_a call: {count_a()}")
    print(f"counter_b call: {count_b()}")

    # testing spell accumulator
    print("\nTesting spell accumulator...")
    adding_power = spell_accumulator(100)

    print(f"Base 100, add 20: {adding_power(20)}")
    print(f"Base 100, add 30: {adding_power(30)}")

    # Testing enchantment factory
    print("\nTesting enchantment factory...")
    item1 = enchantment_factory("Flaming")
    item2 = enchantment_factory("Frozen")

    print(item1("Sword"))
    print(item2("Shield"))

    # memory vault testing

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault["store"]("secret", 42)

    print("Storing 'Secret' = 42")
    print(f"Recall 'Secret' = {vault["recall"]("secret")}")
    print(f"Recall 'Unknown': {vault["recall"]("unknown")}")


if __name__ == "__main__":
    main()
