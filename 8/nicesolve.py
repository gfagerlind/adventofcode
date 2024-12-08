import sys
from collections import defaultdict
from itertools import combinations

inp = """\
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""


def antipod(p1, p2):
    return {2 * p2 - p1, 2 * p1 - p2}


def antinod(p1, p2):
    # abit ugly perhaps with the hardcoded range.
    return {p1 + x * (p1 - p2) for x in range(-50, 50)}


with open(sys.argv[1]) as f:
    inp = f.read()
    inp_s = inp.split("\n")
    sym = defaultdict(set)
    antipodes = set()
    antinodes = set()
    all_cords = set()
    for x in range(len(inp_s)):
        for y in range(len(inp_s[x])):
            p = complex(x, y)
            all_cords.add(p)
            if (s := inp_s[x][y]) != ".":
                sym[s].add(p)
    for s in sym:
        for c in combinations(sym[s], 2):
            antipodes |= antipod(*c)
            antinodes |= antinod(*c)
    # filter out nodes and podes outside of grid
    print(len(antipodes & all_cords))
    print(len(antinodes & all_cords))
