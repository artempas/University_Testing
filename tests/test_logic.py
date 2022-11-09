from logic import calcLogic
from logic.presenter import Presenter


def test_sum(args_fixture):
    assert args_fixture.a + args_fixture.b == args_fixture.sum()


def test_subtract(args_fixture):
    assert args_fixture.a - args_fixture.b == args_fixture.subtract()


def test_multiply(args_fixture):
    assert args_fixture.a * args_fixture.b == args_fixture.multiply()


def test_sum_invalid_input(invalid_input_fixture):
    try:
        invalid_input_fixture.sum()
        assert False
    except TypeError:
        assert True


def test_subtract_invalid_input(invalid_input_fixture):
    try:
        invalid_input_fixture.subtract()
        assert False
    except TypeError:
        assert True


def test_multiply_invalid_input(invalid_input_fixture):
    try:
        invalid_input_fixture.multiply()
        assert False
    except TypeError:
        assert True


def test_divide_invalid_input(invalid_input_fixture):
    try:
        invalid_input_fixture.divide()
        assert False
    except TypeError:
        assert True


def test_zero_div():
    test_logic = calcLogic.CalcLogic(5, 0)
    try:
        test_logic.divide()
        assert False
    except ZeroDivisionError:
        assert True
