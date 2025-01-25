from calculator import Calculator
from behave import given, when, then

@given(u'I have a calculator')
def step_given_calculator(context):
    context.calc = Calculator()

@when(u'I add {num1:d} and {num2:d}')
def step_when_add(context, num1, num2):
    context.result = context.calc.add(num1, num2)

@when(u'I subtract {num1:d} from {num2:d}')
def step_when_subtract(context, num1, num2):
    context.result = context.calc.substract(num2, num1)

@when(u'I multiply {num1:d} by {num2:d}')
def step_when_multiply(context, num1, num2):
    context.result = context.calc.multiply(num1, num2)

@when(u'I divide {num1:d} by {num2:d}')
def step_when_divide(context, num1, num2):
    context.result = context.calc.divide(num1, num2)

@then(u'the result should be {expected:d}')
def step_then_result(context, expected):
    assert context.result == expected, f"Expected {expected}, but got {context.result}"
