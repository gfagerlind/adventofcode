import sys
from collections import defaultdict
from itertools import permutations

inp = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""


def create_right_list(l, r):
    out = []
    for e in l:
        out.insert(next((i for i in range(len(out)) if out[i] in r[e]), len(out)), e)
    return out


def manage_page(p, ruledict):
    pages = p.split(",")
    altpage = create_right_list(pages, ruledict)
    mid = int(altpage[int((len(pages) - 1) / 2)])
    if pages == altpage:
        return mid, 0
    else:
        return 0, mid


with open(sys.argv[1]) as f:
    rules, pagesets = f.read().split("\n\n")
    ruledict = defaultdict(set)
    for l in rules.split():
        x, y = l.split("|")
        ruledict[x].add(y)
    print([sum(x) for x in zip(*[manage_page(p, ruledict) for p in pagesets.split()])])
