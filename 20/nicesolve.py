import sys
import bisect
from collections import defaultdict

inp = """\
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
"""


def pp(s, lx, ly):
    for x in range(lx):
        for y in range(ly):
            if (x + 1j * y) in s:
                print("o", end="")
            else:
                print(".", end="")
        print("")


with open(sys.argv[1]) as f:
    inp = f.read()
    cords = {x + y * 1j: v for x, r in enumerate(inp.split('\n')) for y, v in enumerate(r)
        if v !='#'
    }
    start = 0
    stop = 0
    for k,v in cords.items():
        if v == "S":
            start = k
        if v == "E":
            stop = k
    # only one valid rout
    route = []
    curr = start
    oldcurr = stop
    while True:
        route.append(curr)
        if curr == stop:
            break
        for d in (1, -1, 1j, -1j):
            if curr + d == oldcurr:
                continue
            if curr + d in cords:
                oldcurr = curr
                curr = curr + d
                break
    cheats = (defaultdict(int), defaultdict(int))
    picoseconds = (2, 20)
    cutoff = 100
    for cheatstart in range(len(route)):
        for cheatstop in range(cheatstart+3,len(route)):
            diff = route[cheatstart] - route[cheatstop]
            taxidiff = abs(diff.imag) + abs(diff.real)
            for i in (0,1):
                if taxidiff <= picoseconds[i]:
                    cheats[i][cheatstop - cheatstart - taxidiff ] +=1
    for i in (0,1):
        print(sum(cheats[i][k] for k in cheats[i] if k >= cutoff))
