import sys
from collections import defaultdict
from itertools import combinations

inp = """\
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""


with open(sys.argv[1]) as f:
    inp = f.read()
    inp_s = inp.split("\n")
    cords = {
        (x + y * 1j): int(inp_s[x][y]) for x in range(len(inp_s)) for y in range(len(inp_s[x]))
    }
    tot = 0
    tot2 = 0
    for k, v in cords.items():
        if v == 0:
            routeheads = {k: 1}
            for height in range(1,10):
                newrouteheads = defaultdict(lambda:0)
                for rh in routeheads:
                    for dirs in (1j, -1j, 1, -1):
                        if cords.get(rh + dirs, None) == height:
                            newrouteheads[rh + dirs] += routeheads[rh]
                routeheads = newrouteheads
            tot += len(routeheads)
            tot2 += sum(routeheads.values())

    print(tot)
    print(tot2)
