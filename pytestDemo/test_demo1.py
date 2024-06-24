#from cli comand to run pytest is-> py.test <ur file name>
# pytest -k <regular expression to run any particular function>
# -v -> verbose, -s : logs in output
# -m for mark , where @pytest.mark.<tag> is used to run marked tests like . py.test -m <tag>
#@pytest.mark.skip -> to skip tests
#@pytest.xfail -> test case will run but wont report as pass or fail
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_1():
    print("bye")

def test_2():
    assert "bye" == "bye"

@pytest.mark.xfail
def test_dontshow():
    print("wont mark pass or fail")

