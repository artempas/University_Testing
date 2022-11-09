import pytest
from logic.calcLogic import CalcLogic
from logic.presenter import Presenter, Operation

test_args = [(1, 2), (4, 2), (10, 16), (-31, 22)]


@pytest.fixture(params=test_args)
def args_fixture(request):
    test_logic = CalcLogic(0, 0)
    test_logic.a = request.param[0]
    test_logic.b = request.param[1]
    return test_logic


@pytest.fixture(params=test_args)
def presenter_fixture(request):
    test_presenter = Presenter()
    test_presenter.test_args = request.param
    yield test_presenter
    test_presenter.destroy()


test_args_with_errors = [
    ("da", ""),
    ("1-231", "1231"),
    ("123.123.", "123.123"),
    (".31", "0.31"),
    ("/=-1", "-1"),
]


@pytest.fixture(params=test_args_with_errors)
def invalid_presenter_input_fixture(request):
    test_presenter = Presenter()
    test_presenter.param = request.param
    yield test_presenter
    test_presenter.destroy()


@pytest.fixture(params=test_args_with_errors)
def invalid_input_fixture(request):
    test_logic = CalcLogic(0, 0)
    test_logic.a = request.param[0]
    test_logic.b = request.param[1]
    return test_logic


test_args_zero_division = [(1, 0), (100, 0), (32, 0), (0, 0)]


@pytest.fixture(params=test_args_zero_division)
def zero_division_presenter_input_fixture(request):
    test_presenter = Presenter()
    test_presenter.test_args = request.param
    yield test_presenter
    test_presenter.destroy()


@pytest.fixture()
def calc_fixture(request):
    test_presenter = Presenter()
    yield test_presenter
    test_presenter.destroy()
