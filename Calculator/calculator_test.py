import unittest
from calculator import addition, subtraction, multiplication, division

class TestCalculatorFunctions(unittest.TestCase):
    
    def test_addition(self):
        self.assertEqual(addition(2, 3), 5)
        self.assertEqual(addition(-2, 3), 1)
        self.assertEqual(addition(0, 0), 0)

    def test_subtraction(self):
        self.assertEqual(subtraction(5, 3), 2)
        self.assertEqual(subtraction(0, 0), 0)
        self.assertEqual(subtraction(-2, -3), 1)

    def test_multiplication(self):
        self.assertEqual(multiplication(2, 3), 6)
        self.assertEqual(multiplication(0, 5), 0)
        self.assertEqual(multiplication(-2, 3), -6)

    def test_division(self):
        self.assertEqual(division(6, 3), 2)
        self.assertEqual(division(0, 5), 0)
        self.assertEqual(division(-6, 2), -3)
        
        with self.assertRaises(ZeroDivisionError):
            division(5, 0)

if __name__ == '__main__':
    unittest.main()
