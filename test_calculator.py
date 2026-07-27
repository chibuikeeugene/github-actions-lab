import random
from calculator import add, subtract, multiply, divide

def test_add() -> None:
    """run test on add operation"""
    assert add(2,3) == 5

def test_subtract() -> None:
    """run test on substract operation"""
    assert subtract(2,3) == -1

def test_multiply() -> None:
    """run test on multiply operation"""
    assert multiply(4,5) == 20
    assert multiply(-4, 5) == -20

def test_divide() -> None:
    """run test on division operation"""
    assert divide(4,2) == 2