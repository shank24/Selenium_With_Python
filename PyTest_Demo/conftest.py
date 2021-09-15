import pytest


@pytest.fixture()
def setup():
    print("Init Block")
    #Post Init and test_Fixture, Tear down ll run.
    #yield
    #print("Tear Down")
