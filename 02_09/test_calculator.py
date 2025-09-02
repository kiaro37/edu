import pytest
from practice_calculator import Calculator

calc = Calculator()

def test_add():
    assert calc.add(2,3) == 5
    assert calc.add(-1,1) == 0

def test_sub():
    assert calc.sub(10,3) == 7
    assert calc.sub(5,10) == -5

def test_mul():
    assert calc.mul(4,5) == 20
    assert calc.mul(2, -4) == -8

def test_div():
    assert calc.div(10,2) == 5
    assert calc.div(7,2) == 3.5

def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        calc.div(10,0)