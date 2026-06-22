#!/usr/bin/python3

def secure_archive(file_name: str, mode: str = "r",
                   content: str = "") -> tuple[bool, str]:
    try:
        if mode == "r":
            with open(file_name, mode) as file:
                file_content = file.read()

            return True, file_content

        elif mode == "w":
            with open(file_name, mode) as file:
                file.write(content)

            return True, "Content successfully written to file"

        else:
            return False, "Invalid mode choice"

    except Exception as error:
        return False, str(error)


def main() -> None:
    print("=== Cyber Archives Security ===\n")

    print("Using ’secure_archive’ to read from a nonexistent file:")
    return_value = secure_archive("/not/existing/file")
    print(return_value)

    print()

    print("Using ’secure_archive’ to read from an inaccessible file:")
    return_value = secure_archive("notaccessible.txt")
    print(return_value)

    print()

    print("Using ’secure_archive’ to read from a regular file:")
    return_value = secure_archive("accessible.txt")
    print(return_value)

    print()

    print("Using ’secure_archive’ to write previous content to a new file:")
    return_value = secure_archive("writethis.txt", "w", "REPLACED LOL")
    print(return_value)

    print()

    print("Trying to use the wrong mode:")
    return_value = secure_archive("writethis.txt", "x", "wrong anyway")
    print(return_value)

    print()
    print("=== End of program ===")


if __name__ == "__main__":
    main()
