#!/usr/bin/python3

import random
import typing

PLAYER: list[str] = [
    "Zelie",
    "Thelma",
    "Priyangan",
    "Adrien"
]

ACTIONS: list[str] = [
    "sprint",
    "run slow",
    "look cool to impress",
    "show off muscles",
    "sleep cause tired",
    "climb a tree for fun",
    "move",
    "move backwards",
    "smoke a cigarette",
    "jump"
]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        name = random.choice(PLAYER)
        action = random.choice(ACTIONS)

        yield (name, action)


def create_list() -> list[tuple[str, str]]:

    events = gen_event()
    event_list = []

    for i in range(10):
        event_list.append(next(events))

    print(f"Built list of 10 events: {event_list}")

    return event_list


def get_event(
        event_list: list[tuple[str, str]]
        ) -> typing.Generator[tuple[str, str], None, None]:

    while (len(event_list) > 0):
        random_i = random.randint(0, len(event_list) - 1)
        event = event_list.pop(random_i)
        yield event


def main() -> None:

    print("=== Game Data Stream Processor ===")

    events = gen_event()
    for i in range(1000):
        name, action = next(events)
        print(f"Event {i}: Player {name} did action '{action}'")

    print()

    event_list = create_list()

    for event in get_event(event_list):
        print()
        print("Got event from list: ", event)
        print("Remains in list: ", event_list)


if __name__ == "__main__":
    main()
