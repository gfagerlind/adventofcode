import sys
from itertools import combinations
from operator import sub, pow
from math import prod

with open(sys.argv[1]) as f:
    points = {tuple(map(int, l.split(","))) for l in f.read().split("\n") if l}
    collections = [{p} for p in points]
    weighted_pairs = sorted(combinations(points, 2), key=lambda x: sum(map(pow, map(sub, x[0], x[1]), (2, 2, 2))))
    for i, (a,b) in enumerate(weighted_pairs):
        collections_to_merge = [c for c in collections if a in c or b in c]
        for c in collections_to_merge:
            collections.pop(collections.index(c))
        collections.append({p for c in collections_to_merge for p in c})
        if i == 9:
            print(prod(sorted(map(len,collections))[-3:]))
        if i == 999:
            print(prod(sorted(map(len,collections))[-3:]))
        if len(collections) == 1:
            print(a[0] * b[0])
            break
