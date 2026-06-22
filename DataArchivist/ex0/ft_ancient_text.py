#!/usr/bin/python3

import sys


def open_file(file_name: str) -> None:

    try:
        file = open(file_name)
        content = file.read()
        print("---\n")
        print(content)
        print("---\n")

    except Exception as error:
        print(f"Error opening your file '{file_name}': "
              f"{error}")
        return

    file.close()
    print(f"File '{file_name}' closed.")


def main() -> None:

    if (len(sys.argv) != 2):
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery ===\n")
    print(f"Accessing file '{sys.argv[1]}'\n")
    open_file(sys.argv[1])


if __name__ == "__main__":
    main()
