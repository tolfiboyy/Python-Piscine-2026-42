#!/usr/bin/python3

import sys


def stuff_inventory() -> dict[str, int]:
    inventory: dict[str, int] = {}

    for arg in sys.argv[1:]:
        stuff = arg.split(":")

        if len(stuff) != 2:
            print(f"Error - Invalid parameter '{arg}'")
            continue

        item = stuff[0]
        item_quantity_str = stuff[1]

        if item in inventory:
            print(f"Redundant item ’{item}’ - discarding")
            continue

        try:
            quantity = int(item_quantity_str)
            inventory[item] = quantity
        except ValueError as error:
            print(f"Quantity error for '{item}': {error}")

    return inventory


def show_inventory(inventory: dict[str, int]) -> None:

    print("Got inventory: ", inventory)

    print()

    item_list = list(inventory.keys())
    quantities = list(inventory.values())

    print("Item list: ", item_list)

    print(f"Total quantity of the {len(item_list)} items: ", sum(quantities))

    for item in inventory:
        percent = inventory[item] / sum(quantities) * 100
        print(f"Item {item} represents {round(percent, 1)}%")


def most_or_least(inventory: dict[str, int]) -> None:

    most_item = ""
    most_quantity = 0

    for item in inventory:
        if inventory[item] > most_quantity:
            most_quantity = inventory[item]
            most_item = item

    print(f"Item most abundant: {most_item} with quantity {most_quantity}")

    least_item = ""
    least_quantity = -1

    if least_quantity == -1:
        least_quantity = inventory[item]
        least_item = item

    for item in inventory:
        if inventory[item] < least_quantity:
            least_quantity = inventory[item]
            least_item = item

    print(f"Item least abundant: {least_item} with quantity {least_quantity}")


def add_magic_stuff(inventory: dict[str, int]) -> None:
    print("Adding the magic stuff...\n")

    inventory.update({"Magic Stuff": 1})

    print("Updated inventory: ", inventory)


def main() -> None:
    print("=== Inventory System Analysis ===\n")
    inventory = stuff_inventory()

    if len(inventory) == 0:
        print("Inventory is empty !\n")
        print("Try to stuff your pockets next time :)")
        return

    show_inventory(inventory)
    most_or_least(inventory)

    print()

    add_magic_stuff(inventory)


if __name__ == "__main__":
    main()
