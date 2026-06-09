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
        if (new_height < 0):
            print(f"{self.name}: Error, height can't be negative\n"
                  f"Height update rejected")
            return
        self.height = new_height
        print(f"Height updated: {round(self.height)}cm")

    def set_age(self, new_age: int) -> None:
        """Set the age of the plant to a new value in days"""
        if (new_age < 0):
            print(f"{self.name}: Error, age can't be negative\n"
                  f"Age update rejected")
            return
        self.days_old = new_age
        print(f"Age updated: {self.days_old} days")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()

    print()
    rose.set_height(25.0)
    rose.set_age(30)

    print()
    rose.set_height(-5.0)
    rose.set_age(-3)

    print()
    print("Current state: ", end="")
    rose.show()
