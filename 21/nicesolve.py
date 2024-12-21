import functools
import sys

inp = """\
029A
980A
179A
456A
379A
"""

# inp = """\
# 029A
# """

numpad = {
    "A": (("0", "<"), ("3", "^")),
    "0": (("A", ">"), ("2", "^")),
    "1": (("2", ">"), ("4", "^")),
    "2": (("0", "v"), ("3", ">"), ("1", "<"), ("5", "^")),
    "3": (("A", "v"), ("2", "<"), ("6", "^")),
    "4": (("1", "v"), ("5", ">"), ("7", "^")),
    "5": (("2", "v"), ("4", "<"), ("6", ">"), ("8", "^")),
    "6": (("3", "v"), ("5", "<"), ("9", "^")),
    "7": (("8", ">"), ("4", "v")),
    "8": (("9", ">"), ("5", "v"), ("7", "<")),
    "9": (("6", "v"), ("8", "<")),
}

dirpad = {
    "A": (("^", "<"), (">", "v")),
    "^": (("A", ">"), ("v", "v")),
    ">": (("A", "^"), ("v", "<")),
    "v": ((">", ">"), ("<", "<"), ("^", "^")),
    "<": (("v", ">"),),
}

"""
best is 'A', '>', 'v', '<', 
best is '<', 'v', '^', 'A', 
best is 'A', '^', 
best is '^', 'A', 
best is 'A', '>', 'v
best is '>', 'v', '^', 
best is 'A', '>', 'v', 
best is 'v', '^', 'A', 
best is 'v', '<', 
best is '^', 'v', '>', 
best is '>', 'A', 
best is '<', 'v', '^', 
best is 'v', '>', 
best is '^', 'v', '<', 
"""

cache = {}
def stepsFromDirPad(start, stop, depth=3, noopt=None):
    global cache
    if (depth==3 and (start[0], stop) in cache):
        return (*cache[(start[0], stop)],)
    if start[0] == stop:
        return ((start,),)
    elif depth > 0:
        minlen = None
        res = []
        for i in sorted(
            [
                (start, *c)
                for d in dirpad[start[0]]
                for c in stepsFromDirPad(d, stop, depth - 1, noopt=noopt)
                if c[-1][0] == stop
            ],
            key=len,
        ):
            if minlen is None:
                minlen = len(i)
            if len(i) > minlen:
                break
            res.append(i)
        if (depth==3) and not noopt:
            # figure out the best candidate
            best = None
            shortes = None
            candidateshort = 0
            for c in res:
                candidateshort = len(sorted(runString("".join(map(lambda c: c[1], [(None, 'A'), *c[1:]])),stepsFromDirPad, noopt=True), key=len)[0])
                if shortes is None or candidateshort < shortes:
                    shortes = candidateshort
                    best = c
            res = [best]
            print(len(cache))
            cache[(start[0], stop)] = res
        return (*res,)
    return ()


def stepsFromNumPad(start, stop, depth=5, noopt=None):
    if start[0] == stop:
        return ((start,),)
    elif depth > 0:
        minlen = None
        res = []
        for i in sorted( [
                (start, *c)
                for d in numpad[start[0]]
                for c in stepsFromNumPad(d, stop, depth - 1, noopt=noopt)
                if c[-1][0] == stop
            ],
            key=len,
        ):
            if minlen is None:
                minlen = len(i)
            if len(i) > minlen:
                break
            res.append(i)
        return (*res,)
    return ()

def getvariants(char, prev, func, noopt):
    return [[d[1] for d in c[1:]] for c in func((prev, None), char, noopt=noopt)]

def runString(inp, func, noopt=False):
    prev = "A"
    candidates = ([],)
    for char in inp:
        variants = getvariants(char, prev, func, noopt=noopt)
        prev = char
        candidates = [
            [x for x in (*candidate, *variant, "A")]
            for candidate in candidates
            for variant in variants
        ]
    return {"".join(candidate) for candidate in candidates}


with open(sys.argv[1]) as f:
    inp = f.read()
    summa = 0
    for line in inp.strip().split("\n"):
        # res = {
        #     c
        #     for a in runString(line, stepsFromNumPad)
        #     for b in runString(a, stepsFromDirPad)
        #     for c in runString(b, stepsFromDirPad)
        # }
        res = runString(line, stepsFromNumPad)
        for i in range(0,8):
            print(f"{i} {len(res)}")
            res = {q for r in res for q in runString(r, stepsFromDirPad)}
        add = len(sorted(res, key=len)[0]) * int(line[:-1])
        summa += add
    print(summa)
