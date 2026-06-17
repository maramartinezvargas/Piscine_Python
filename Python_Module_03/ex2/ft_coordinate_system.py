#!/usr/bin/env python3

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_input: str = input("Enter new coordinates "
                                "as floats in format 'x,y,z': ")
        parts = user_input.split(",")

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        coords: list[float] = []
        valid = True

        for part in parts:
            try:
                coords.append(float(part.strip()))
            except ValueError as e:
                print(f"Error on parameter '{part.strip()}': {e}")
                valid = False

        if valid:
            return coords[0], coords[1], coords[2]


def calc_distance(dest: tuple[float, float, float],
                  center: tuple[float, float, float]) -> float:
    x1, y1, z1 = dest
    x2, y2, z2 = center
    return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    coord_1 = get_player_pos()
    print(f"Got a first tuple: {coord_1}")
    x, y, z = coord_1
    print(f"It includes: X={x}, Y={y}, Z={z}")

    distance_to_center = calc_distance(coord_1, (0, 0, 0))
    print(f"Distance to center: {distance_to_center:.4f}")

    print("\nGet a second set of coordinates")
    coord_2 = get_player_pos()

    distance_between = calc_distance(coord_2, coord_1)
    print(f"Distance between the 2 sets of coordinates: "
          f"{distance_between:.4f}")
