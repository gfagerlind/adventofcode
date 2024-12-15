import sys
import re
import math

inp = """\
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""

# inp = """\
# ########
# #..O.O.#
# ##@.O..#
# #...O..#
# #.#.O..#
# #...O..#
# #......#
# ########

# <^^>>>vv<v>>v<<
# """
inp = """\
#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^
"""
def char2move(s):
    if s == '<':
        return -1j
    if s == '>':
        return 1j
    if s == '^':
        return -1
    if s == 'v':
        return 1

def pp(s, lx, ly):
    for x in range(lx):
        for y in range(ly):
            if (x + 1j * y) in s:
                print(s[(x + 1j * y)], end="")
            else:
                print(".", end="")
        print("")

def push(p, d, cords,attempt=False):
    np = cords.get(p+d,'None')
    print(p+d,np)
    if np == '#':
        return False
    if np in 'O[]' and not push(p+d, d, cords, attempt=attempt):
        return False
    if np in '[]' and d not in (-1j,1j):
        if not push(p+d, d, cords, attempt=True):
            return False
        if np == '[' and not push(p+d + 1j, d, cords, attempt=True):
            return False
        if np == ']' and not push(p+d - 1j, d, cords, attempt=True):
            return False
        push(p+d, d, cords)
        if np == '[':
            push(p+d + 1, d, cords)
        if np == ']':
            push(p+d - 1, d, cords)
    if attempt:
        return True
    if p in cords:
        print(f'moving {cords[p]} from {p} to {p+d}')
        cords[p+d] = cords.pop(p)
    return True

with open(sys.argv[1]) as f:
    # inp = f.read()
    inp_s, moves = inp.split("\n\n")
    inp_s = inp_s.split('\n')
    cords = {
        x + y * 1j: inp_s[x][y] for x in range(len(inp_s)) for y in range(len(inp_s[x]))
    }
    cords2 = {}
    for x in range(len(inp_s)):
        for y in range(len(inp_s[x])):
            v = inp_s[x][y]
            if v == '#':
                cords2[x + y*2 * 1j] = v
                cords2[x + y*2 * 1j + 1j] = v
            if v == 'O':
                cords2[x + y*2 * 1j] = '['
                cords2[x + y*2 * 1j + 1j] = ']'
            if v == '@':
                cords2[x + y*2 * 1j] = '@'
    moves = [char2move(m) for m in moves.replace('\n','')]
    print(cords2, '\n', moves)
    rp = [k for k,v in cords2.items() if v =="@"][0]
    print(rp)
    for i,m in enumerate(moves):
        print(i,m)
        pp(cords2, 10,20)
        if push(rp, m, cords2):
            rp = rp+m
    pp(cords2, 10,20)
    print(sum(100 * p.real + p.imag for p,v in cords.items() if v in 'O['))
