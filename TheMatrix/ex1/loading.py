#!/usr/bin/env python3
import sys
from importlib import util
import importlib


modules: list = ["numpy", "pandas", "matplotlib"]


def get_version(name: str):
    module = importlib.import_module(name)
    return module.__version__


def find_spec(name: str):
    return util.find_spec(name)


def check_modules(modules: list):
    print("Checking dependencies...\n")

    missing_module = []

    for module in modules:
        if find_spec(module):
            try:
                print(f"[OK] {module} ({get_version(module)})")
            except ImportError:
                print(f"[BROKEN] {module} (missing dependency)")
                missing_module.append(module)
        else:
            print(f"[MISSING] {module}")
            missing_module.append(module)

    return missing_module


def generate_data() -> None:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as pl

    data = np.random.randint(0, 100, 10)

    data_sorted = np.sort(data)

    data_frame = pd.DataFrame(data_sorted)

    pl.plot(data_frame)

    pl.savefig("matrix_analysis.png")


def main() -> None:

    print("LOADING STATUS: Loading programs...\n")

    is_missing = check_modules(modules)

    if len(is_missing) > 0:
        print("\nA module is missing !")
        print("Please install the module package with:")
        print("pip install -r requirements.txt")
        print("Then go into your venv and run the program\n")
        print("or")
        print("\npoetry install")
        print("run: poetry run python loading.py")
        sys.exit(1)
    else:
        print("\nAnalyzing Matrix data...")
        print("Processing a thousand data points...")
        print("Generating your visualization...")

        generate_data()

        print("\nAnalysis complete !")
        print("Your results were saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
