import hashlib


def part_1(door_id: str) -> str:
    idx = 0
    result = ""
    while len(result) < 8:
        new_door_id = f"{door_id}{idx}"
        idx += 1
        res = hashlib.md5(new_door_id.encode())
        hash = res.hexdigest()
        if hash.startswith("00000"):
            result += hash[5]
    return result


def test_1_example():
    assert part_1("abc") == "18f47a30"


def test_1_actual():
    assert part_1("ugkcyxxp") == "d4cd2ee1"


def part_2(door_id: str) -> str:
    idx = 0
    total_found = 0
    result = ["_"] * 8
    while total_found < 8:
        new_door_id = f"{door_id}{idx}"
        idx += 1
        res = hashlib.md5(new_door_id.encode())
        hash = res.hexdigest()
        if hash.startswith("00000"):
            if "0" <= hash[5] <= "7":
                pos = int(hash[5])
                if result[pos] == "_":
                    result[pos] = hash[6]
                    total_found += 1
    return "".join(result)


def test_2_example():
    assert part_2("abc") == "05ace8e3"


def test_2_actual():
    assert part_2("ugkcyxxp") == "f2c730e5"
