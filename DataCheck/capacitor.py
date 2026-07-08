#!/usr/bin/python3
from ex1 import HealingCreatureFactory, TransformCreatureFactory


def testing_healing(factory: HealingCreatureFactory) -> None:
    print("=== Testing creatures with healing capacities ===")

    print("Basic healer: ")
    base_healer = factory.create_base()
    print(base_healer.describe_itself())
    print(base_healer.attack())
    print(base_healer.heal())

    print("\nEvolved:\n")
    evolved_healer = factory.create_evolved()
    print(evolved_healer.describe_itself())
    print(evolved_healer.attack())
    print(evolved_healer.heal())


def testing_transform(factory: TransformCreatureFactory) -> None:
    print("=== Testing creatures with transforming capabalities ===")

    print("Basic transformer: ")
    base_transformer = factory.create_base()
    print(base_transformer.describe_itself())
    print(base_transformer.attack())
    print(base_transformer.transform())
    print(base_transformer.attack())
    print(base_transformer.revert())

    print("\nEvolved:\n")
    evolved_transformer = factory.create_evolved()
    print(evolved_transformer.describe_itself())
    print(evolved_transformer.attack())
    print(evolved_transformer.transform())
    print(evolved_transformer.attack())
    print(evolved_transformer.revert())


if __name__ == "__main__":

    healing_factory = HealingCreatureFactory()

    testing_healing(healing_factory)

    print()

    transform_factory = TransformCreatureFactory()

    testing_transform(transform_factory)
