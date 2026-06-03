class Plant:
    def __init__(jar, name: str, height: float, age: int) -> None:
        jar.name = name
        jar.height = height
        jar.age = age

    def show(jar) -> None:
        print(f"{jar.name}: {jar.height}cm, {jar.age} days old")


def ft_garden_data() -> None:
    print("=== Garden Plant Registry ===")

    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    rose.show()
    sunflower.show()
    cactus.show()


if __name__ == "__main__":
    ft_garden_data()
