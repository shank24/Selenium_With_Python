#Coding Convention - start with test_ or end with _test.
#Pytest method should start with test
#Code should be wrapped in a method.

def test_first_program():
    msg = "Hello World"
    assert msg == "Hello World", "Strings do not match"


def test_second_program():
    a = 4
    b = 6
    assert a+2 == 6, "Addition not matching"





