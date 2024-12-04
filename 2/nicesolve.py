import sys

inp = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
1 1 2 4 5
8 6 4 4 1
1 3 6 7 9""".split(
    "\n"
)


def is_row_ok(row):
    # create a set of all diffs, they should all be 1 - 3, and they should
    # all have the same value (not my original idea)
    s = set(row[i + 1] - row[i] for i in range(len(row) - 1))
    return s <= {1, 2, 3} or s <= {-1, -2, -3}


with open(sys.argv[1]) as f:
    d = [[int(e) for e in line.split()] for line in f.readlines()]
    print(sum(map(is_row_ok, d)))
    print(sum(any(is_row_ok(r[:i] + r[i + 1 :]) for i in range(len(r))) for r in d))
