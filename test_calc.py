from calculatrice import addition, soustraction, multiplication, division

def test_addition():
    assert addition(2, 3) == 8
    assert addition(-5, -10) == -15
    assert addition(-5.05, -10.09) == -15.14
    assert addition(1022656598984549898979, 10.0945959498484849) == 1022656598984549898989.0945959498484849

def test_soustraction():
    assert soustraction(5, 3) == 2

def test_multiplication():
    assert multiplication(2, 4) == 8

def test_division():
    assert division(10, 2) == 5
