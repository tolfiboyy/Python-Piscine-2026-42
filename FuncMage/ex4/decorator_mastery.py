from functools import wraps
from typing import Callable, Any
import time


def spell_timer(func: Callable) -> Callable:

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any):

        print(f"Casting {wrapper.__name__}...")

        start = time.time()

        result = func(*args, **kwargs)

        time.sleep(0.101)

        end = time.time() - start

        print(f"Spell completed in {end:.3f} seconds")

        return result

    return wrapper


def power_validator(min_power: int) -> Callable:

    def decorator(func: Callable):

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any):
            power = kwargs.get("power")

            if power is None:
                power = args[-1]

            if power >= min_power:
                return func(*args, **kwargs)

            return "Not enough power for this spell !"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:

    def decorator(func: Callable):

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any):

            index = 1
            for _ in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print("Spell failed, retrying... "
                          f"({index}/{max_attempts})")
                    index += 1

            return "Spell casting failed after trying maximum attempts !"

        return wrapper

    return decorator


@retry_spell(3)
def dupe_spell():
    raise "Error"


@retry_spell(3)
def valid_spell():
    return "Magic wand spits fire !"


@power_validator(10)
def fireball_cast(power: int):
    return f"Fireball cast! {power}"


@spell_timer
def fireball():
    return "Fireball cast!"


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c == " " for c in name)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:

    # spell timer
    print("Testing spell timer...")
    print(f"Result: {fireball()}")
    print("Casting without enough power:", fireball_cast(9))

    # Testing retrying spell
    print("\nTesting retrying spell...")

    print("Invalid spell:")
    print(dupe_spell())

    print("Valid spell:")
    print(valid_spell())

    # guild class
    print("\nTesting MageGuild...")
    mage = MageGuild()
    print("Valid mage name:", mage.validate_mage_name("Adrien"))
    print("Invalid mage name:", mage.validate_mage_name("Ad"))
    print(mage.cast_spell("Lightning", 15))
    print(mage.cast_spell("Lightning", 9))


if __name__ == "__main__":
    main()
