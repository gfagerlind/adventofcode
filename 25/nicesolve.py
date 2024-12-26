import sys
import collections

inp = """\
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
"""


def fits(key, lock):
    return not sum(k + l >= 6 for k, l in zip(key, lock))


with open(sys.argv[1]) as f:
    inp = f.read()
    inp = inp.strip().split("\n\n")
    locks = []
    keys = []
    for lock in inp:
        keyorlock = tuple(
            map(lambda x: collections.Counter(x)["#"] - 1, zip(*lock.split("\n")))
        )
        if lock[0] == "#":
            locks.append(keyorlock)
        else:
            keys.append(keyorlock)
    print(sum(fits(key, lock) for lock in locks for key in keys))
