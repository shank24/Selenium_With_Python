#Coding Convention - start with test_ or end with _test.
#Pytest method should start with test
#Code should be wrapped in a method.
import pytest


@pytest.mark.xfail()
def test_first_Hello_Program(setup):
    print("Hello")


def test_second_Credit_Greet():
    print("Good Morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser)

