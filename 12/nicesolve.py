import sys

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
        region = None
        # fence is 4 minus
        # for side in (top, left), if shared, reduce fence with 2
        add_fence = (
            4 - 2 * (cords.get(k - 1, None) == v) - 2 * (cords.get(k - 1j, None) == v)
        )
        if add_fence < 4:
            # if fence is less than four, there are regions, check
            # which one to add the fence to.
            # If we are the tunnel between two regions, merge them
            rs = [
                r
                for r in regions
                if (k - 1 in r[0] and cords[k - 1] == v)
                or (k - 1j in r[0] and cords[k - 1j] == v)
            ]
            region = rs[0]
            if len(rs) > 1:
                # merge
                region[0] |= rs[1][0]
                region[1] += rs[1][1]
                regions.remove(rs[1])
        else:
            region = [set(), 0]
            regions.append(region)
        region[0].add(k)
        region[1] += add_fence
    for r in regions:
        # again, check up and left, for each side we have that we don't share
        # add it
        tot_size = sum(
            (k + x * y not in r[0] and (k + y not in r[0] or k + x * y + y in r[0]))
            for x in (1j, -1j)
            for y in (-1j, -1)
            for k in r[0]
        )
        r.append(tot_size)
    print("\n".join([f"{l[0]} {l[1]} {l[2]}" for l in regions]))
    print(sum(len(x[0]) * x[1] for x in regions))
    print(sum(len(x[0]) * x[2] for x in regions))
