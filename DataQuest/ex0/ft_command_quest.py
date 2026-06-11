#!/usr/bin/python3
import sys


def display() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")

    if (len(sys.argv) == 1):
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(sys.argv)}")

        i = 1

        while i < len(sys.argv):
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1

    print(f"Total arguments: {len(sys.argv)}")


def main() -> None:
    display()


if __name__ == "__main__":
    main()
