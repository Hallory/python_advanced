from simple_math import SimpleMath


def test_square_positive():
    math = SimpleMath()
    assert math.square(2) == 4


def test_square_negative():
    math = SimpleMath()
    assert math.square(-3) == 9


def test_square_zero():
    math = SimpleMath()
    assert math.square(0) == 0


def test_cube_positive():
    math = SimpleMath()
    assert math.cube(3) == 27


def test_cube_negative():
    math = SimpleMath()
    assert math.cube(-3) == -27


def test_cube_zero():
    math = SimpleMath()
    assert math.cube(0) == 0