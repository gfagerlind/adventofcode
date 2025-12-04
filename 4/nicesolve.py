import sys

with open(sys.argv[1]) as f:
    rolls = {
        x + y * 1j
        for x, l in enumerate(f.read().split("\n"))
        for y, alpha in enumerate(l)
        if alpha == "@"
    }
    start = len(rolls)
    first = True
    while True:
        before = len(rolls)
        rolls = {
            r
            for r in rolls
            if not 4
            >= len(
                [
                    r + dx + dy * 1j
                    for dx in range(-1, 2)
                    for dy in range(-1, 2)
                    if r + dx + dy * 1j in rolls
                ]
            )
        }
        if first:
            print(start - len(rolls))
            first = False
        if len(rolls) == before:
            break
    print(start - len(rolls))
