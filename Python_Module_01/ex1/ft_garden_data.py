#!/usr/bin/env python3

class Plant:
    name: str
    height: int
    age: int

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_garden_data() -> None:
    print("=== Garden Plant Registry ===")

    rose = Plant()
    rose.name = "Rose"
    rose.height = 30
    rose.age = 30

    sunflower = Plant()
    sunflower.name = "Sunflower"
    sunflower.height = 150
    sunflower.age = 60

    cactus = Plant()
    cactus.name = "Cactus"
    cactus.height = 15
    cactus.age = 120

    plants = [rose, sunflower, cactus]

    for plant in plants:
        plant.show()


if __name__ == "__main__":
    ft_garden_data()
