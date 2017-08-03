def nand(a, b):
    if a == b == 1:
        return 0
    else:
        return 1


def _not(a):
    return nand(a, a)


def _and(a, b):
    return _not(nand(a, b))


def _or(a, b):
    return nand(_not(a), _not(b))


def xor(a, b):
    return _or(_and(_not(a), b), _and(a, _not(b)))


def mux(a, b, sel):
    if sel == 0:
        return a
    else:
        return b


def mux2(inputs, sel):
    return inputs[sel]
