import unittest
from re import sub

from calculator import add,substract, multiply,division

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3),5)
        self.assertEqual(add(-1,1),0)
        self.assertEqual(add(0,0),0)

    def test_sub(self):
        self.assertEqual(substract(2,3),-1)
        self.assertEqual(substract(-1,1),-2)
        self.assertEqual(substract(0,0),0)

    def test_mul(self):
        self.assertEqual(multiply(2,3),6)
        self.assertEqual(multiply(-1,1),-1)
        self.assertEqual(multiply(0,0),0)

    def test_div(self):
        self.assertEqual(division(6,3),2)
        self.assertEqual(division(-1,1),-1)
        self.assertEqual(division(-1,-1),1)


if __name__== '__main__':
    unittest.main()

