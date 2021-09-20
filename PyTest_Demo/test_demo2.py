# Coding Convention - start with test_ or end with _test.
# Pytest method should start with test
# Code should be wrapped in a method.
# -k for Regex (Method Name exexution)
# -s logs in output
# -v for verbose (More Info Metadata)
# -m tagname - py.test -m smoke -v -s
# Running specific file with py.test filenames
# Skip Test with - @pytest.mark.skip
# Fixtures are used for setup and tear down for test cases
# Conftest to generalize and code re-usability
# ,it is available to all TestCase.

import pytest


@pytest.mark.skip
def test_first_Assert_Hello_Program():
    msg = "Hello World"
    assert msg == "Hello World", "Strings do not match"


@pytest.mark.skip
def test_second_Credit():
    a = 4
    b = 6
    assert a + 2 == 6, "Addition not matching"

