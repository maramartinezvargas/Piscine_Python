#!/usr/bin/env python3

class Plant:
    """Representing a plant in the garden that grows and ages over time"""
    name: str
    _height: float
    _days_old: int
    _stats: "_Statistics"

    class _Statistics:
        """Subclass to track growth, age, and show counts for the plant"""
        grow: int
        age: int
        show: int

        def __init__(self) -> None:
            self.grow = 0
            self.age = 0
            self.show = 0

        def show_statistics(self) -> None:
            print(f"Stats: {self.grow} grow, {self.age} age, {self.show} show")

    def __init__(self, name: str, height: float, days_old: int) -> None:
        """Initialize a new plant with the given name, height, and age in days
        If height or age is negative, print an error message and set the value
        to 0"""
        self.name = name
        self._height = 0.0
        self._days_old = 0
        self._stats = self._Statistics()

        if height < 0:
            print(f"{name}: Error, height can't be negative\n"
                  f"Height update rejected")
        else:
            self._height = height

        if days_old < 0:
            print(f"{name}: Error, age can't be negative\n"
                  f"Age update rejected")
        else:
            self._days_old = days_old

    def show(self) -> None:
        self._stats.show += 1
        print(f"{self.name}: {self._height:.1f}cm, {self._days_old} days old")

    def grow(self) -> None:
        """Simulate the growth of the plant for one day"""
        self._stats.grow += 1
        self._height += 8.0

    def age(self) -> None:
        """Simulate the aging of the plant for one day"""
        self._stats.age += 1
        self._days_old += 1

    @staticmethod
    def is_older(age: int) -> bool:
        """Check if the plant is older than one year (365 days)"""
        return age > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        """Create an anonymous plant with default values"""
        return cls("Unknown plant", 0.0, 0)

    def get_height(self) -> float:
        """Return the current height of the plant"""
        return self._height

    def get_age(self) -> int:
        """Return the current age of the plant in days"""
        return self._days_old

    def set_height(self, new_height: float) -> None:
        """Set the height of the plant to a new value"""
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative\n"
                  f"Height update rejected")
            return
        self._height = new_height
        print(f"Height updated: {int(self._height)}cm")

    def set_age(self, new_age: int) -> None:
        """Set the age of the plant to a new value in days"""
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative\n"
                  f"Age update rejected")
            return
        self._days_old = new_age
        print(f"Age updated: {self._days_old} days")

    def show_statistics(self) -> None:
        """Show the growth, age, and show counts for the plant"""
        self._stats.show_statistics()


class Flower(Plant):
    """Representing a flower in the garden that has a color attribute"""
    color: str
    is_blooming: bool

    def __init__(self, name: str, height: float, days_old: int,
                 color: str) -> None:
        super().__init__(name, height, days_old)
        self.color = color
        self.is_blooming = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.is_blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")

    def bloom(self) -> None:
        """Simulate the blooming of the flower"""
        self.is_blooming = True


class Seed(Flower):
    """Representing a seed in the garden that can grow into a flower"""
    def __init__(self, name: str, height: float, days_old: int,
                 color: str) -> None:
        super().__init__(name, height, days_old, color)
        self.seeds = 0

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")

    def grow(self) -> None:
        """Simulate the growth of the seed for one day and update its height"""
        self._height += 30.0
        self._stats.grow += 1

    def age(self) -> None:
        """Simulate the aging of the seed for one day
        and update its age in days"""
        self._days_old += 20
        self._stats.age += 1

    def bloom(self) -> None:
        """Simulate the blooming of the seed and produce seeds"""
        super().bloom()
        self.seeds += 42


class Tree(Plant):
    """Representing a tree in the garden that has a trunk diameter attribute"""
    trunk_diameter: float
    shade_calls: int

    def __init__(self, name: str, height: float, days_old: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, days_old)
        self.trunk_diameter = trunk_diameter
        self.shade_calls = 0

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        """Simulate the tree producing shade and track the shade call count"""
        self.shade_calls += 1
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.get_height():.1f}cm long and "
            f"{self.trunk_diameter:.1f}cm wide."
        )

    def show_statistics(self) -> None:
        """Show the growth, age, and show counts for the tree"""
        super().show_statistics()
        print(f"{self.shade_calls} shade")


class Vegetable(Plant):
    """Representing a vegetable in the garden that has a harvest season
    and nutritional value attributes"""
    harvest_season: str
    nutritional_value: int

    def __init__(self, name: str, height: float, days_old: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, days_old)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def grow(self) -> None:
        """Simulate the growth of the vegetable for one day and update its
        nutritional value"""
        self._height += 2.1
        self.nutritional_value += 1
        self._stats.grow += 1

    def age(self) -> None:
        """Simulate the aging of the vegetable for one day and update its
        nutritional value"""
        super().age()
        self.nutritional_value += 1


def show_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.show_statistics()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old ===")
    age1 = 30
    age2 = 400
    print(f"Is {age1} days more than a year? -> "
          f"{Plant.is_older(age1)}")
    print(f"Is {age2} days more than a year? -> "
          f"{Plant.is_older(age2)}")

    print()
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print(f"[statistics for {rose.name}]")
    rose.show_statistics()
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    show_stats(rose)

    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print(f"[statistics for {oak.name}]")
    oak.show_statistics()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    show_stats(oak)

    print()
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    show_stats(sunflower)

    print()
    print("=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    show_stats(unknown)
