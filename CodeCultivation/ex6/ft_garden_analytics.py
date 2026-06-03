class Plant:
    class Statistics:
        def __init__(self):
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def show(self) -> None:
            print(f"Stats: {self.grow_calls} grow, {self.age_calls} age, "
                  f"{self.show_calls} show")

    def __init__(self, name: str, height: float, plant_age: int):
        self.name = name
        self._height = height
        self._plant_age = plant_age
        self.stats = Plant.Statistics()

    def show(self) -> None:
        self.stats.show_calls += 1
        print(f"{self.name}: {round(self._height, 1)}cm, "
              f"{self._plant_age} days old")

    def age(self, days: int) -> None:
        self.stats.age_calls += 1
        self._plant_age += days

    def grow(self, growth: float) -> None:
        self.stats.grow_calls += 1
        self._height += growth

    @staticmethod
    def check_year_old(days: int) -> bool:
        return days > 365

    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, plant_age: int, color: str):
        super().__init__(name, height, plant_age)

        self.color = color
        self.has_bloomed = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if (self.has_bloomed is False):
            print(f"{self.name} has not bloomed yet")
            self.has_bloomed = True
        elif (self.has_bloomed is True):
            print(f"{self.name} is blooming beautifully!")

    def bloom(self) -> None:
        self.has_bloomed = True


class Tree(Plant):
    class Tree_Statistics(Plant.Statistics):
        def __init__(self):
            super().__init__()
            self.shade_calls = 0

        def show(self) -> None:
            super().show()
            print(f"{self.shade_calls} shade")

    def __init__(self, name: str, height: float, plant_age: int,
                 trunk_diameter: float):
        super().__init__(name, height, plant_age)

        self.trunk_diameter = trunk_diameter
        self.shade_status = False
        self.stats: Tree.Tree_Statistics = Tree.Tree_Statistics()

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        self.stats.shade_calls += 1
        if (self.shade_status is False):
            print(f"[asking the {self.name} to produce shade]")
            print(f"Tree {self.name} now produces a shade of "
                  f"{self._height}cm long and {self.trunk_diameter}cm wide.")
            self.shade_status = True
        elif (self.shade_status is True):
            print(f"Tree {self.name} is already producing shade!")


class Seed(Flower):
    def __init__(self, name: str, height: float, plant_age: int, color: str):
        super().__init__(name, height, plant_age, color)
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


def statistics_show(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.stats.show()


def ft_plant_type() -> None:
    tree = Tree("Oak", 200.0, 365, 5.0)
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.check_year_old(30)}")
    print(f"Is 400 days more than a year? -> {Plant.check_year_old(400)}")

    print()

    print("=== Flower")
    flower = Flower("Rose", 15.0, 10, "Red")
    flower.show()
    flower.bloom()
    statistics_show(flower)
    print(f"[asking the {flower.name} to grow and bloom]")
    flower.grow(8.0)
    flower.show()
    flower.bloom()
    statistics_show(flower)

    print()

    print("=== Tree")
    tree.show()
    statistics_show(tree)
    tree.produce_shade()
    statistics_show(tree)

    print()

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "Yellow")
    sunflower.show()
    print(f"[make {sunflower.name} grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    statistics_show(sunflower)

    print()

    print("=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    statistics_show(unknown)


if __name__ == "__main__":
    ft_plant_type()
