import sys

sizes = [7, 7, 7, 7, 6, 5]
with open(sys.argv[1]) as f:
    res = 0
    for l in f.read().split("\n"):
        if "x" in l:
            area, count = l.split(":")
            x, y = map(int, area.split("x"))
            area = int(x) * int(y)
            count = list(map(int, count.split()))
            if x // 3 * y // 3 >= sum(count):
                print("trivially fits")
                res += 1
            elif area <= sum([sizes[i] * count[i] for i in range(len(count))]):
                print("trivially dont fit")
            else:
                print(
                    area, count, sum([sizes[i] * count[i] for i in range(len(count))])
                )
                print(x // 3 * y // 3, sum(count))
    print(res)
