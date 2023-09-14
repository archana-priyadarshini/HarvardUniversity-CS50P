#Problem statement: https://cs50.harvard.edu/python/2022/psets/5/test_twttr/
from twttr import shorten

def test_vowels():
    assert shorten("aeiou")==""

def test_consonants():
    assert shorten("myth")=="myth"

def test_mixed():
    assert shorten("apple")=="ppl"
    assert shorten("HELLO WORLD") == "HLL WRLD"
    assert shorten("h3ll0 w0rld!!") == "h3ll0 w0rld!!"
    assert shorten("@pple") == "@ppl"