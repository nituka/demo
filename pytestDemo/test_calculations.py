import pytest
@pytest.fixture
def setup():
    print("setup")
    yield
    print("bye")
@pytest.mark.regression
def test_sum():
    assert sum([10,17],3) == 30, "sum is wrong"
@pytest.mark.skip
def test_diff():
    assert 20-10 ==20 , "diff is wrong"
def test_prod():
    assert 20*10==200, "prod is wrong"

def test_fix(setup):
    print("test fix")

