import sys
import re

inp = """\
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""
lx, ly = 11, 7


def pp(s, lx, ly):
    for y in range(ly):
        for x in range(lx):
            if (x, y) in s:
                print("o", end="")
            else:
                print(".", end="")
        print("")


def istreelike(s):
    q = 0
    for p in s:
        for x in range(-3, 3):
            for y in range(-3, 3):
                if (p[0] + x, p[1] + y) in s:
                    q += 1
    return q


with open(sys.argv[1]) as f:
    inp, lx, ly = f.read(), 101, 103
    m = [
        list(map(int, t)) for t in re.findall(r"p=(\d+),(\d+) v=([-\d]+),([-\d]+)", inp)
    ]
    bestfit = 0
    for s in range(10000):
        p = {((px + vx * s) % lx, (py + vy * s) % ly) for px, py, vx, vy in m}
        c = istreelike(p)
        if c > bestfit:
            pp(p, lx, ly)
            print(s)
            bestfit = c
