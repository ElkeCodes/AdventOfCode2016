deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def part_1(input_data):
    delta_idx = 0
    coordinate = (0, 0)
    for line in input_data.strip().split("\n"):
        for direction in list(line.split(", ")):
            turn, steps = direction[0], int(direction[1:])
            delta_idx = (delta_idx + (1 if turn == "R" else -1)) % 4
            dx, dy = deltas[delta_idx]
            coordinate = (coordinate[0] + dx * steps, coordinate[1] + dy * steps)
    return abs(coordinate[0]) + abs(coordinate[1])


def test_part_1_example_1():
    input_data = """R2, L3"""
    assert part_1(input_data) == 5


def test_part_1_example_2():
    input_data = """R2, R2, R2"""
    assert part_1(input_data) == 2


def test_part_1_example_3():
    input_data = """R5, L5, R5, R3"""
    assert part_1(input_data) == 12


def test_part_1_actual():
    with open("days/01/input.txt") as f:
        input_data = f.read()
    assert part_1(input_data) == 241


def part_2(input_data):
    delta_idx = 0
    coordinate = (0, 0)
    visited = set()
    visited.add(coordinate)
    for line in input_data.strip().split("\n"):
        for direction in list(line.split(", ")):
            turn, steps = direction[0], int(direction[1:])
            delta_idx = (delta_idx + (1 if turn == "R" else -1)) % 4
            dx, dy = deltas[delta_idx]
            for _ in range(steps):
                coordinate = (coordinate[0] + dx, coordinate[1] + dy)
                if coordinate in visited:
                    return abs(coordinate[0]) + abs(coordinate[1])
                visited.add(coordinate)
    return None


def test_part_2_example_1():
    input_data = """R8, R4, R4, R8"""
    assert part_2(input_data) == 4


def test_part_2_actual():
    with open("days/01/input.txt") as f:
        input_data = f.read()
    assert part_2(input_data) == 116
