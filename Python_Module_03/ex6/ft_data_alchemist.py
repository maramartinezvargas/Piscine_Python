#!/usr/bin/env python3

import random


def main() -> None:
    print("=== Game Data Alchemist ===")
    players: list[str] = ['Alice', 'bob', 'Charlie',
                          'dylan', 'Emma', 'Gregory',
                          'john', 'kevin', 'Liam']

    print(f"Initial list of players: {players}")

    all_names_capitalized: list[str] = [name.capitalize()
                                        for name in players]
    print(f"New list with all names capitalized: {all_names_capitalized}")

    # New list of capitalized names only:
    capitalized_names_only: list[str] = [name for name in players
                                         if name == name.capitalize()]
    print(f"New list of capitalized names only: {capitalized_names_only}")

    # Dictionary of players with random values between 1 and 1000
    player_scores: dict[str, int] = {name: random.randint(1, 1000)
                                     for name in all_names_capitalized}
    print(f"Score dict: {player_scores}")

    # Second dictionary with scores higher than the average score
    average_score: float = sum(player_scores.values()) / len(player_scores)
    print(f"Score average is {average_score:.2f}")

    high_scorers: dict[str, int] = {name: score
                                    for name, score in player_scores.items()
                                    if score > average_score}
    print(f"High scores: {high_scorers}")


if __name__ == "__main__":
    main()
