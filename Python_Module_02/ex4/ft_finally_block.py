#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(
        self,
        message: str = "Unknown garden error"
    ) -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(
        self,
        message: str = "Unknown plant error"
    ) -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    valid_plants = ["Tomato", "Lettuce", "Carrots"]
    invalid_plants = ["Tomato", "lettuce"]

    print("=== Garden Watering System ===")

    print("\nTesting valid plants...")
    try:
        print("Opening watering system")
        for plant in valid_plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    finally:
        print("Closing watering system")

    print("\nTesting invalid plants...")
    try:
        print("Opening watering system")
        for plant in invalid_plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print("... ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    test_watering_system()
    print("\nCleanup always happens, even with errors!")
