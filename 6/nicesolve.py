import sys
import re
lambdas = {
    "*": (lambda x,y: x*y),
    "+": (lambda x,y: x+y)
}
with open(sys.argv[1]) as f:
    sums = []
    ops = []
    rawlines = []
    for i, l in enumerate(reversed([l for l in f.read().split("\n") if l])):
        rawlines.append(l)
        for j, e in enumerate(l.strip().split()):
            if i == 0:
                ops.append(lambdas[e])
            elif i == 1:
                sums.append(int(e))
            else:
                sums[j] = ops[j](sums[j],int(e))
    print(sum(sums))
    sums2 = []
    local_sum = 0
    for i in range(0, len(rawlines[0])):
        ops = ops if rawlines[0][i] == " " else lambdas[rawlines[0][i]]
        num = "".join(rawlines[j][i] for j in range(len(rawlines)-1, 0, -1)).strip()
        if not num:
            sums2.append(local_sum)
            local_sum = 0
        else:
            local_sum  = ops(local_sum, int(num)) if local_sum else int(num)
    sums2.append(local_sum)
    print(sum(sums2))
