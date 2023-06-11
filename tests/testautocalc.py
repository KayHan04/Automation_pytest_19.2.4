import pytest

from app.calculator import Calculator


class Testcalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_succsess(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_adding_unsuccsess(self):
        assert self.calc.adding(self, 1, 1) == 3

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self,1, 0)

    def test_multiply(self):
        assert  self.calc.multiply(self, 2, 2) == 4

    def test_substration(self):
        assert self.calc.subtraction(self, 40, 30) == 11

    def teardown(self):
        print('Выполнение метода Teardown')
