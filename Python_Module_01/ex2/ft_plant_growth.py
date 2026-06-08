#!/usr/bin/env python3

class Plant:
    """Representing a plant in the garden that grows and ages over time"""
    name: str
    height: float
    days_old: int

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.days_old} days old")

    def grow(self) -> None:
        """Simulate the growth of the plant for one day"""
        self.height += 0.8

    def age(self) -> None:
        """Simulate the aging of the plant for one day"""
        self.days_old += 1


if __name__ == "__main__":

    print("=== Garden Plant Growth ===")
    rose: Plant = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose.days_old = 30
    initial_height: float = rose.height
    rose.show()

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age()
        rose.show()

    growth = rose.height - initial_height
    print(f"Growth this week: {growth:.1f}cm")
