import sys
import re
import math

inp = """\
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""
inp = """\
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
"""

with open(sys.argv[1]) as f:
    inp = f.read()
    oa,ob,oc, rawp = re.findall(
        r"Register A: (\d+)\n"
      + r"Register B: (\d+)\n"
      + r"Register C: (\d+)\n\n"
      + r"Program: ([\d,]+)",
        inp,
        re.MULTILINE,
    )[0]
    a,b,c = int(oa), int(ob), int(oc)
    p = list(map(int,rawp.split(',')))
    # a = 0
    # b = 2024
    # c = 43690
    # p = [4,0]
    print(a,b,c,p)
    def co(a,b,c,op):
        if op < 4:
            return op
        if op == 4:
            return a
        if op == 5:
            return b
        if op == 6:
            return c
        if op == 5:
            assert False, "error"
    out = []
    ip = 0
    # 1 -> 3
    # 2 -> 1
    # 3 -> 0
    # 4 -> 5
    # 5 -> 3
    # 6 -> 5
    # 7 -> 5
    # 8 -> 3
    # 9 -> 2
    #Program: 2,4,1,5,7,5,1,6,0,3,4,3,5,5,3,0
    #         2,4,1,2,3,1,3,2,5,4,1,3,7,2
    #         2,4,1,2,3,5,1,2,3,4,1,3,7,2
    #         3,3,3,3,3,3,3,3,3,3,3,1,3,2
    #         3,3,3,3,3,3,3,3,3,3,3,3,3,1,3,2
    while ip < len(p):
        op = p[ip+1]
        match p[ip]:
            case 0:
                a = a // (2 ** co(a,b,c, op))
            case 1:
                b = b ^ op
            case 2: #bst
                b = co(a,b,c,op) % 8
:q
:q
:qa
:qa
            case 3: # jnz
                if a != 0:
                    ip = op
                    continue
            case 4:
                b = b ^ c
            case 5:
                out.append(co(a,b,c,op) % 8)
            case 6: # bdv
                b = a // (2 ** co(a,b,c, op))
            case 7:
                c = a // (2 ** co(a,b,c, op))
        ip += 2
    print(",".join(map(str,out)))
    print(",".join(map(str,p)))
