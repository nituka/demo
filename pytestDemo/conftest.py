import pytest


# pytest.fixture() function is used to run setup and teardown,  anything after yield is run after tests are over
# fixtures are mentioned in conftest.py file( name has to be conftest only)
@pytest.fixture()
def setup():
    print("I am in external setup")
    yield
    print("I am in external teardown")


# fixture to pass input to all functions
# this setup and teardown is done only once at the start and end
@pytest.fixture(scope="class")
def setup_class():
    print("I am in setup from class")
    yield
    print("I am teardown from class")


@pytest.fixture(scope="class")
def input_data():
    print("\nI am fixture")
    return ["Bob", "https://www.google.com/"]

#fixture will be called for each param
@pytest.fixture(params=["Chrome", "FireFox", "IE"])
def input_data_param(request):
    #keyword request is mandatory to use
    return request.param
