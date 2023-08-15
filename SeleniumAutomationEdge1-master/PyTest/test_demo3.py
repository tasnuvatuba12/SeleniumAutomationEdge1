import pytest


@pytest.fixture
def common_function():
    name = input("Enter your name: ")
    return name


@pytest.mark.order(2)
def test_case5(common_function):
    print("Test case 5 Executed successfully.Your name is: ", common_function)


@pytest.mark.order(3)
def test_case6(common_function):
    print("Test case 6 Executed successfully", common_function)


@pytest.mark.order(1)
def test_case7(common_function):
    print("Test case 7 Executed successfully", common_function)
