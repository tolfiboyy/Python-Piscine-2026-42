#!/usr/bin/python3
import sys


def print_stats(scores: list[int]) -> None:
    total = sum(scores)
    average = total / len(scores)
    highest = max(scores)
    lowest = min(scores)

    print(f"Total players: {len(scores)}")
    print(f"Total score: {total}")
    print(f"Average score: {average}")
    print(f"High score: {highest}")
    print(f"Low score: {lowest}")
    print(f"Score range: {highest - lowest}")


def print_score(scores: list[int]) -> None:
    print("Scores processed:", end=" ")
    print(scores)


def check_args() -> list[int]:

    scores: list[int] = []

    for arg in sys.argv[1:]:
        try:
            score = int(arg)
            scores = scores + [score]
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    return (scores)


def main() -> None:
    print("=== Player Score Analytics ===")
    scores = check_args()
    if len(scores) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
        return
    if len(scores) > 0:
        print_score(scores)
        print_stats(scores)


if __name__ == "__main__":
    main()
