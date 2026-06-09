#!/usr/bin/env python3

class Plant:
    """Representing a plant in the garden that grows and ages over time"""
    name: str
    height: float
    days_old: int

    def __init__(self, name: str, height: float, days_old: int) -> None:
        self.name = name
        self.height = height
        self.days_old = days_old

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.days_old} days old")

    def grow(self) -> None:
        """Simulate the growth of the plant for one day"""
        self.height += 0.8

    def age(self) -> None:
        """Simulate the aging of the plant for one day"""
        self.days_old += 1

    def get_height(self) -> float:
        """Return the current height of the plant"""
        return self.height

    def get_age(self) -> int:
        """Return the current age of the plant in days"""
        return self.days_old

    def set_height(self, new_height: float) -> None:
        """Set the height of the plant to a new value"""
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative\n"
                  f"Height update rejected")
            return
        self.height = new_height
        print(f"Height updated: {int(self.height)}cm")

    def set_age(self, new_age: int) -> None:
        """Set the age of the plant to a new value in days"""
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative\n"
                  f"Age update rejected")
            return
        self.days_old = new_age
        print(f"Age updated: {self.days_old} days")


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


class Tree(Plant):
    """Representing a tree in the garden that has a trunk diameter attribute"""
    trunk_diameter: float

    def __init__(self, name: str, height: float, days_old: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, days_old)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        """Simulate the tree producing shade"""
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height:.1f}cm long and "
            f"{self.trunk_diameter:.1f}cm wide."
        )


class Vegetable(Plant):
    """Representing a vegetable in the garden that has a harvest season and"
        "nutritional value attributes"""
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
        self.height += 2.1
        self.nutritional_value += 1

    def age(self) -> None:
        """Simulate the aging of the vegetable for one day and update its
        nutritional value"""
        super().age()
        self.nutritional_value += 1


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower ===")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("\n=== Tree ===")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("\n=== Vegetable ===")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.age()
        tomato.grow()
    tomato.show()
