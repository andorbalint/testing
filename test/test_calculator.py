import pytest
from calculator.calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_addition(calculator):
    result = calculator.add(3,5)
    assert result == 8


def test_multiplication(calculator):
    result = calculator.multiply(4, 5)
    assert result == 20

def test_subtraction(calculator):
    result = calculator.subtract(8, 3)
    assert result == 5

def test_division(calculator):
    result = calculator.divide(10, 2)
    assert result == 5.0

def test_integer_division(calculator):
    result = calculator.integer_divide(10, 3)
    assert result == 3

def test_division_by_zero(calculator):
    with pytest.raises(ZeroDivisionError):
        calculator.divide(5, 0)











