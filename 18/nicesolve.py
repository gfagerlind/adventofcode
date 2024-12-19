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
    inp = inp.strip().split("\n")
    valid = []
    for i, line in enumerate(inp):
        if line:
            x,y = map(int,line.split(','))
            valid.append(x + y *1j)
    bottom = 1024
    pivot = 2000
    top = 3450
    while True:
        candidates = [(0, set(), 0)]
        stop = 70 + 70j
        visited = set()
        mincost = None
        while len(candidates):
            p, route, c = candidates.pop(0)
            for d in (1, -1, 1j, -1j):
                pd = p + d
                if pd in valid[0:pivot] or pd in route or not( 0 <= pd.real <= 70) or not( 0<= pd.imag <= 70):
                    # if not path or route has already traversed this point
                    continue
                cost = c + 1
                if mincost and cost > mincost:
                    # if a cheaper complete path exists
                    continue
                if pd in visited:
                    # if we have already visited this point from this direction skip, and the cost is worse
                    # We need to consider equal paths for part2, otherwise the cost could be skipped
                    continue
                if pd == stop:
                    mincost = cost
                    break
                visited.add(pd)
                bisect.insort(candidates, (pd, route | {pd}, cost), key=lambda x: x[2])
        print(f"{pivot=} {cost} {top=} {bottom=} {valid[pivot]}")
        if mincost:
            mincost = 0
            bottom = pivot
        else:
            top = pivot
        pivot = bottom + (top - bottom) // 2 
