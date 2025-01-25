# TDD & BDD with Python, unitest, and Pytest
import pytest
from calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5


def test_substract():
    calc = Calculator()
    assert calc.substract(3,2) == 1


def test_multiply():
    calc = Calculator()
    assert calc.multiply(2,3) == 6


def test_divide():
    calc = Calculator()
    assert calc.divide(6,3) == 2



