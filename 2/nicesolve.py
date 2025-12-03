import sys


with open(sys.argv[1]) as f:
    sets = [[int(i) for i in p.split('-')] for p in f.read().strip().split(",")]
    summa_1 = 0
    summa_2 = 0
    for s in sets:
        for i in range(s[0], s[1] + 1):
            l = str(i)
            le = len(l)
            for sl in range(le // 2,0,-1):
                q,r = divmod(le,sl)
                if r == 0 and l[:sl]*q == l:
                    summa_2 += i
                    if le / sl == 2:
                        summa_1 += i
                    break
    print(summa_1, summa_2)
