import pytest


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print("Execute Steps in Fixture Demo")

    def test_fixtureDemo1(self):
        print("Execute Steps in Fixture Demo 1 ")

    def test_fixtureDemo2(self):
        print("Execute Steps in Fixture Demo 2 ")

    def test_fixtureDemo3(self):
        print("Execute Steps in Fixture Demo 3 ")
