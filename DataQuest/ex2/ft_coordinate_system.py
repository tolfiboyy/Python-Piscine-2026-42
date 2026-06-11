#!/usr/bin/python3
import math
Coordinates = tuple[float, float, float]


def distance_between_two(coords: Coordinates, coords2: Coordinates) -> None:
    distance: float = math.sqrt(
        (coords2[0] - coords[0]) ** 2 +
        (coords2[1] - coords[1]) ** 2 +
        (coords2[2] - coords[2]) ** 2
    )
    print("Distance between the 2 sets of coordinates: ", round(distance, 4))


def distance(coords: Coordinates) -> None:
    distance: float = math.sqrt(
        coords[0] ** 2 +
        coords[1] ** 2 +
        coords[2] ** 2
    )
    print("Distance to center: ", round(distance, 4))


def get_player_pos() -> Coordinates:

    while True:
        try:

            coords = input("Enter new coordinates "
                           "as floats in format ’x,y,z’: ")

            coords_split = coords.split(",")

            if (len(coords_split) != 3):
                print("Invalid syntax, 3 float values needed.")
                continue

            x = float(coords_split[0].strip())
            y = float(coords_split[1].strip())
            z = float(coords_split[2].strip())

            return (x, y, z)

        except ValueError as error:
            print(error)


def main() -> None:
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates [x,y,z]")
    first_tuple = get_player_pos()
    print("Got a first tuple: ", first_tuple)
    print(f"It includes: X={first_tuple[0]}, "
          f"Y={first_tuple[1]}, Z={first_tuple[2]}")
    distance(first_tuple)

    print()

    print("Get a second set of coordinates [x,y,z]")
    second_tuple = get_player_pos()
    print("Got a second tuple: ", second_tuple)
    print(f"It includes: X={second_tuple[0]}, "
          f"Y={second_tuple[1]}, Z={second_tuple[2]}")
    distance_between_two(first_tuple, second_tuple)

    print()

    print("=== End ===")


if __name__ == "__main__":
    main()
