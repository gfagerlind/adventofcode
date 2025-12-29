import sys
from itertools import combinations
import collections
import functools

with open(sys.argv[1]) as f:
    i = collections.defaultdict(set)
    for l in f.read().split("\n"):
        if not l:
            continue
        key, vals = l.split(":")
        for v in vals.strip().split():
            i[v].add(key)

    @functools.cache
    def recurse(start, stop):
        tal, tvia_fft, tvia_dac, tvia_both = 0, 0, 0, 0
        if start == stop:
            return (1, 0, 0, 0)
        for k in i[stop]:
            al, via_fft, via_dac, via_both = recurse(start, k)
            if k == "fft":
                tvia_fft += al
                tvia_both += via_dac
            if k == "dac":
                tvia_dac += al
                tvia_both += via_fft
            tal += al
            tvia_fft += via_fft
            tvia_dac += via_dac
            tvia_both += via_both
        return tal, tvia_fft, tvia_dac, tvia_both

    print(recurse("you", "out")[0])
    print(recurse("svr", "out")[3])
