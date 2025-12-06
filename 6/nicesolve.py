import sys
import re

with open(sys.argv[1]) as f:
    sums = []
    ops = []
    #l = f.read().split("\n")
    for i, l in enumerate(reversed([l for l in f.read().split("\n") if l])):
        elems = l.strip().split()
        print(elems, i)
        for j, e in enumerate(elems):
            if i == 0:
                ops.append((lambda x,y: x*y) if e == "*" else (lambda x,y: x+y))
            elif i == 1:
                sums.append(int(e))
            else:
                sums[j] = ops[j](sums[j],int(e))
            print(sums)
    print(sum(sums))
