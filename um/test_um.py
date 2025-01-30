from um import count

def test_count_1():
    assert count("um") == 1
    assert count("um hello um") == 2

def test_count_2():
    assert count("fhefum fheumfef um") == 1
    assert count("helloum umm um") == 1

def test_count_3():
    assert count("UM um")==2
    assert count("Um FHGUM FHFum") ==1
