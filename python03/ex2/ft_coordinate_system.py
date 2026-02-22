import sys

import math


def ft_coordinate_system():
    print("=== Game Coordinate System ===")
    print("")
    position_1: tuple[int, int, int] = (0, 0, 0)
    x1, y1, z1 = position_1
    argc: int = len(sys.argv)
    if argc == 1:
        position_2: tuple[int, int, int] = (10, 20, 5)
        x2, y2, z2 = position_2

        print(f"Position created: ({x2}, {y2}, {z2})")

        distance: float = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
        print(
            f"Distance between ({x1}, {y1}, {z1}) "
            f"and ({x2}, {y2}, {z2}): {distance:.2f}"
            )
    else:
        try:
            if argc > 2:
                raise ValueError("Too many arguments")
            argv: str = sys.argv[1]
            parts: list[str] = argv.split(",")

            if len(parts) != 3:
                raise ValueError(
                    "Not the number of values requested by the program"
                    )
            values: list[int] = []

            try:
                for p in parts:
                    values.append(int(p))

            except ValueError as e:
                print(f"Parsing invalid coordinates: \"{sys.argv[1]}\"")
                print(f"Error parsing coordinates: {e}")
                print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
                return

            print(f"Parsing coordinates: \"{sys.argv[1]}\"")

            coords: tuple[int, int, int] = tuple(values)
            x2, y2, z2 = coords
            print(f"Parsed position: ({x2}, {y2}, {z2})")

            distance: float = math.sqrt(
                (x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2
                )
            print(
                f"Distance between ({x1}, {y1}, {z1}) "
                f"and ({x2}, {y2}, {z2}): {distance:.1f}"
                )

        except ValueError as e:
            print(e)
            return

    print("")
    print("Unpacking demonstration:")
    print(f"Player at x={x2}, y={y2}, z={z2}")
    print(f"Coordinates: X={x2}, Y={y2}, Z={z2}")


if __name__ == "__main__":
    ft_coordinate_system()
