#!/usr/bin/env python3

import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players: list[str] = ['alice', 'bob', 'charlie', 'dylan']
    actions: list[str] = ['run', 'eat', 'sleep', 'grab', 'move',
                          'climb', 'swim', 'use', 'release']
    # Infinite generator of events
    while True:
        player: str = random.choice(players)
        action: str = random.choice(actions)
        yield (player, action)


def consume_event(events: list[tuple[str, str]]) -> Generator[tuple[str, str],
                                                              None, None]:
    """ takes the previously created list, randomly pick one of its elements,
    remove it from the list, and yields it, until the list is empty."""
    while len(events) > 0:
        event = random.choice(events)
        events.remove(event)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")
    # Generate 1000 events and print them
    events_gen = gen_event()

    for i in range(1000):
        player, action = next(events_gen)
        print(f"Event {i}: Player {player} did action {action}")

    # Build a list of 10 events
    events: list[tuple[str, str]] = []
    for _ in range(10):
        events.append(next(events_gen))

    print(f"Built list of 10 events: {events}")

    # Consume events from the list using a generator
    for consumed_event in consume_event(events):
        print(f"Got event from list: {consumed_event}")

    # Print the remaining events in the list (should be empty)
    print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
