from typing import Callable


def part_1(lines: list[str], sort: Callable[[dict[str, int]], str]) -> str:
    occurences = [{} for _ in range(len(lines[0]))]
    for line in lines:
        for index, character in enumerate(line):
            occurences[index][character] = occurences[index].get(character, 0) + 1
    return "".join(map(lambda x: sort(x, key=x.get), occurences))


def test_part_1_example():
    with open("days/06/example.txt") as f:
        input_data = f.read()
    lines = input_data.strip().split("\n")
    assert part_1(lines, max) == "easter"


def test_part_1_actual():
    with open("days/06/input.txt") as f:
        input_data = f.read()
    lines = input_data.strip().split("\n")
    assert part_1(lines, max) == "gyvwpxaz"


def test_part_2_example():
    with open("days/06/example.txt") as f:
        input_data = f.read()
    lines = input_data.strip().split("\n")
    assert part_1(lines, min) == "advent"


def test_part_2_actual():
    with open("days/06/input.txt") as f:
        input_data = f.read()
    lines = input_data.strip().split("\n")
    assert part_1(lines, min) == "jucfoary"
