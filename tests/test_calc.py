from pytest_bdd import scenario, given, when, then, parsers


@scenario("test_calc.feature", "Add one number to another")
def test_calc(calc_fixture):
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


@when("I pressed calculate button")
def step_impl(calc_fixture):
    calc_fixture.calculate()


@when("I pressed plus button")
def step_impl(calc_fixture):
    calc_fixture.on_plus()


@then(parsers.parse("I get {result:d}"))
def step_impl(calc_fixture, result):
    assert result == float(calc_fixture.memory_field["text"])
