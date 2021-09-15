#Coding Convention - start with test_ or end with _test.
#Pytest method should start with test
#Code should be wrapped in a method.
import pytest


@pytest.mark.skip
def test_first_Hello_Program():
    print("Hello")


def test_second_Credit_Greet():
    print("Good Morning")


