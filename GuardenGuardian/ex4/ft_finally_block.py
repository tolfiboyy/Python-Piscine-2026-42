#!/usr/bin/python3

class PlantError(Exception):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


def water_the_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")

    print(f"Watering {plant_name}: [OK]")


def test_watering(plants: list[str]) -> None:
    print("Opening watering system")
    try:
        for plant in plants:
            water_the_plant(plant)

    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print(".. ending tests and returning to main")
        return

    finally:
        print("Closing watering system")


def main() -> None:
    print("=== Garden Watering System ===\n")

    print("Testing valid plants...")
    test_watering(["Tomato", "Lettuce", "Carrots"])

    print()

    print("Testing invalid plants...")
    test_watering(["Tomato", "lettuce", "Carrots"])

    print()

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
