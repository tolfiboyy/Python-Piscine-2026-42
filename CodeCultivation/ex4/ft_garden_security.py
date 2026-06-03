class Plant:
    def __init__(jar, name: str, height: float, plant_age: int):
        jar.name = name
        jar._height = 0.0
        jar._plant_age = 0

        jar.set_height(height)
        jar.set_age(plant_age)

    def show(jar) -> None:
        print(f"{jar.name}: {round(jar._height, 1)}cm, "
              f"{jar._plant_age} days old")

    def age(jar) -> None:
        jar._plant_age = jar._plant_age + 1

    def set_height(jar, height: float) -> None:
        if (height < 0):
            print(f"{jar.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            jar._height = height
            print(f"Height updated: {jar._height}")

    def set_age(jar, age: int) -> None:
        if (age < 0):
            print(f"{jar.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            jar._plant_age = age
            print(f"Age updated: {jar._plant_age}")

    def get_height(jar) -> float:
        return jar._height

    def get_age(jar) -> int:
        return jar._plant_age


def ft_garden_security() -> None:
    print("=== Garden Security System ===")

    edelweiss = Plant("Edelweiss", 15.0, 5)

    print("Plant created: ", end=" ")
    edelweiss.show()

    print()

    edelweiss.set_height(25.0)
    edelweiss.set_age(10)

    print()

    edelweiss.set_height(-5)
    edelweiss.set_age(-15)

    print()

    print("Current state", end=" ")
    edelweiss.show()


if __name__ == "__main__":
    ft_garden_security()
