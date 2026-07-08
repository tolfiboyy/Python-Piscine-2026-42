#!/usr/bin/python3
from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, DefensiveStrategy, AggressiveStrategy, \
    BattleStrategy, InvalidStrategy

opponent = tuple[CreatureFactory, BattleStrategy]


def battle(opponents: list[opponent]) -> None:

    print("*** Huge Tournament !!! ***")
    print(f"So many opponents ! At least {len(opponents)} are involved !!!")

    creatures = []

    for factory, strategy in opponents:
        creature = factory.create_base()
        creatures.append((creature, strategy))

    for i in range(len(creatures)):
        for j in range(i + 1, len(creatures)):
            # giving the attributes of the list[tuple] to our differrent
            # creatures to make the fight
            creature1, strategy1 = creatures[i]
            creature2, strategy2 = creatures[j]

            print("\n* Battle *\n")
            print(creature1.describe_itself())
            print("* versus *")
            print(creature2.describe_itself())

            print("\n* Fight ! *\n")

            try:
                for line in strategy1.act(creature1):
                    print(line)
                for line in strategy2.act(creature2):
                    print(line)

            except InvalidStrategy as error:
                print(f"{error}, stopping the fight!")


def main() -> None:

    tournament_0 = [(FlameFactory(), NormalStrategy()),
                    (HealingCreatureFactory(), DefensiveStrategy())]

    print("//Tournament 0")
    battle(tournament_0)

    tournament_1 = [(AquaFactory(), NormalStrategy()),
                    (HealingCreatureFactory(), AggressiveStrategy())]

    print("\n//Tournament 1 voluntary error")
    battle(tournament_1)

    tournament_2 = [(AquaFactory(), NormalStrategy()),
                    (HealingCreatureFactory(), DefensiveStrategy()),
                    (TransformCreatureFactory(), AggressiveStrategy())]

    print("\n//Tournament 2")
    battle(tournament_2)

    print("\n=== END ===")


if __name__ == "__main__":
    main()
