from app import add, divide

def test_add():
    assert add(2,3) == 6

def test_divide():
    assert divide(10,2) == 5

def test_divide_by_zero():
    divide(5,0)

def test_add_string():
    assert add("a ", "b") == "ab"

def test_divide_by_zero():
    divide(5,0)