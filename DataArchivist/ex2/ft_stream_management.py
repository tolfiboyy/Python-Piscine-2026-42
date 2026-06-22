#!/usr/bin/python3

import sys


def open_file(file_name: str) -> None:

    try:
        file = open(file_name)
        content = file.read()
        print("---\n")
        print(content)
        print("---\n")

        file.close()
        print(f"File '{file_name}' closed.\n")

        print("Transform data:")
        print("---\n")

        lines_stripped = content.splitlines()
        new_content = ""

        for line in lines_stripped:
            new_content += line + "#\n"

        print(new_content)
        print("---\n")

        print("Enter a new file name or type entry: ", end="")
        sys.stdout.flush()

        new_file_name = sys.stdin.readline()
        new_file_name = new_file_name.strip()

        if new_file_name == "":
            print("It's your choice ! Not saving data.")
            return

        try:
            print()
            print(f"Saving data to '{new_file_name}'\n")

            write_file = open(new_file_name, "w")
            write_file.write(new_content)
            write_file.close()

            print(f"Data saved to '{new_file_name}', closing file.")

        except Exception as error:
            print(f"[STDERR] Error saving file: "
                  f"{new_file_name}: {error}", file=sys.stderr)
            print("Data not saved !")

    except Exception as error:
        print(f"Error opening your file '{file_name}': "
              f"{error}", file=sys.stderr)
        return


def main() -> None:

    if (len(sys.argv) != 2):
        print("Usage: ft_archive_creation.py <file>")
        return

    print("=== Cyber Archives Recovery & Preservation ===\n")
    print(f"Accessing file '{sys.argv[1]}'\n")

    open_file(sys.argv[1])


if __name__ == "__main__":
    main()
