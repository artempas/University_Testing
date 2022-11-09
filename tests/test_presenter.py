from logic.presenter import Presenter, Operation
import logic.main


def test_presenter_on_plus(presenter_fixture):
    arg1, arg2 = presenter_fixture.test_args
    for char in str(arg1)[::-1]:
        presenter_fixture.input_field.insert(0, char)
    presenter_fixture.on_plus()
    for char in str(arg2)[::-1]:
        presenter_fixture.input_field.insert(0, char)
    presenter_fixture.calculate()
    result = float(presenter_fixture.memory_field["text"])
    expected_result = float(str(arg1 + arg2)[:16])
    assert result == expected_result


def test_presenter_on_divide(presenter_fixture: Presenter):
    arg1, arg2 = presenter_fixture.test_args
    for char in str(arg1)[::-1]:
        presenter_fixture.input_field.insert(0, char)
    presenter_fixture.on_divide()
    for char in str(arg2)[::-1]:
        presenter_fixture.input_field.insert(0, char)
    presenter_fixture.calculate()
    result = float(presenter_fixture.memory_field["text"])
    expected_result = float(str(arg1 / arg2)[:16])
    assert result == expected_result


def test_presenter_multiply(presenter_fixture):
    arg1, arg2 = presenter_fixture.test_args
    for char in str(arg1)[::-1]:
        presenter_fixture.input_field.insert(0, char)
    presenter_fixture.on_multiply()
    for char in str(arg2)[::-1]:
        presenter_fixture.input_field.insert(0, char)
    presenter_fixture.calculate()
    result = float(presenter_fixture.memory_field["text"])
    expected_result = float(str(arg1 * arg2)[:16])
    assert result == expected_result


def test_presenter_on_subtract(presenter_fixture):
    arg1, arg2 = presenter_fixture.test_args
    for char in str(arg1)[::-1]:
        presenter_fixture.input_field.insert(0, char)
    presenter_fixture.on_subtract()
    for char in str(arg2)[::-1]:
        presenter_fixture.input_field.insert(0, char)
    presenter_fixture.calculate()
    result = float(presenter_fixture.memory_field["text"])
    expected_result = float(str(arg1 - arg2)[:16])
    assert result == expected_result


def test_invalid_input(invalid_presenter_input_fixture):
    inp, out = invalid_presenter_input_fixture.param
    for char in enumerate(str(inp)):
        invalid_presenter_input_fixture.input_field.insert(*char)
    invalid_presenter_input_fixture.on_plus()
    result = invalid_presenter_input_fixture.memory_field["text"]
    assert result == out


def test_presenter():
    logic.main.main()


def test_presenter_zero_division(zero_division_presenter_input_fixture: Presenter):
    arg1, arg2 = zero_division_presenter_input_fixture.test_args
    for char in str(arg1)[::-1]:
        zero_division_presenter_input_fixture.input_field.insert(0, char)
    zero_division_presenter_input_fixture.on_divide()
    for char in str(arg2)[::-1]:
        zero_division_presenter_input_fixture.input_field.insert(0, char)
    zero_division_presenter_input_fixture.calculate()
    result = zero_division_presenter_input_fixture.memory_field["text"]
    assert result == "ОШИБКА"
