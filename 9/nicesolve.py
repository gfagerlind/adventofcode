import sys

inp = """\
2333133121414131402
"""


# inp = """\
# 12345
# """
def to_list(a_list: list):
    return [fid for fid, size in a_list for _ in range(size)]


with open(sys.argv[1]) as fo:
    inp = fo.read()
    # padd input to align
    inp = inp.strip() + "0"
    blocks = []
    blocks_part2 = []
    count = 0
    for file, free in zip(*(map(int, iter(inp)),) * 2):
        blocks.extend([*(file * [count]), *(free * ["."])])
        blocks_part2.extend([(count, file), (".", free)])
        count += 1
    packed1 = []
    for c in blocks:
        if c == ".":
            while (c := blocks.pop()) == ".":
                pass
        packed1.append(c)
    for i in range(len(blocks_part2) - 1, 0, -1):
        fid, size = blocks_part2[i]
        if fid == ".":
            continue
        for j, (b, s) in enumerate(blocks_part2[0:i]):
            if b != ".":
                continue
            if size <= s:
                # print(f"swapping {j} {blocks_part2[j]} and {i} {blocks_part2[i]}")
                blocks_part2[j] = (b, s - size)
                blocks_part2[i] = (".", size)
                # here we push what i points to with insert, but since every block
                # is matched with a free block from the get go we dont miss anything
                blocks_part2.insert(j, (fid, size))
                break
    assert 6288707484810 == sum(i * int(c) for i, c in enumerate(packed1))
    assert 6311837662089 == sum(
        i * int(c) for i, c in enumerate(to_list(blocks_part2)) if c != "."
    )
    print(sum(i * int(c) for i, c in enumerate(packed1)))
    print(sum(i * int(c) for i, c in enumerate(to_list(blocks_part2)) if c != "."))
