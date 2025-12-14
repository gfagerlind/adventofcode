import sys
import re
import numpy as np
import scipy
def bitfield_as_str(i):
    return '{0:b}'.format(i)
def stupid_method(m,a, g):
    cs = {tuple(a)}
    found = False
    while not found:
        new_cs = set()
        for a in cs:
            res = g - np.matmul(m,np.array(a))
            if len(np.where(res < 0)[0]) > 0:
                continue
            if not any(res):
                print(f"whoho {a}")
                found = True
            for i in range(len(a)):
                b = [*a]
                b[i] += 1
                new_cs.add(tuple(b))
        cs = new_cs
with open(sys.argv[1]) as f:
    tot_sum = 0
    for l in f.read().split("\n"):
        if not l:
            continue
        buttons = set()
        matrix = np.zeros((17,17))
        c = 0
        for chunk in l.split():
            match chunk[0]:
                case '[':
                    goal = sum((1 if c == "#" else 0) << i for i, c in enumerate(chunk[1:-1]))
                case '(':
                    buttons.add(sum(1 << int(c)  for c in chunk[1:-1].split(',')))
                    for j in map(int,chunk[1:-1].split(',')):
                        matrix[j,c] = 1
                    c += 1
                case '{':
                    sum_goal = np.array([*map(int,chunk[1:-1].split(','))]).T
        states = {0}
        #m = np.column_stack((matrix[:sum_goal.shape[0],:c],sum_goal))
        m = matrix[:sum_goal.shape[0],:c]
        # test = np.array([1,3,0,3,1,2])
        # print(np.matmul(m, test))
        print(sum_goal)
        # print(all(sum_goal.T == np.matmul(m, test)))
        #print(scipy.linalg.lu(m, permute_l=True, check_finite=False)[1])
        print(m)
        res = stupid_method(m,np.zeros((c,)),sum_goal)
        print(res)
        print('net')
    print(tot_sum)

