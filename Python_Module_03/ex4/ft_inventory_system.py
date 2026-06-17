#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    args: list[str] = sys.argv[1:]
    inventory: dict[str, int] = {}

    for item in args:
        parts = item.split(":")

        if len(parts) != 2:
            print(f"Error - invalid parameter '{item}'")
        else:
            item_name, value_str = parts[0], parts[1]

            if item_name in inventory:
                print(f"Redundant item '{item_name}' - discarding")
            else:
                try:
                    quantity = int(value_str)
                    inventory[item_name] = quantity
                except ValueError as e:
                    print(f"Quantity error for '{item_name}': {e}")

    # Statistics of the inventory
    print(f"Got inventory: {inventory}")

    # Total number of items
    item_names: list[str] = list(inventory.keys())
    print(f"Item list: {item_names}")

    # Total quantity of all items and
    # percentage representation in the inventory
    total_items: int = len(item_names)
    if total_items > 0:
        total_quantity: int = sum(inventory.values())
        print(f"Total quantity of the {total_items} items: {total_quantity}")

        # Quantity percentage for each item represented in the inventory
        for item in item_names:
            quantity = inventory[item]
            percentage: float = quantity / total_quantity * 100
            print(f"Item {item} represents {percentage:.1f}%")

        # Most abundant item and least abundant item (without max() and min())
        most_abundant_item: str = item_names[0]
        least_abundant_item: str = item_names[0]
        for item in item_names:
            if inventory[item] > inventory[most_abundant_item]:
                most_abundant_item = item
            if inventory[item] < inventory[least_abundant_item]:
                least_abundant_item = item

        print(f"Item most abundant: {most_abundant_item} "
              f"with quantity {inventory[most_abundant_item]}")
        print(f"Item least abundant: {least_abundant_item} "
              f"with quantity {inventory[least_abundant_item]}")

    # Updated inventory (adding a new item)
    inventory.update({'magic_item': 1})
    print("Updated inventory:", inventory)


if __name__ == "__main__":
    main()
