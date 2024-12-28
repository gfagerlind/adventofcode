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

inp = """\
x00: 0
x01: 1
x02: 0
x03: 1
x04: 0
x05: 1
y00: 0
y01: 0
y02: 1
y03: 1
y04: 0
y05: 1

x00 AND y00 -> z05
x01 AND y01 -> z02
x02 AND y02 -> z01
x03 AND y03 -> z03
x04 AND y04 -> z04
x05 AND y05 -> z00
"""
maxbit=5

with open(sys.argv[1]) as f:
    inp = f.read(); maxbit=45
    summa = 0
    system = {}
    # @functools.cache
    def func(i1, op=None, i2=None):
        if op is None:
            return i1[0]
        match op:
            case 'XOR':
                # print(f"{system[i1]} ^ {system[i2]}")
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
    # bits = "".join(str(func(*system[f"z{k:02}"])) for k in range(maxbit,-1, -1))
    # print(bits)
    # print(int(bits, base=2))
    for k in range(maxbit,22, -1):
        print(f'z{k:02} {func2(*system[f"z{k:02}"])}')
    # for z(i) try x(i) + y(i)
    system["z11"], system["vkq"] = system["vkq"], system["z11"]
    # mmk z24
    system["z24"], system["mmk"] = system["mmk"], system["z24"]
    # x28 XOR y28 -> qdq
    # y28 AND x28 -> pvb
    system["qdq"], system["pvb"] = system["pvb"], system["qdq"]
    # vsb AND dkp -> z38
    # y38 XOR x38 -> vsb
    # dkp XOR vsb -> hqh
    system["z38"], system["hqh"] = system["hqh"], system["z38"]
    # set to zero
    for prefix in ('x', 'y'):
        for k in range(maxbit+1):
            system[f"{prefix}{k:02}"] = [(0,), None, f"{prefix}{k:02}"]
    for k in range(maxbit):
        kplus1 = k+1
        system[f"y{k:02}"] = [(1,), None, f"y{k:02}"]
        if func(*system[f"z{k:02}"]) != 1:
            print(f'y=1,x=0 for {k} failed{func(*system[f"x{k:02}"])} {func(*system[f"y{k:02}"])} {func(*system[f"z{k:02}"])}')
            bits = "".join(str(func(*system[f"z{k:02}"])) for k in range(maxbit+1))
            print(bits)
        system[f"x{k:02}"] = [(1,), None, f"x{k:02}"]
        # print(f'i tried to set {system[f"x{k:02}"]}')
        if func(*system[f"z{k:02}"]) != 0:
            print(f'y=1,x=1 for {k} failed{func(*system[f"x{k:02}"])} {func(*system[f"y{k:02}"])} {func(*system[f"z{k:02}"])}')
            bits = "".join(str(func(*system[f"z{k:02}"])) for k in range(maxbit+1))
            print(bits)
        if kplus1 <= maxbit and func(*system[f"z{kplus1:02}"]) != 1:
            print(f'y=1,x=1 for k+1 {k} failed{func(*system[f"x{k:02}"])} {func(*system[f"y{k:02}"])} {func(*system[f"z{kplus1:02}"])}')
            bits = "".join(str(func(*system[f"z{k:02}"])) for k in range(maxbit+1))
            print(bits)
        system[f"y{k:02}"] = [(0,), None, f"y{k:02}"]
        if func(*system[f"z{k:02}"]) != 1:
            print(f'y=0,x=1 for {k} failed{func(*system[f"x{k:02}"])} {func(*system[f"y{k:02}"])} {func(*system[f"z{k:02}"])}')
            bits = "".join(str(func(*system[f"z{k:02}"])) for k in range(maxbit+1))
            print(bits)
        system[f"x{k:02}"] = [(0,), None, f"x{k:02}"]
