from calculatrice import addition, soustraction, multiplication, division

def test_addition():
    assert addition(2, 3) == 5

def test_soustraction():
    assert soustraction(5, 3) == 2

def test_multiplication():
    assert multiplication(2, 4) == 8

def test_division():
    assert division(10, 2) == 5
