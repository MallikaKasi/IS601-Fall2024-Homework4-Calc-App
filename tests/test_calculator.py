'''My Calculator Test'''
from calculator import Calculator

def test_addition():
    '''Test that Addition function works '''    
    assert Calculator.add(2,2) == 4

def test_subtraction():
    '''Test that Subtraction function works '''    
    assert Calculator.subtract(2,2) == 0

def test_multiply():
    '''Test that Multiplication function works '''    
    assert Calculator.multiply(2,2) == 4

def test_divide():
    '''Test that Division function works '''    
    assert Calculator.divide(2,2) == 1
