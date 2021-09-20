import pytest


# Scope =Class defines the setup execution only before class

@pytest.fixture(scope="class")
def setup():
    print("Init Block")
    # Post Init and test_Fixture, Tear down ll run.
    # yield
    # print("Tear Down")


@pytest.fixture()
def dataLoad():
    print("user-profile data is being created")
    return ["Harvey", "Specter", "Suits"]


@pytest.fixture(params=["Chrome", "Firefox", "Edge"])
def crossBrowser(request):
    return request.param
