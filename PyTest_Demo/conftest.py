import pytest

#Scope =Class defines the setup execution only before class

@pytest.fixture(scope="class")
def setup():
    print("Init Block")
    #Post Init and test_Fixture, Tear down ll run.
    #yield
    #print("Tear Down")
