#!/usr/bin/python3

import random

PLAYERS: list[str] = [
    "Thelma",
    "priyangan",
    "adrien",
    "Zelie",
    "Emma",
    "Adele",
    "tom"
]


def capitalize_dict(players: list[str]) -> list[str]:

    capitalized_players = [name.capitalize() for name in PLAYERS]

    return (capitalized_players)


def capitalized_only(players: list[str]) -> list[str]:

    capitalized_only = [name for name in PLAYERS if name == name.capitalize()]
    return (capitalized_only)


def assign_score(players: list[str]) -> dict[str, int]:
    score_dict = {name: random.randint(0, 1000) for name in players}
    return (score_dict)


def score_average(scores: dict[str, int]) -> float:
    total = sum(scores.values()) / len(scores)
    return (round(total, 2))


def highest_scores(scores: dict[str, int], average: float) -> dict[str, int]:
    highest = {name: score for name,
               score in scores.items() if score > average}
    return (highest)


def main() -> None:
    print("=== Game Data Alchemist ===\n")

    print("Initial list of players: ", PLAYERS)

    print()

    capitalized = capitalize_dict(PLAYERS)
    print("New list of all players names but capitalized: ", capitalized)

    print()

    only_capitalized = capitalized_only(PLAYERS)
    print("New list of only capitalized names: ", only_capitalized)

    print()

    scores = assign_score(capitalized)
    print("Score dict: ", scores)

    print()

    average = score_average(scores)
    print("Average score: ", average)

    print()

    highest = highest_scores(scores, average)
    print("High scores: ", highest)

    print()

    print("=== End ===")


if __name__ == "__main__":
    main()
