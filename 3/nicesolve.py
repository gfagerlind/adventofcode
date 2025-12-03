import sys


with open(sys.argv[1]) as f:
    nums = [[int(a) for a in l] for l  in f.read().split() ]
    sum1 = 0
    lsum = 0
    for n in nums:
        second = max(n[n.index(first:=max(n[:-1]))+1:])
        sum1 += 10*first + second
        pos = 0
        for i in range(0,12):
            currslice = n[pos:-11+i] if 11 > i else n[pos:]
            found = max(currslice)
            lsum += (10**(11 - i)) * found
            pos += currslice.index(found) + 1
    print(sum1, lsum)
