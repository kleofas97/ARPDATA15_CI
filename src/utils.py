import unittest

class Calculator:

    def __init__(self, a, b):
        if isinstance(a, (int,float)):
            self._a = a
        else:
            raise Exception('wrong parameter a please use only int or float')
        if isinstance(b, (int, float)):
            self._b = b
        else:
            raise Exception('wrong parameter a please use only int or float')

    def dodawanie(self):
        return self._a + self._b
    def odejmowanie(self):
        return self._a - self._b
class TestCalculator(unittest.TestCase):
    def test_init(self):
        calc = Calculator(1, 2)
        self.assertEqual(calc._a, 1)
        self.assertEqual(calc._b, 2)

        with self.assertRaises(Exception):
            Calculator('a', 2)
        with self.assertRaises(Exception):
            Calculator(1, 'b')


    def test_dodawanie(self):
        calc = Calculator(1, 2)
        self.assertEqual(calc.dodawanie(), 3)

    def test_odejmowanie(self):
        calc = Calculator(1, 2)
        self.assertEqual(calc.odejmowanie(), -1)

if __name__ == '__main__':
    unittest.main()