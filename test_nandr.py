from nandr import xor, _and, _not, _or, nand, mux, mux2


def test_mux():
    assert mux(1, 1, 1) == 1
    assert mux(0, 1, 1) == 1
    assert mux(1, 0, 1) == 0
    assert mux(0, 0, 1) == 0
    assert mux(1, 0, 0) == 1
    assert mux(1, 1, 0) == 1
    assert mux(0, 0, 0) == 0
    assert mux(0, 1, 0) == 0


def test_mux2():
    assert mux2((1, 1), 1) == 1
    assert mux2((0, 1), 1) == 1
    assert mux2((1, 0), 1) == 0
    assert mux2((0, 0), 1) == 0
    assert mux2((1, 0), 0) == 1
    assert mux2((1, 1), 0) == 1
    assert mux2((0, 0), 0) == 0
    assert mux2((0, 1), 0) == 0


def test_xor():
    assert xor(1, 1) == 0
    assert xor(0, 1) == 1
    assert xor(1, 0) == 1
    assert xor(0, 0) == 0


def test_or():
    assert _or(1, 1) == 1
    assert _or(0, 1) == 1
    assert _or(1, 0) == 1
    assert _or(0, 0) == 0


def test_and():
    assert _and(1, 1) == 1
    assert _and(0, 1) == 0
    assert _and(1, 0) == 0
    assert _and(0, 0) == 0


def test_not():
    assert _not(1) == 0
    assert _not(0) == 1


def test_nand():
    assert nand(1, 1) == 0
    assert nand(0, 1) == 1
    assert nand(1, 0) == 1
    assert nand(0, 0) == 1
