from twttr import shorten

def test_shorten():
    assert shorten("hello")=="hll"
    assert shorten("world56")=="wrld56"
    assert shorten("HEllo, World")=="Hll, Wrld"






