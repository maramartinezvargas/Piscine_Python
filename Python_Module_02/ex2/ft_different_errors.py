#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "text" + 5
    else:
        print("Operation completed successfully")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
        except ValueError as ve:
            print(f"Caught ValueError: {ve}")
        except ZeroDivisionError as zde:
            print(f"Caught ZeroDivisionError: {zde}")
        except FileNotFoundError as fnfe:
            print(f"Caught FileNotFoundError: {fnfe}")
        except TypeError as te:
            print(f"Caught TypeError: {te}")

    print("\nTesting multiple exception catch...")
    for i in (0, 1):
        try:
            garden_operations(i)
        except (ValueError, ZeroDivisionError) as e:
            print(f"Caught multiple exception types: {e}")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
