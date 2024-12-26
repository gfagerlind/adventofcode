import sys
import collections
from collections import defaultdict


sys.setrecursionlimit(2100)
inp = """\
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
"""

with open(sys.argv[1]) as f:
    inp = f.read()
    inp = inp.strip().split("\n")
    links = defaultdict(set)
    for l in inp:
        x, y = l.split('-')
        links[x].add(y)
        links[y].add(x)
    res = set()
    res2 = set()
    of = len(links)
    for k, tlinks in links.items():
        print(f"{k} {of}")
        if k.startswith('t'):
            for l in tlinks:
                for j in links[l] & tlinks:
                    res.add(tuple(sorted([k,l,j])))
        res3 = set([(k,)])
        for t in res2:
            st = set(t)
            if st.intersection(tlinks) >= st:
                # print(f"testing {st} and {tlinks} {st.intersection(tlinks)}")
                res3.add(tuple([*t,k]))
        res2.update(res3)
    print(len(res))
    print(",".join(sorted(sorted(res2, key=len, reverse=True)[0])))
