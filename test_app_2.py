from app_2 import add

def test_add():
    assert add(37, 21) == 16
    assert add(-1, 1) == -2
