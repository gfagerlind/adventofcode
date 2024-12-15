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
# inp = """\
# #######
# #...#.#
# #.....#
# #..OO@#
# #..O..#
# #.....#
# #######

# <vv<<^^<<^^
# """
def char2move(s):
    if s == '<':
        return -1j
    if s == '>':
        return 1j
    if s == '^':
        return -1
    if s == 'v':
        return 1

def move2char(s):
    if s == -1j:
        return '<'
    if s == 1j:
        return '>'
    if s == -1:
        return '^'
    if s == 1:
        return 'v'

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
    if np == '#':
        return False
    if np in '[]' and d in (-1,1):
        if np == '[':
            ps = p+1j
        else:
            ps = p-1j
        if not push(p+d,d,cords, attempt=True):
            return False
        if not push(ps+d,d,cords, attempt=True):
            return False
        if attempt:
            return True
        else:
            push(p+d, d, cords)
            push(ps+d,d,cords)
    elif np in 'O[]' and not push(p+d, d, cords):
        # no attempt needed due since Os are only in variant 1,
        # and [] pushed up or down are caught above
        return False
    if p in cords and not attempt:
        cords[p+d] = cords.pop(p)
    return True

with open(sys.argv[1]) as f:
    inp = f.read()
    inp_s, moves = inp.split("\n\n")
    inp_s = inp_s.split('\n')
    cords1 = {
        x + y * 1j: inp_s[x][y] for x in range(len(inp_s)) for y in range(len(inp_s[x]))
    }
    cords1['@'] = [k for k,v in cords1.items() if v =="@"][0]
    cords2 = {}
    for x in range(len(inp_s)):
        for y in range(len(inp_s[x])):
            v = inp_s[x][y]
            bp = x + y*2 * 1j
            if v == '#':
                cords2[bp] = v
                cords2[bp + 1j] = v
            if v == 'O':
                cords2[bp] = '['
                cords2[bp + 1j] = ']'
            if v == '@':
                cords2[bp] = '@'
                cords2['@'] = bp
    moves = [char2move(m) for m in moves.replace('\n','')]
    for i,m in enumerate(moves):
        for cords in cords1, cords2:
            if push(cords['@'], m, cords):
                cords['@'] += m
    print(sum(100 * p.real + p.imag for p,v in cords1.items() if p != '@' and v in 'O['))
    print(sum(100 * p.real + p.imag for p,v in cords2.items() if p != '@' and v in 'O['))
