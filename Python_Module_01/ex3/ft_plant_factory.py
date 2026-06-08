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


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25.0, 30)
    oak = Plant("Oak", 200.0, 365)
    cactus = Plant("Cactus", 5.0, 90)
    sunflower = Plant("Sunflower", 80.0, 45)
    fern = Plant("Fern", 15.0, 120)

    plants = [rose, oak, cactus, sunflower, fern]

    for plant in plants:
        print("Created: ", end="")
        plant.show()
