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
                print("o", end="")
            else:
                print(".", end="")
        print("")


with open(sys.argv[1]) as f:
    inp = f.read()
    inp = inp.split("\n")
    valid = {
        x + y * 1j for x, r in enumerate(inp) for y, v in enumerate(r) if v in ".E"
    }
    startstop = {
        v: x + y * 1j for x, r in enumerate(inp) for y, v in enumerate(r) if v in "ES"
    }
    candidates = [(startstop["S"], set(), 1j, 0)]
    stop = startstop["E"]
    # [(point, direction): cost]
    visited = {}
    seats = set()
    mincost = None
    while len(candidates):
        p, route, pd, c = candidates.pop(0)
        if mincost and c > mincost:
            continue
        if (p, pd) in visited and visited[(p, pd)] < c:
            # if we have already visited this point from this direction skip, and the cost is worse
            # We need to consider equal paths for part2, otherwise the cost could be skipped
            continue
        visited[(p, pd)] = c
        if p == stop:
            if mincost == None or c < mincost:
                mincost = c
                seats = route
            if c == mincost:
                seats |= route
        for d in (1, -1, 1j, -1j):
            if p + d not in valid:
                continue
            if p + d in route:
                # if this route has already traversed this point
                continue
            cost = c + 1 + (1000 if pd != d else 0)
            bisect.insort(
                candidates, (p + d, route | {p + d}, d, cost), key=lambda x: x[3]
            )
    print(mincost)
    print(len(seats) + 1)
