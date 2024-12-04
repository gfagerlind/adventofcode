#!/bin/python
import sys
from collections import Counter, defaultdict


def createDict(l):
    return defaultdict(lambda: 0, Counter(l))


with open(sys.argv[1]) as f:
    columns = tuple(zip(*[map(int, line.split()) for line in f.readlines()]))
    # sort the two columns, zip them, apply the absolut diff and sum it
    print(sum(map(lambda a, b: abs(a - b), *map(sorted, columns))))
    # use Counter to get a dict with the key of the element, and the value of the number of duplicates
    # default to 0
    a, b = map(createDict, columns)
    print(sum(k * a[k] * b[k] for k in a))
