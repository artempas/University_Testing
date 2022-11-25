from pytest_bdd import scenario, given, when, then, parsers


@scenario("test_calc.feature", "Sum")
def test_sum(calc_fixture):
    pass


@scenario("test_calc.feature", "Zero division")
def test_zero_div(calc_fixture):
    pass


@scenario("test_calc.feature", "Enter value and press equal")
def test_val_eq(calc_fixture):
    pass


@scenario("test_calc.feature", "Zero division with other operation")
def test_zero_div_op(calc_fixture):
    pass


@scenario("test_calc.feature", "Consecutive operations")
def test_consec(calc_fixture):
    pass


@scenario("test_calc.feature", "Consecutive zero division")
def test_consec_zero_div(calc_fixture):
    pass


@scenario("test_calc.feature", "Wrong Input")
def test_text(calc_fixture):
    pass


@scenario("test_calc.feature", "Mixed input")
def test_mixed(calc_fixture):
    pass


@scenario("test_calc.feature", "Multiply")
def test_multiply(calc_fixture):
    pass


@scenario("test_calc.feature", "Subtract")
def test_subtraction(calc_fixture):
    pass


@given("I opened calc app", target_fixture="calc_fixture")
def step_impl(calc_fixture):
    return calc_fixture


@when(parsers.parse("I entered {first_value:d}"))
def step_impl(calc_fixture, first_value):
    for char in str(first_value)[::-1]:
        calc_fixture.input_field.insert(0, char)


@when(parsers.parse("I entered {second_value:d}"))
def step_impl(calc_fixture, second_value):
    for char in str(second_value)[::-1]:
        calc_fixture.input_field.insert(0, char)


@when(parsers.parse("I entered {first_value_mixed}"))
def step_impl(calc_fixture, first_value_mixed):
    for char in first_value_mixed[::-1]:
        calc_fixture.input_field.insert(0, char)


@when(parsers.parse("I entered {second_value_mixed}"))
def step_impl(calc_fixture, second_value_mixed):
    for char in second_value_mixed[::-1]:
        calc_fixture.input_field.insert(0, char)


@when("I pressed calculate button")
def step_impl(calc_fixture):
    calc_fixture.calculate()


@when("I pressed plus button")
def step_impl(calc_fixture):
    calc_fixture.on_plus()


@then(parsers.parse("I get {result:d}"))
def step_impl(calc_fixture, result):
    assert result == float(calc_fixture.memory_field["text"])


@when("I pressed multiply button")
def step_impl(calc_fixture):
    calc_fixture.on_multiply()


@when("I pressed minus button")
def step_impl(calc_fixture):
    calc_fixture.on_subtract()


@when("I pressed divide button")
def step_impl(calc_fixture):
    calc_fixture.on_divide()


@when("I entered text")
def step_impl(calc_fixture):
    for char in "some text"[::-1]:
        calc_fixture.input_field.insert(0, char)


@then("I get nothing")
def step_impl(calc_fixture):
    assert "" == calc_fixture.memory_field["text"]


@then("I get error")
def step_impl(calc_fixture):
    assert "ОШИБКА" == calc_fixture.memory_field["text"]
