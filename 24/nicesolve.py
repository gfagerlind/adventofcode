import sys
import collections
import functools

sys.setrecursionlimit(100)
inp = """\
x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj
"""
maxbit=12

with open(sys.argv[1]) as f:
    inp = f.read(); maxbit=45
    summa = 0
    system = {}
    @functools.cache
    def func(i1, op=None, i2=None):
        if op is None:
            return i1[0]
        match op:
            case 'XOR':
                return func(*system[i1]) ^ func(*system[i2])
            case 'OR':
                return func(*system[i1]) | func(*system[i2])
            case 'AND':
                return func(*system[i1]) & func(*system[i2])
    @functools.cache
    def func2(i1, op=None, i2=None):
        if op is None:
            print(i1, i2)
            return str(i2)
        l = sorted([func2(*system[i1]),func2(*system[i2])])
        match op:
            case 'XOR':
                return f"( {l[0]} ) ^ ( {l[1]} )"
            case 'OR':
                return f"( {l[0]} ) | ( {l[1]} )"
            case 'AND':
                return f"( {l[0]} ) & ( {l[1]} )"
    inp, inp2 = inp.strip().split("\n\n")
    for l in inp.split('\n'):
        k, v = l.split(': ')
        system[k] = [(int(v),),None, k]
    for l in inp2.split('\n'):
        i1, op, i2, _, out = l.split()
        system[out] = (i1, op, i2)
    bits = "".join(str(func(*system[f"z{k:02}"])) for k in range(maxbit,-1, -1))
    print(bits)
    print(int(bits, base=2))
    for k in range(maxbit,-1, -1):
        print(f'z{k:02} {func2(*system[f"z{k:02}"])}')
    # for z(i) try x(i) + y(i)
