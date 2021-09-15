import pytest


@pytest.fixture()
def setup():
    print("Init Block")
    #Post Init and test_Fixture, Tear down ll run.
    #yield
    #print("Tear Down")


def test_fixtureDemo(setup):
    print("Execute Steps in Fixture Demo")