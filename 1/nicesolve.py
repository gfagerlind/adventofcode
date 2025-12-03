#!/bin/python
with open("input2") as f:
    first_res = 0
    third_res = 0
    res = 50
    for i in f.read().split():
        update = int(i[1:])
        sign = 1 if i[0] == "R" else (-1)
        if sign == 1:
            third_res += (update + res) // 100
        else:
            third_res += (update + 100 - (res or 100)) // 100
        res = (res + update * sign) % 100
        if not res:
            first_res += 1
    print(first_res, third_res)
