# Problem statement: https://cs50.harvard.edu/python/2022/psets/5/test_bank/
from bank import value

def test_value():
    assert value("Hello Sir")==0
    assert value("HELLO WORLD")==0
    assert value("hi")==20
    assert value("hey")==20
    assert value("Good morning")==100
    assert value("What's Up?")==100