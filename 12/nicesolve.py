import sys
from collections import defaultdict
from itertools import combinations

inp = """\
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

# inp = """\
# EEEEE
# EXXXX
# EEEEE
# EXXXX
# EEEEE"""


with open(sys.argv[1]) as f:
    inp = f.read()
    inp_s = inp.split("\n")
    cords = {
        x + y * 1j: inp_s[x][y] for x in range(len(inp_s)) for y in range(len(inp_s[x]))
    }
    regions = list()
    for k, v in cords.items():
        # check up and left
        region = None
        add_fence = 4
        print(f'testing {k} {v}')
        if k - 1 in cords and cords[k-1] == v:
            for r in regions:
                if k-1 in r[2]:
                    region = r
                    # print(f'{k} is linked to {k-1} {r}')
                    break
            add_fence -= 2
        if k - 1j in cords and cords[k - 1j] == v:
            add_fence -= 2
            for r in regions:
                if k - 1j in r[2]:
                    if region and region != r:
                        regions.remove(r)
                        region[0] += r[0]
                        region[1] += r[1]
                        region[2] |= r[2]
                    else:
                       region = r
        if not region:
            region = [0,0,set(),v]
            regions.append(region)
        region[0] += 1
        region[1] += add_fence
        region[2].add(k)
        # post processing for part 2
    print("")
    for r in regions:
        # for each region
        tot_size = 0
        print(r[3])
        for k in r[2]:
            sides = 0
            print(k)
            if k - 1 not in r[2]:
                sides += 1
                print("top is side")
                # then top is a side
                # check top
                print(f"top shared {k - 1j} {k - 1j in r[2]} {k - 1 - 1j not in r[2]}")
                if k - 1j in r[2] and k - 1 - 1j not in r[2]:
                    # side shared, decrease with one
                    sides -= 1
            if k + 1 not in r[2]:
                sides += 1
                print("bottom is side")
                # then bottom is a side
                print(f"{k - 1j} {k - 1j in r[2]} {k + 1 - 1j} {k + 1 - 1j not in r[2]}")
                if k - 1j in r[2] and k + 1 - 1j not in r[2]:
                    # side shared, decrease with one
                    sides -= 1
                    print("bottom shared")
            if k - 1j not in r[2]:
                sides += 1
                print("left is side")
                # then left is a side
                print(f"{k - 1} {k - 1 in r[2]} {k - 1 - 1j} {k - 1 - 1j not in r[2]}")
                if k - 1 in r[2] and k - 1 - 1j not in r[2]:
                    # side shared, decrease with one
                    sides -= 1
                    print("left shared")
            if k + 1j not in r[2]:
                sides += 1
                print("right is side")
                # then right is a side
                print(f"{k - 1} {k - 1 in r[2]} {k - 1 + 1j} {k - 1 + 1j not in r[2]}")
                if k - 1 in r[2] and k - 1 + 1j not in r[2]:
                    # side shared, decrease with one
                    sides -= 1
                    print("right shared")
            print(f"{sides=}")
            tot_size += sides
        r.append(tot_size)
    # regions[3] = v
    print("\n".join([f"{l[0]} {l[1]} {l[3]} {l[4]}"  for l in regions]))
    print(sum(x[0] * x[1] for x in regions))
    print(sum(x[0] * x[4] for x in regions))
