import sys
import re

inp = """\
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

with open(sys.argv[1]) as f:
    inp = f.read()
    calibs = {
        int(re.findall(r"\d+", l)[0]): map(int, re.findall(r"\d+", l)[1:])
        for l in inp.split("\n")
        if len(l)
    }
    tot_sum = 0
    tot_concat_sum = 0
    for calib, nums in calibs.items():
        multi_plus_sums = set([1])
        concat_sums = set()
        for n in nums:
            added_concat_sums = {
                int(str(c) + str(n)) for c in multi_plus_sums if c <= calib
            }
            multi_plus_sums = {
                p for c in multi_plus_sums for p in (c * n, c + n) if c <= calib
            }
            concat_sums = (
                {
                    p
                    for c in concat_sums
                    for p in (c * n, c + n, int(str(c) + str(n)))
                    if c <= calib
                }
                | added_concat_sums
                | multi_plus_sums
            )

        if calib in multi_plus_sums:
            tot_sum += calib
            tot_concat_sum += calib
        elif calib in concat_sums:
            tot_concat_sum += calib
    print(tot_sum, tot_concat_sum)
