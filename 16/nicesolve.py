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
        p, route, prev_d, c = candidates.pop(0)
        for d in (1, -1, 1j, -1j):
            pd = p + d
            if pd not in valid or pd in route:
                # if not path or route has already traversed this point
                continue
            cost = c + 1 + (1000 if prev_d != d else 0)
            if mincost and cost > mincost:
                # if a cheaper complete path exists
                continue
            if pd == stop:
                if mincost == None or cost < mincost:
                    mincost = cost
                    seats = route | {pd}
                if cost == mincost:
                    seats |= route | {pd}
                # no need to continue from a successful route
                continue
            if (pd, d) in visited and visited[(pd, d)] < cost:
                # if we have already visited this point from this direction skip, and the cost is worse
                # We need to consider equal paths for part2, otherwise the cost could be skipped
                continue
            visited[(pd, d)] = cost
            bisect.insort(candidates, (pd, route | {pd}, d, cost), key=lambda x: x[3])
    print(mincost)
    print(len(seats) + 1)
