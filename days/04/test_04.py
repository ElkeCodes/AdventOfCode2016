import re


def parse(data: str) -> tuple[str, int, str]:
    result = re.match(
        r"(?P<name>[\w-]+)+-(?P<sector_id>\d+)\[(?P<checksum>\w+)\]", data
    )
    return (
        result.group("name").replace("-", ""),
        int(result.group("sector_id")),
        result.group("checksum"),
    )


def find_checksum_letter_in_name(name: str, checksum_letter: str):
    for idx in range(len(name)):
        if name[idx] == checksum_letter:
            return idx
    return -1


def calculate_sector_id(name_to_parse: str) -> int:
    (name, sector_id, checksum) = parse(name_to_parse)
    occurences = {}
    for letter in name:
        occurences[letter] = occurences.get(letter, 0) + 1
    sorted_occurences = sorted(
        occurences.items(), key=lambda occurence: (-occurence[1], occurence[0])
    )
    calculated_checksum = "".join([letter for (letter, _) in sorted_occurences[:5]])
    if calculated_checksum == checksum:
        return sector_id
    return 0


def test_part_1_example():
    lines = [
        "aaaaa-bbb-z-y-x-123[abxyz]",
        "a-b-c-d-e-f-g-h-987[abcde]",
        "not-a-real-room-404[oarel]",
        "totally-real-room-200[decoy]",
    ]
    assert calculate_sector_id("aaaaa-bbb-z-y-x-123[abxyz]") == 123
    assert calculate_sector_id("a-b-c-d-e-f-g-h-987[abcde]") == 987
    assert calculate_sector_id("not-a-real-room-404[oarel]") == 404
    assert calculate_sector_id("totally-real-room-200[decoy]") == 0
    assert sum(map(calculate_sector_id, lines)) == 1514


def test_part_1_actual():
    with open("days/04/input.txt") as f:
        input_data = f.read()
    lines = input_data.strip().split("\n")
    assert sum(map(calculate_sector_id, lines)) == 158835
