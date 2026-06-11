#!/usr/bin/python3

import random

ALL_ACHIEVEMENTS: list[str] = [
    "First Steps",
    "Half Million",
    "Wheelie Rider",
    "Walk Free",
    "Chain Reaction",
    "The Lost Boy",
    "Catch The Bus",
    "Pool Shark",
    "Welcome to Liberty City",
    "Gracefully taken"
]


def gen_player_achievements() -> set[str]:

    achievements: set[str] = set()

    assign = random.randint(3, 8)

    while len(achievements) < assign:
        achievement = random.choice(ALL_ACHIEVEMENTS)
        achievements = achievements.union({achievement})

    return achievements


def show_players(adrien: set[str],
                 thelma: set[str],
                 priyangan: set[str],
                 zelie: set[str]) -> None:

    # print players and their success/achievements

    print("Player Adrien: ", adrien)
    print("Player Thelma: ", thelma)
    print("Player Priyangan: ", priyangan)
    print("Player Zelie: ", zelie)

    # print distinct

    print()

    all_distinct = adrien.union(thelma)
    all_distinct = all_distinct.union(priyangan)
    all_distinct = all_distinct.union(zelie)

    print("All distinct achievements: ", all_distinct)

    print()

    # print common

    common = adrien.intersection(thelma)
    common = common.intersection(priyangan)
    common = common.intersection(zelie)

    if common:
        print("Common achievements: ", common)
    else:
        print("No common achievements")


def only_has(adrien: set[str],
             thelma: set[str],
             priyangan: set[str],
             zelie: set[str]) -> None:

    # print player only has

    others = thelma.union(priyangan)
    others = others.union(zelie)

    only_adrien = adrien.difference(others)

    others = adrien.union(priyangan)
    others = others.union(zelie)

    only_thelma = thelma.difference(others)

    others = adrien.union(thelma)
    others = others.union(zelie)

    only_priyangan = priyangan.difference(others)

    others = adrien.union(priyangan)
    others = others.union(thelma)

    only_zelie = zelie.difference(others)

    if only_adrien:
        print("Only Adrien has: ", only_adrien)
    else:
        print("Adrien has no unique achievements to himself!")

    if only_thelma:
        print("Only Thelma has: ", only_thelma)
    else:
        print("Thelma has no unique achievements to himself!")

    if only_priyangan:
        print("Only Priyangan has: ", only_priyangan)
    else:
        print("Priyangan has no unique achievements to himself!")

    if only_zelie:
        print("Only Zelie has: ", only_zelie)
    else:
        print("Zelie has no unique achievements to himself!")


def is_missing(adrien: set[str],
               thelma: set[str],
               priyangan: set[str],
               zelie: set[str]) -> None:

    all_achievements = set(ALL_ACHIEVEMENTS)

    missing_adrien = all_achievements.difference(adrien)
    missing_thelma = all_achievements.difference(thelma)
    missing_priyangan = all_achievements.difference(priyangan)
    missing_zelie = all_achievements.difference(zelie)

    print("Adrien is missing: ", missing_adrien)
    print("Thelma is missing: ", missing_thelma)
    print("Priyangan is missing: ", missing_priyangan)
    print("Zelie is missing: ", missing_zelie)


def main() -> None:

    print("=== Achievement Tracker System ===\n")

    adrien = gen_player_achievements()
    thelma = gen_player_achievements()
    priyangan = gen_player_achievements()
    zelie = gen_player_achievements()

    show_players(adrien, thelma, priyangan, zelie)

    print()

    only_has(adrien, thelma, priyangan, zelie)

    print()

    is_missing(adrien, thelma, priyangan, zelie)

    print("\n=== End ===")


if __name__ == "__main__":
    main()
