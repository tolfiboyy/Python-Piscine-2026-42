class Plant:
    def __init__(jar, name: str, height: float, plant_age: int):
        jar.name = name
        jar._height = height
        jar._plant_age = plant_age

    def show(jar) -> None:
        print(f"{jar.name}: {round(jar._height, 1)}cm, "
              f"{jar._plant_age} days old")

    def age(jar) -> None:
        jar._plant_age += 1


class Flower(Plant):
    def __init__(jar, name: str, height: float, plant_age: int, color: str):
        super().__init__(name, height, plant_age)

        jar.color = color
        jar.has_bloomed = False

    def show(jar) -> None:
        super().show()
        print(f"Color: {jar.color}")

    def bloom(jar) -> None:
        if (jar.has_bloomed is False):
            print(f"{jar.name} has not bloomed yet")
            print(f"[asking the {jar.name} to bloom]")
            jar.has_bloomed = True
        elif (jar.has_bloomed is True):
            print(f"{jar.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(jar, name: str, height: float, plant_age: int,
                 trunk_diameter: float):
        super().__init__(name, height, plant_age)

        jar.trunk_diameter = trunk_diameter
        jar.shade_status = False

    def show(jar) -> None:
        super().show()
        print(f"Trunk diameter: {jar.trunk_diameter}cm")

    def produce_shade(jar) -> None:
        if (jar.shade_status is False):
            print(f"[asking the {jar.name} to produce shade]")
            print(f"Tree {jar.name} now produces a shade of "
                  f"{jar._height}cm long and {jar.trunk_diameter}cm wide.")
            jar.shade_status = True
        elif (jar.shade_status is True):
            print(f"Tree {jar.name} is already producing shade!")


class Vegetable(Plant):
    def __init__(jar, name: str, height: float, plant_age: int,
                 harvest_season: str, nutritional_value: int):
        super().__init__(name, height, plant_age)

        jar.harvest_season = harvest_season
        jar.nutritional_value = nutritional_value

    def show(jar) -> None:
        super().show()
        print(f"Harvest season: {jar.harvest_season}")
        print(f"Nutritional value: {jar.nutritional_value}")

    def grow(jar, growth: float, days: int) -> None:
        print(f"[make {jar.name} grow and age for {days} days]")
        jar._height += days * growth
        jar._plant_age += 20
        jar.nutritional_value += days


def ft_plant_type() -> None:
    flower = Flower("Rose", 15.0, 10, "Red")
    tree = Tree("Oak", 200.0, 365, 5.0)
    tomato = Vegetable("Tomato", 5.0, 10, "April", 0)
    print("=== Garden Plant Types ===")

    print("=== Flower")
    flower.show()
    flower.bloom()
    flower.show()
    flower.bloom()

    print()

    print("=== Tree")
    tree.show()
    tree.produce_shade()

    print()

    print("=== Vegetable")
    tomato.show()
    tomato.grow(2.1, 20)
    tomato.show()


if __name__ == "__main__":
    ft_plant_type()
