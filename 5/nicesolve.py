import sys

with open(sys.argv[1]) as f:
    sets = []
    numbers = []
    for l in f.read().split("\n"):
        if len(k:=l.split("-"))==1:
            if l:
                numbers.append(int(k[0]))
        else:
            sets.append((int(k[0]),int(k[1]),))
    sets = sorted(sets, key=lambda x: x[0])
    startid = None
    stopid = None
    new_sets = []
    for i, (l, h) in enumerate(sets):
        startid = l if l-1 > (stopid or 0) else startid
        stopid = max(stopid or 0, h)
        if i+1 == len(sets) or stopid < sets[i+1][0] - 1:
            new_sets.append((startid,stopid,))
    print(len([n for n in numbers if any(l<= n <=h for l,h in new_sets)]))
    print(sum(h-l+1 for l,h in new_sets))
