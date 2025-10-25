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


def calculate_sector_id(data: tuple[str, int, str]) -> int:
    name, sector_id, checksum = data
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
    assert calculate_sector_id(parse("aaaaa-bbb-z-y-x-123[abxyz]")) == 123
    assert calculate_sector_id(parse("a-b-c-d-e-f-g-h-987[abcde]")) == 987
    assert calculate_sector_id(parse("not-a-real-room-404[oarel]")) == 404
    assert calculate_sector_id(parse("totally-real-room-200[decoy]")) == 0
    assert sum(map(calculate_sector_id, map(parse, lines))) == 1514


def test_part_1_actual():
    with open("days/04/input.txt") as f:
        input_data = f.read()
    lines = input_data.strip().split("\n")
    assert sum(map(calculate_sector_id, map(parse, lines))) == 158835


def rotate_letter(letter: str) -> str:
    match letter:
        case "z":
            return "a"
        case "-":
            return " "
        case " ":
            return " "
        case _:
            return chr(ord(letter) + 1)


def rotate_name(name: str, sector_id) -> str:
    for _ in range(sector_id):
        name = map(rotate_letter, name)
    return "".join(name)


def parse_with_rotation(line: str) -> tuple[str, int, str]:
    (name, sector_id, checksum) = parse(line)
    return (rotate_name(name, sector_id), sector_id, checksum)


def test_rotate_letter():
    assert rotate_letter("z") == "a"
    assert rotate_letter("a") == "b"
    assert rotate_letter("b") == "c"
    assert rotate_letter("-") == " "
    assert rotate_letter(" ") == " "


def test_rotate_name():
    assert rotate_name("qzmt-zixmtkozy-ivhz", 343) == "very encrypted name"


def test_part_2_example():
    lines = [
        "aaaaa-bbb-z-y-x-123[abxyz]",
        "a-b-c-d-e-f-g-h-987[abcde]",
        "not-a-real-room-404[oarel]",
        "totally-real-room-200[decoy]",
    ]
    assert sum(map(calculate_sector_id, map(parse_with_rotation, lines))) == 987


def test_part_2_actual():
    with open("days/04/input.txt") as f:
        input_data = f.read()
    lines = input_data.strip().split("\n")
    assert (
        list(
            filter(
                lambda x: x[0] == "northpoleobjectstorage",
                map(parse_with_rotation, lines),
            )
        )[0][1]
        == 993
    )
