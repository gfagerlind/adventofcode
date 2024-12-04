import sys
import re

REGEX = r"mul\((\d{1,3}),(\d{1,3})\)"
REGEX2 = r"((^|do\(\)).*?(don\'t\(\)|$))"


def regex_multiply_sum(txt):
    return sum(int(a) * int(b) for a, b in re.findall(REGEX, txt))


with open(sys.argv[1]) as f:
    txt = f.read().replace("\n", "")
    print(regex_multiply_sum(txt))
    print(regex_multiply_sum("".join(l[0] for l in re.findall(REGEX2, txt))))
