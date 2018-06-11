from unittest import TestCase

from constraint_system import connector, converter, converter2


class TestConstraintSystem(TestCase):

    def test_celsius_25_should_be_fahrenheit_77(self):
        celsius = connector('Celsius')
        fahrenheit = connector('Fahrenheit')
        converter(celsius, fahrenheit)
        celsius['set_val']('user', 25)

    def test_input_10_should_be_output_20(self):
        input = connector('Input')
        output = connector('Output')
        converter2(input, output)
        output['set_val']('user', 10)
