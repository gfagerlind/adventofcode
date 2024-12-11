import sys
import math
import functools

inp = """\
0 1 10 99 999
"""

inp = """\
125 17
"""
@functools.cache
def get_len(number, depth):
    if depth == 0:
        return 1
    depth -= 1
    if number == 0:
        return get_len( 1, depth)
    num_as_str = str(number)
    if len(num_as_str) % 2 == 0:
        half = int(len(num_as_str)/2)
        return get_len(int(num_as_str[:half]), depth) + get_len(int(num_as_str[half:]), depth)
    return get_len(number * 2024, depth)

with open(sys.argv[1]) as f:
    inp = f.read()
    inp = list(map(int, inp.split()))
    print(sum([get_len(n, 25) for n in inp]))
    print(sum([get_len(n, 75) for n in inp]))
