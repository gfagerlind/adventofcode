import sys
import re
import math

inp = """\
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""


with open(sys.argv[1]) as f:
    inp = f.read()
    m = re.findall(
        r"Button A: X\+(\d+), Y\+(\d+)\n"
        + r"Button B: X\+(\d+), Y\+(\d+)\n"
        + r"Prize: X=(\d+), Y=(\d+)",
        inp,
        re.MULTILINE,
    )
    l = re.findall("Prize:", inp, re.MULTILINE)
    assert len(m) == len(l)
    s = [0, 0]
    for t in m:
        xa, ya, xb, yb, xp, yp = map(int, t)
        for part in (1, 2):
            if part == 2:
                xp += 10000000000000
                yp += 10000000000000
            # xa * a + xb * b = xp
            # ya * a + yb * b = yp
            # find a, b
            # a = (xp - xb * b) / xa
            # b = ( yp - ya * a ) /yb
            # b = ( yp - ya *((xp - xb * b) / xa) )/ yb)
            # b - b * l = k
            # b = k / (1 - l)
            k = yp / yb - ya * xp / xa / yb
            l = ya * xb / xa / yb
            b = int(math.floor((k / (1 - l)) + 0.1))
            a = int(math.floor((xp - xb * b) / xa + 0.1))
            if xa * a + xb * b == xp and ya * a + yb * b == yp:
                s[part - 1] += a * 3 + b
    print(s)
