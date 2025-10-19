from itertools import batched, chain


def is_valid_triangle(sides: map[int]) -> bool:
    a, b, c = sides
    return a + b > c and a + c > b and b + c > a


def count_valid_triangles(lines: list[int]) -> int:
    return sum(map(is_valid_triangle, lines))


def test_part_1_example():
    assert count_valid_triangles([(5, 10, 25)]) == 0


def test_part_1_actual():
    with open("days/03/input.txt") as f:
        input_data = f.read()
    lines = [list(map(int, line.split())) for line in input_data.strip().split("\n")]
    assert count_valid_triangles(lines) == 993


def transform(lines: list[str]) -> list[str]:
    lines = [[int(value) for value in row.split()] for row in lines]
    return list(batched(chain(*zip(*lines)), 3))


def test_transform_lines():
    assert transform(
        """101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603
""".strip().split("\n")
    ) == [
        (101, 102, 103),
        (201, 202, 203),
        (301, 302, 303),
        (401, 402, 403),
        (501, 502, 503),
        (601, 602, 603),
    ]


def test_part_2_actual():
    with open("days/03/input.txt") as f:
        input_data = f.read()
    lines = input_data.strip().split("\n")
    assert count_valid_triangles(transform(lines)) == 1849
