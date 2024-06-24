import pytest

# setup is fixture here, first it will be checked in current file. if not found , it will search for conftest.py
#two ways 1. function level, 2nd is class level
#function level when fixture is in same file
@pytest.fixture
def setup_internal():
    print("This is local setup")
    yield
    print("this is local teardown")

def test_local_fix(setup_internal):
    print("this is local fixture")

#below is example when fixture is outside in conftest file
def test_fix_1(setup):
    print("this is func level fixture 1")
def test_fix_2(setup):
    print("this is func levl fix 2")

# when done at class level, fixture will be applicable to all the functions of class

@pytest.mark.usefixtures("setup_class")
class TestExample:
    def test_fixture_1(self):
        print("This is class level fixture 1")

    def test_fixture_2(self):
        print("this is class level fixture 2")
