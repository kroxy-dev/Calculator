from calculator import add,subtract,divide,multiply
import pytest
#tests the add function
def test_add():
    assert add(2,5)==7
    assert add (2,0)==2

#tests the subtract function
def test_subtract():
    assert subtract(5,2)==3
    assert subtract (2,0)==2

#tests the divide function
def test_divide():
    assert divide(10,5)==2
    with pytest.raises(ZeroDivisionError):
        divide(3,0)

#tests the multiply function
def test_multiply():
    assert multiply(3,5)==15
    assert multiply (2,0)==0
