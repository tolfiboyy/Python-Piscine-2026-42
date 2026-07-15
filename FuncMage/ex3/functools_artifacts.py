from operator import add, mul
from functools import reduce, lru_cache, singledispatch
from typing import Callable, Any

SPELLS = [15, 20, 25, 30]


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    if operation == "add":
        return reduce(add, spells)

    elif operation == "mul":
        return reduce(mul, spells)

    elif operation == "min":
        return reduce(min, spells)

    elif operation == "max":
        return reduce(max, spells)

    raise ValueError("Unknown operation")


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    # print(memoized_fibonacci.cache_info())
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def infer(spell: Any) -> str:
        return "Unknown spell type"

    @infer.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @infer.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @infer.register(list)
    def _(spell: list[Any]) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return infer


def main() -> None:
    # Spell reducer
    print("Testing spell reducer...")

    try:
        print("Add: ", spell_reducer(SPELLS, "add"))
        print("Product: ", spell_reducer(SPELLS, "mul"))
        print("Min: ", spell_reducer(SPELLS, "min"))
        print("Max: ", spell_reducer(SPELLS, "max"))
        print("test: ", spell_reducer(SPELLS, "unknown"))
    except ValueError as error:
        print("Expected error: ", error)

    # fibonacci but memorized
    print("\nTesting memoized fibonacci...")
    print("Fib(0): ", memoized_fibonacci(0))
    print("Fib(1): ", memoized_fibonacci(1))
    print("Fib(10): ", memoized_fibonacci(10))
    print("Fib(15): ", memoized_fibonacci(15))

    # spell dispatcher that will infer which function to use
    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()

    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher(SPELLS))
    print(dispatcher({"test": 15}))


if __name__ == "__main__":
    main()
