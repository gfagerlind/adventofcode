import sys
from collections import defaultdict
from itertools import permutations

inp = """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""
rotation = ((-1, 0), (0, 1), (1, 0), (0, -1))


def pp(c):
    s = max(k[0] for k in c) + 1
    m = [s * ["@"] for x in range(0, s)]
    for k in c:
        m[k[0]][k[1]] = c[k]
    print("\n".join(["".join(y for y in m[x]) for x in range(len(m))]))


def travel_in_a_loop(cords, curpos, curr, visits):
    while True:
        # while on map
        candidate = curpos[0] + rotation[curr][0], curpos[1] + rotation[curr][1]
        if candidate not in cords:
            return False
        if cords[candidate] in ".^":
            if curr in visits[candidate]:
                return True
            visits[candidate].append(curr)
            curpos = candidate
        if cords[candidate] in "#O":
            curr = (curr + 1) % 4


with open(sys.argv[1]) as f:
    inp = f.read()
    inp_s = inp.split("\n")
    cords = {
        (x, y): inp_s[x][y] for x in range(len(inp_s)) for y in range(len(inp_s[x]))
    }
    startpos = [k for k in cords if cords[k] == "^"][0]
    visits = defaultdict(list)
    travel_in_a_loop(cords, startpos, 0, visits)
    print(len(visits))
    loops = 0
    for visit in visits:
        # now for fancy, make candidate
        cc = {**cords, visit: "O"}
        # find out if this is obstructing by looping, only consider first collision
        curr = visits[visit][0]
        # take a step back!
        curpos = visit[0] - rotation[curr][0], visit[1] - rotation[curr][1]
        # pp(cc)
        # print(visit, curpos, rotation[curr])
        if travel_in_a_loop(cc, curpos, curr, defaultdict(list)):
            loops += 1
    print(loops)
