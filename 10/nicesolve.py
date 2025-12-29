import sys
import re
from functools import cache, reduce
from itertools import chain, combinations
from collections import defaultdict
def bitfield_as_str(i):
    return '{0:b}'.format(i)
with open(sys.argv[1]) as f:
    part1_sum = 0
    part2_sum = 0
    for l in f.read().split("\n"):
        if not l:
            continue
        buttons = []
        for chunk in l.split():
            match chunk[0]:
                case '[':
                    goal = tuple((1 if c == "#" else 0) for c in chunk[1:-1])
                case '(':
                    buttons.append(tuple(int(c)  for c in chunk[1:-1].split(',')))
                case '{':
                    sum_goal = tuple(map(int,chunk[1:-1].split(',')))
        all_button_combinations = set()
        for x in range(len(buttons)+1):
            all_button_combinations.update(combinations(range(len(buttons)),x))
        parity_dict = defaultdict(list)
        sum_pressed = {}
        for bc in all_button_combinations:
            sum_p = [0] * len(sum_goal)
            for b in bc:
                for i in buttons[b]:
                    sum_p[i] += 1
            parity = tuple(i %2 for i in sum_p)
            parity_dict[parity] += [bc]
            sum_pressed[bc] = sum_p
        @cache
        def solve(sum_goal, depth):
            if min(sum_goal) < 0:
                # if overshoot
                return 9999999999999
            if sum(sum_goal) == 0:
                # if done
                return 0
            best = 9999999999999
            parity = tuple(i %2 for i in sum_goal)
            # look for parity
            for bc in parity_dict[parity]:
                # Not my own idea, but when you have an even set to push, to ideally press half of it twice will be the ideal way to push the whole
                # find rest
                rest = tuple((i-sum) // 2 for i, sum in zip(sum_goal, sum_pressed[bc]))
                best = min(best, len(bc) + 2 * solve(rest, depth+1))
            print(sum_goal, best, depth)
            return best
        part1_sum += min(map(len,parity_dict[goal]))
        print(mysum:=solve(sum_goal, depth=0))
        part2_sum += mysum
        print('--------------------------')
    print(part1_sum)
    print(part2_sum)
