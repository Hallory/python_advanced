from simple_math import SimpleMath
import pytest

@pytest.fixture
def math():
    return SimpleMath()
def test_square_positive():
    assert math.square(2) == 4


def test_square_negative():
    assert math.square(-3) == 9


def test_square_zero():
    assert math.square(0) == 0


def test_cube_positive():
    assert math.cube(3) == 27


def test_cube_negative():
    assert math.cube(-3) == -27


def test_cube_zero():
    assert math.cube(0) == 0