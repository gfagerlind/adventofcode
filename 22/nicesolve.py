import sys
import collections

sys.setrecursionlimit(2100)
inp = """\
1
10
100
2024
"""
inp = """\
1
2
3
2024
"""


def nextseed(seed, currentset, allsets, i, depth=0):
    """

    Calculate the result of multiplying the secret number by 64. Then, mix this result into the secret number. Finally, prune the secret number.
    Calculate the result of dividing the secret number by 32. Round the result down to the nearest integer. Then, mix this result into the secret number. Finally, prune the secret number.
    Calculate the result of multiplying the secret number by 2048. Then, mix this result into the secret number. Finally, prune the secret number.
    """
    if depth == 2000:
        print(seed)
        allsets.append({})
    before = seed % 10
    seed = ((seed << 6) ^ seed) & 16777215
    seed = (seed >> 5) ^ seed
    seed = ((seed << 11) ^ seed) & 16777215
    currentset.append((seed % 10) - before)
    # print(f"{seed=} {before=} {tuple(currentset)}")
    if len(currentset) == 4 and tuple(currentset) not in allsets[i]:
        allsets[i][tuple(currentset)] = seed % 10
    if depth > 1:
        return nextseed(seed, currentset, allsets, i, depth=depth - 1)
    return seed


# nextseed(123,collections.deque(maxlen=4), [], 0, depth=7)

with open(sys.argv[1]) as f:
    inp = f.read()
    summa = 0
    inp = inp.strip().split("\n")
    allsets = []
    print(
        sum(
            nextseed(int(line), collections.deque(maxlen=4), allsets, i, depth=2000)
            for i, line in enumerate(inp)
        )
    )
    max = 0
    for k in set(k for s in allsets for k in s):
        # look for k in each dict of all elements in all sets and sum up.
        # max sum is the key
        # print(k)
        # print([s[k] for s in allsets if k in s])
        candidate = sum(s.get(k, 0) for s in allsets)
        if candidate > max:
            max = candidate
            # print(k)
    print(max)
