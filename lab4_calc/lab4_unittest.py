import unittest
import calc

class CalcTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(5, 7), 12)

    def test_sub(self):
        self.assertEqual(calc.sub(5, 2), 3)

    def test_mul(self):
        self.assertEqual(calc.mul(4, 4), 16)

    def test_div(self):
        self.assertEqual(calc.div(16, 4), 4)

    def test_exp(self):
        self.assertEqual(calc.exp(7, 3), 343)

    def test_exp_NotEq(self):
        self.assertNotEqual(calc.exp(7, 3), 121)

    def test_sqr(self):
        self.assertEqual(calc.sqr(4), 16)

if __name__ == '__main__':
    unittest.main()
