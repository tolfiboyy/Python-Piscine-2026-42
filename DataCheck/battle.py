#!/usr/bin/python3
from ex0 import AquaFactory, CreatureFactory, FlameFactory


def testing_factory(factory: CreatureFactory, type: str) -> None:
    print("=== Testing factory ===\n")
    print(f"{type} creatures:")

    base_creature = factory.create_base()
    print(base_creature.describe_itself())
    print(base_creature.attack())

    print()

    evolved_creature = factory.create_evolved()
    print(evolved_creature.describe_itself())
    print(evolved_creature.attack())

    print()


def battle(water_factory: CreatureFactory, fire_factory: CreatureFactory):
    evolved_aqua = water_factory.create_evolved()
    base_fire = fire_factory.create_base()

    print("=== Battle time ! ===")

    print(base_fire.describe_itself())
    print(".vs")
    print(evolved_aqua.describe_itself())

    print("\n=== Fight ! ===")

    print(base_fire.attack())
    print(evolved_aqua.attack())

    print("\nTorragon wins easily !")


if __name__ == "__main__":

    fire_factory = FlameFactory()
    testing_factory(fire_factory, "Fire")

    water_factory = AquaFactory()
    testing_factory(water_factory, "Water")

    battle(water_factory, fire_factory)
