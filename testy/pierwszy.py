# def add(a, b):
#     return a + b
#
#
# def test_001():
#     assert add(1, 1) == 2
#
#
# def test_002():
#     assert add(0, 0) == 0
#
#
# def test_003():
#     assert add(1, 0) == 1
#
#
# def test_004():
#     assert add(100, 100) == 200
#
#
# def test_005():
#     assert add(-100, 100) == 0


def sqrt(x):
    assert x >= 0
    precision = 0.0001
    step = 1
    start = 0
    while abs(start * start - x) > precision:
        start += step
        if start * start > x:
            start -= step
            step /= 10
    return start


def test_check_if_throw_exception_when_x_below_0():
    try:
        sqrt(-1)
        assert False
    except Exception:
        assert True


def test_001():
    assert sqrt(4) == 2


def test_002():
    assert sqrt(0) == 0


def test_003():
    assert sqrt(81) == 9


def test_004():
    assert sqrt(1) == 1


def test_005():
    assert sqrt(25) == 5