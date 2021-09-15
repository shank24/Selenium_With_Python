# Coding Convention - start with test_ or end with _test.
# Pytest method should start with test
# Code should be wrapped in a method.
# -k for Regex (Method Name exexution)
# -s logs in output
# -v for verbose (More Info Metadata)
# -m tagname - py.test -m smoke -v -s
# Running specific file with py.test filenames
import pytest


@pytest.mark.smoke
def test_first_Assert_Hello_Program():
    msg = "Hello World"
    assert msg == "Hello World", "Strings do not match"


def test_second_Credit():
    a = 4
    b = 6
    assert a + 2 == 6, "Addition not matching"
