import sys
import bisect
import functools
from enum import Enum

inp = """\
029A
980A
179A
456A
379A
"""

numpad = {
    'A': ((0, '<'),(3, '^')),
    0: (('A', '>'),(2, '^')),
    1: ((2, '>'),(4,'^')),
    2: ((0,'v'),(3, '>'),(1, '<'),(5, '^')),
    3: (('A', 'v'), (2, '<'),(6, '^'))
    4: ((1, 'v'),(5, '>'),(7, '^')),
    5: ((2, 'v'),(4, '<'),(6, '>'),(8, '^')),
    6: ((3, 'v'),(5, '<'),(9, '^')),
    7: ((8, '>'),(4, 'v')),
    8: ((9, '>'),(5, 'v'),(7,'<')),
    9: ((6, 'v'),(8, '<')),
}

dirpad = {
    'A': (('^', '<'),('>', 'v')),
    '^': (('A', '>'),('v', 'v')),
    '>': (('A', '^'), ('v', '<')),
    'v': (('>', '>'), ('<', '<'), ('^', '^')),
    '<': (('v', '>')),
}
@functools.cache
def stepsFromDirPad(start, stop, depth):
    pass

@functools.cache
def stepsFromNumPad(start, stop, route, depth):
    if res := numpad.get(start):
        return [res]
    elif depth > 0:
        candidates = []
        for d in numpad[start]:
            if d[0] not in route:
                candidates.append(stepsFromNumPad(d[0], stop, route | {d[0]}, depth - 1))
        min(candidates)

with open(sys.argv[1]) as f:
    # inp = f.read()
    inp = inp.strip().split("\n")
    for l in inp:
        keys = []
        prev = ['A', 'A', 'A']
        for c in l:
            stepsFromDirPad(None, c)
