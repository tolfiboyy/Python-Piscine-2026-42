class Plant:
    def __init__(jar, name: str, height: float, plant_age: int,
                 growth_rate: float):
        jar.name = name
        jar.height = height
        jar.plant_age = plant_age
        jar.growth_rate = growth_rate

    def show(jar) -> None:
        print(f"{jar.name}: {round(jar.height, 1)}cm, "
              f"{jar.plant_age} days old")

    def grow(jar) -> None:
        jar.height = jar.height + jar.growth_rate

    def age(jar) -> None:
        jar.plant_age = jar.plant_age + 1


def ft_plant_factory() -> None:
    plants = [
        Plant("Edelweiss", 8.0, 1, 0.8),
        Plant("Hibiscus", 16.0, 5, 0.2),
        Plant("Tulip", 12.0, 10, 0.3),
        Plant("Lily", 21.0, 12, 0.4),
        Plant("Violet", 1.0, 120, 1.5)
        ]

    for plant in plants:
        print("Created:", end=" ")
        plant.show()


if __name__ == "__main__":
    ft_plant_factory()
