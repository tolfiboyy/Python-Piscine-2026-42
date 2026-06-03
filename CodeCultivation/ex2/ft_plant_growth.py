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


def ft_plant_growth() -> None:
    plant = Plant("Edelweiss", 8.0, 1, 0.8)
    start_height = plant.height
    print("=== Garden Plant Growth ===")
    plant.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")

        plant.grow()
        plant.age()

        plant.show()

    total_growth = plant.height - start_height
    print(f"Growth this week: {round(total_growth, 1)}cm")


if __name__ == "__main__":
    ft_plant_growth()
