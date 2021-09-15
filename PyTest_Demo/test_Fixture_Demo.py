import pytest


@pytest.fixture()
def setup():
    print("Execution begin from me")


def test_fixtureDemo(setup):
    print("Execute Steps in Fixture Demo")