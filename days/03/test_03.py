def part_1(input_data):
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = 0
    coordinate = (1, 1)
    for line in input_data.strip().split("\n"):
        for direction in list(line):
            (x, y) = coordinate
            match direction:
                case "U":
                    coordinate = (x, max(0, y - 1))
                case "R":
                    coordinate = (min(2, x + 1), y)
                case "D":
                    coordinate = (x, min(2, y + 1))
                case "L":
                    coordinate = (max(0, x - 1), y)
        result *= 10
        (x, y) = coordinate
        result += keypad[y][x]
    return result


def test_part_1_example():
    assert (
        part_1(
            """ULL
RRDDD
LURDL
UUUUD"""
        )
        == 1985
    )


def test_part_1_actual():
    with open("days/02/input.txt") as f:
        input_data = f.read()
    assert part_1(input_data) == 14894


"""
    1
  2 3 4
5 6 7 8 9
  A B C
    D

"""


def part_2(input_data):
    keypad = [
        [None, None, 1, None, None],
        [None, 2, 3, 4, None],
        [5, 6, 7, 8, 9],
        [None, "A", "B", "C", None],
        [None, None, "D", None, None],
    ]
    result = ""
    coordinate = (0, 2)
    for line in input_data.strip().split("\n"):
        for direction in list(line):
            (x, y) = coordinate
            match direction:
                case "U":
                    (new_x, new_y) = (x, y - 1)
                    if (
                        0 <= new_y < len(keypad)
                        and 0 <= new_x < len(keypad[new_y])
                        and keypad[new_y][new_x]
                    ):
                        coordinate = (new_x, new_y)
                case "R":
                    (new_x, new_y) = (x + 1, y)
                    if (
                        0 <= new_y < len(keypad)
                        and 0 <= new_x < len(keypad[new_y])
                        and keypad[new_y][new_x]
                    ):
                        coordinate = (new_x, new_y)
                case "D":
                    (new_x, new_y) = (x, y + 1)
                    if (
                        0 <= new_y < len(keypad)
                        and 0 <= new_x < len(keypad[new_y])
                        and keypad[new_y][new_x]
                    ):
                        coordinate = (new_x, new_y)
                case "L":
                    (new_x, new_y) = (x - 1, y)
                    if (
                        0 <= new_y < len(keypad)
                        and 0 <= new_x < len(keypad[new_y])
                        and keypad[new_y][new_x]
                    ):
                        coordinate = (new_x, new_y)
        (x, y) = coordinate
        result += str(keypad[y][x])
    return result


def test_part_2_example():
    assert (
        part_2(
            """ULL
RRDDD
LURDL
UUUUD"""
        )
        == "5DB3"
    )


def test_part_2_actual():
    with open("days/02/input.txt") as f:
        input_data = f.read()
    assert part_2(input_data) == "26B96"
