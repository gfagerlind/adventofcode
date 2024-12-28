import functools
import sys

inp = """\
029A
980A
179A
456A
379A
"""
idealmoves = {
    ("<", "A"): (">", ">", "^", "A"),
    ("<", "^"): ( ">", "^", "A"),
    (">", "A"): ("^", "A"),
    (">", "^"): ('<', '^',  'A'),
    (">", "v"): ("<", "A"),
    ("A", "<"): ("v", "<", "<", "A"),
    ("A", ">"): ("v", "A"),
    ("A", "^"): ("<", "A"),
    ("A", "v"): ("<", "v", "A"),
    ("^", "<"): ("v", "<", "A"),
    ("^", ">"): ("v", ">", "A"),
    ("^", "A"): (">", "A"),
    ("v", "<"): ("<", "A"),
    ("v", ">"): (">", "A"),
    ("v", "A"): ("^", ">","A"),
    ("A", "A"): ("A",),
    (">", ">"): ("A",),
    ("<", "<"): ("A",),
    ("<", "v"): (">", "A",),
    ("^", "^"): ("A",),
    ("v", "v"): ("A",),
}


@functools.cache
def lenOfNumpad(string, depth):
    if depth == 0:
        # print(string,end='')
        return len(string)
    return sum(lenOfNumpad(idealmoves[(string[i-1] if i > 0 else 'A', char)], depth - 1) for i, char in enumerate(string))


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
 ('<', 'A'),
 ('<', '^'),
 ('>', 'A'),
 ('>', '^')])
 ('>', 'v'),
 ('A', '<'),
 ('A', '>'),
 ('A', '^'),
 ('A', 'v'),
 ('^', '<'),
 ('^', 'A'),
 ('v', '<'),
 ('v', '>'),
 ('v', 'A'),
"""

def stepsFromDirPad(start, stop, depth=3, noopt=None):
    if start[0] == stop:
        return ((start,),)
    if depth > 0:
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
        return (*res,)
    return ()


def stepsFromNumPad(start, stop, depth=5, noopt=None):
    if start[0] == stop:
        return ((start,),)
    elif depth > 0:
        minlen = None
        res = []
        for i in sorted(
            [
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
        res = runString(line, stepsFromNumPad)
        add = min(lenOfNumpad(c, 25) for c in res) * int(line[:-1])
        summa += add
    print('')
    print(summa)
