import sys
from collections import defaultdict

with open(sys.argv[1]) as f:
    beams = defaultdict(int)
    split_count = 0
    for l in f.read().split("\n"):
        for i, c in enumerate(l):
            if c == "^" and i in beams:
                split_count += 1
                worlds = beams.pop(i)
                beams[i - 1] += worlds
                beams[i + 1] += worlds
            elif c == "S":
                beams[i] = 1
    print(split_count, sum(beams.values()))
