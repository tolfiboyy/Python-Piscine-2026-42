#!/usr/bin/python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error"):
        super().__init__(message)


def check_plant() -> None:
    raise PlantError("The tomato plant is wilting!")


def check_water() -> None:
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        check_plant()
    except PlantError as error:
        print(f"Caught PlantError: {error}\n")

    print("Testing WaterError...")
    try:
        check_water()
    except WaterError as error:
        print(f"Caught WaterError: {error}\n")

    print("Testing catching all garden errors...")

    try:
        check_plant()
    except PlantError as error:
        print(f"Caught GardenError: {error}")

    try:
        check_water()
    except WaterError as error:
        print(f"Caught GardenError: {error}\n")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
