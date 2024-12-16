import sys
import bisect

inp = """\
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
"""
inp = """\
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""
def pp(s, lx, ly):
    for x in range(lx):
        for y in range(ly):
            if (x + 1j * y) in s:
                print('o', end="")
            else:
                print(".", end="")
        print("")

with open(sys.argv[1]) as f:
    inp = f.read()
    inp = inp.split('\n')
    valid = {x + y * 1j for x, r in enumerate(inp) for y, v in enumerate(r) if v in '.E'}
    startstop = {v: x + y * 1j for x, r in enumerate(inp) for y, v in enumerate(r) if v in 'ES'}
    candidates = [(startstop['S'],set(),1j,0)]
    stop = startstop['E']
    visited = {}
    res = {}
    while len(candidates):
        c = candidates.pop(0)
        p = c[0]
        if visited.get(p, 9999999999999999) + 1000 < c[3]:
            continue
        visited[p] = c[3]
        if p == stop:
            if c[3] in res:
                res[c[3]] = res[c[3]] | {*c[1]}
            else:
                res[c[3]] = {*c[1]}
        for d in (1,-1,1j,-1j):
            cost = c[3] + 1 + (1000 if c[2] != d else 0)
            if p + d not in valid:
                continue
            if p + d in c[1]:
                continue
            bisect.insort(candidates, (p+d, [*c[1], p + d], d, cost), key=lambda x: x[3])
    print(min(res))
    print(len(res[min(res)]) + 1)
