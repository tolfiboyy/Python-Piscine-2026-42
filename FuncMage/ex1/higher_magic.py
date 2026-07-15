from typing import Callable


def create_spell() -> Callable:
    def spell(target: str, power: int) -> str:
        return (f"{target} gets {power} power")

    return spell


def create_heal() -> Callable:
    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    return heal


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        return (
            spell1(target, power),
            spell2(target, power)
            )

    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplified


def enough_power(target: str, power: int) -> bool:
    return power >= 200


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(target: str, power: int):
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell Fizzled"

    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def casting_spells(target: str, power: int):
        results = []

        for spell in spells:
            results.append(spell(target, power))

        return results

    return casting_spells


def main() -> None:
    # Spell combiner testing
    print("Testing spell combiner...")
    spell1 = create_spell()
    spell2 = create_heal()

    combined = spell_combiner(spell1, spell2)

    result = combined("Gordon", 56)

    print(f"Combined spell result: {result[0]}, {result[1]}\n")

    # Spell amplifier testing
    print("Testing spell amplifier...")

    orb = create_spell()
    amplified_orb = power_amplifier(orb, 2)

    original = orb("Orb", 115)
    amplified = amplified_orb("Maxi Orb", 115)

    print(f"Original spell: {original}")
    print(f"Amplified spell: {amplified}")

    # Conditional caster testing...
    print("\nConditional caster testing...")

    caster_spell = conditional_caster(enough_power, orb)

    print("Testing with a spell that does not meet the minimum power (< 200)")
    print(f"{caster_spell("Orb", 199)}\n")

    print("Testing with a spell that meets the minimum power (>= 200)")
    print(f"{caster_spell("Orb", 250)}")

    # Testing spell_sequence

    print("\nTesting spell_sequence...")
    spell_list = [spell1, spell2]

    sequence = spell_sequence(spell_list)

    print(f"List of spells: {sequence("HeadCrab", 89)}")


if __name__ == "__main__":
    main()
