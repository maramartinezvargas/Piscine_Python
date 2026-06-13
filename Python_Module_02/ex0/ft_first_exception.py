#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print()

    temps = ["25", "abc"]
    for temp_str in temps:
        print(f"Input data is '{temp_str}'")
        try:
            temp = input_temperature(temp_str)
            print(f"Temperature is now {temp}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")

        print()

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
