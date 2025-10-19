def is_valid_move(x, y, keypad):
    return 0 <= y < len(keypad) and 0 <= x < len(keypad[y]) and keypad[y][x]


def move(x, y, direction, keypad):
    match direction:
        case "U":
            (new_x, new_y) = (x, y - 1)
            if is_valid_move(new_x, new_y, keypad):
                return (new_x, new_y)
        case "R":
            (new_x, new_y) = (x + 1, y)
            if is_valid_move(new_x, new_y, keypad):
                return (new_x, new_y)
        case "D":
            (new_x, new_y) = (x, y + 1)
            if is_valid_move(new_x, new_y, keypad):
                return (new_x, new_y)
        case "L":
            (new_x, new_y) = (x - 1, y)
            if is_valid_move(new_x, new_y, keypad):
                return (new_x, new_y)
    return (x, y)


def input_combinations(lines, coordinate, keypad):
    result = ""
    for line in lines:
        for direction in list(line):
            (x, y) = coordinate
            coordinate = move(x, y, direction, keypad)
        (x, y) = coordinate
        result += str(keypad[y][x])
    return result


def part_1(input_data):
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    coordinate = (1, 1)
    return input_combinations(input_data.strip().split("\n"), coordinate, keypad)


def test_part_1_example():
    assert (
        part_1(
            """ULL
RRDDD
LURDL
UUUUD"""
        )
        == "1985"
    )


def test_part_1_actual():
    with open("days/02/input.txt") as f:
        input_data = f.read()
    assert part_1(input_data) == "14894"


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
    coordinate = (0, 2)
    return input_combinations(input_data.strip().split("\n"), coordinate, keypad)


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
