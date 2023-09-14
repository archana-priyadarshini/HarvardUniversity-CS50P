# Problem statement: https://cs50.harvard.edu/python/2022/psets/5/test_plates/
from plates import is_valid

def test_starts_2letters():
    assert is_valid("CS50") == True
    assert is_valid("50CS") == False
    assert is_valid("C8987") == False
def test_length():
    assert is_valid("C")== False
    assert is_valid("CS")== True
    assert is_valid("CS50HARVARD")== False
    assert is_valid("CS5045")== True
def test_numbers():
    assert is_valid("CS50P")==False
    assert is_valid("CS05")==False
    assert is_valid("xcp87")==True
def test_punc():
    assert is_valid("CS50!!")== False
