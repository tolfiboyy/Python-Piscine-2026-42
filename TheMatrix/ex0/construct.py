#!/usr/bin/env python3
import os
import sys
import site


def am_i_in_the_matrix() -> bool:
    return sys.prefix != sys.base_prefix


def main() -> None:

    path_of_python = sys.executable
    environment_path = sys.prefix
    environment_name = os.path.basename(environment_path)

    print(f"\n{sys.prefix}\n")
    print(f"\nbase: {sys.base_prefix}\n")

    if am_i_in_the_matrix() is True:
        print("MATRIX STATUS: Welcome to the construct\n")

        print("Current Python: ", path_of_python)
        print("Virtual Environment: ", environment_name)
        print("Environment path: ", environment_path)

        print("SUCCESS: You’re in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the outside world.\n")

        print("Package installation path:")
        print(site.getsitepackages()[0])

    else:
        print("MATRIX STATUS: You’re still plugged in\n")

        print("Current Python: ", path_of_python)
        print("Virtual Environment: None detected\n")

        print("WARNING: You’re in the global environment!")
        print("The machines can see everything you install.\n")

        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")
        print("(But we're not using windows)\n")

        print("Then try running this program again using ./construct.py")


if __name__ == "__main__":
    main()
