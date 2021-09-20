#Coding Convention - start with test_ or end with _test.
#Pytest method should start with test
#Code should be wrapped in a method.
#When you define fixture scope to class,
# it will run once before class is initiated and at the end.
#Data Driven & Parameterization can be done
# with return statements in tuple format.

import pytest


@pytest.mark.xfail()
def test_first_Hello_Program(setup):
    print("Hello")


def test_second_Credit_Greet():
    print("Good Morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])

