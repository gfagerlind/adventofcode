import sys
from itertools import product

test = [
    "EFGXHIJ",
    "1234567",
    "890abcd",
    "efgxhij",
    "klmnopq",
    "rstuvxy",
    "RSTUVXY",
]
inp = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX",
]

p = (-1, 0, 1)
PERMS = list(product(p, p))


def get_bounded(m, x: int, y: int) -> str:
    if 0 <= x < len(m) and 0 <= y < len(m[x]):
        return m[x][y]
    return ""


def get(sx, sy, m, x, y, start, stop) -> str:
    return "".join([get_bounded(m, x + sx * i, y + sy * i) for i in range(start, stop)])


def count(m, x: int, y: int) -> int:
    if m[x][y] != "X":
        return 0
    return sum([get(sx, sy, m, x, y, 0, 4) == "XMAS" for sx, sy in PERMS])


def xcount(m, x: int, y: int) -> int:
    if m[x][y] != "A":
        return 0
    if get(1, -1, m, x, y, -1, 2) in ("MAS", "SAM"):
        if get(1, 1, m, x, y, -1, 2) in ("MAS", "SAM"):
            return 1
    return 0


with open(sys.argv[1]) as f:
    m = f.readlines()
    print(
        [
            sum(x)
            for x in zip(
                *[
                    (count(m, x, y), xcount(m, x, y))
                    for x in range(len(m))
                    for y in range(len(m[x]))
                ]
            )
        ]
    )
