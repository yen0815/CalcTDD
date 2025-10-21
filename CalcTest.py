import unittest
from Calc import Calculator  # The class we are going to implement

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(result, 5)  # Expect 2 + 3 = 5
    def test_subtract(self):
        calc = Calculator()
        result = calc.subtract(5, 2)
        self.assertEqual(result, 3)
    def test_multiply(self):
        calc = Calculator()
        self.assertEqual(calc.multiply(3, 4), 12)
    def test_divide(self):
        calc = Calculator()
        self.assertEqual(calc.divide(10, 2), 5)     

if __name__ == "__main__":
    unittest.main()

