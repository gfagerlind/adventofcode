import sys
import functools

inp = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
"""

with open(sys.argv[1]) as f:
    inp = f.read()
    inp = inp.split("\n")
    patterns = inp[0].split(", ")
    data = inp[1:]
    possible = 0
    permpossible = 0

    @functools.cache
    def recurse(substring):
        if not substring:
            return 1
        sum = 0
        for p in patterns:
            if substring.startswith(p):
                sum += recurse(substring[len(p) :])
        return sum

    for i, d in enumerate(data):
        if d and (tot := recurse(d)):
            print(f"{d} has {tot}")
            possible += 1
            permpossible += tot
    print(possible, permpossible)
