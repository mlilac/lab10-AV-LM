#https://github.com/mlilac/lab10-AV-LM.git
#Partner 1: Aniruth Venkedesh
#Partner 2: Lucas Moraes
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
    # + +
        self.assertEqual(add(5,2),7)
        # - -
        self.assertEqual(add(-5, -10), -15)
        # + -
        self.assertEqual(add(-5, 10), 5)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(10,1),9)
        self.assertEqual(subtract(-2, -3),1)
        self.assertEqual(subtract(1,10),-9)
# ##########################

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(mul(2, 3), 6, "2 * 3 should be 6")
        self.assertEqual(mul(-1, 5), -5, "-1 * 5 should be -5")
        self.assertEqual(mul(0, 10), 0, "0 * 10 should be 0")

    def test_divide(self): # 3 assertions
        self.assertEqual(div(3,6), 2, "6 / 3 should be 2")
        self.assertEqual(div(2, 5), 2.5, "5 / 2 should be 2.5")
        self.assertEqual(div(2, -10), -5, "-10 / 2 should be -5")

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code
        with self.assertRaises(ZeroDivisionError):
            div(0,17)

    def test_logarithm(self): # 3 assertions
    #     fill in code
        self.assertEqual(logarithm(10,100),2.0)
        self.assertEqual(logarithm(2,2), 1.0)
        self.assertEqual(logarithm(2,8,),3.0)

    def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
        with self.assertRaises(ZeroDivisionError):
            logarithm(1,2)
            logarithm(-2, 100)
            logarithm(0, 24)

    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5, "Hypotenuse of 3, 4 should be 5")
        self.assertEqual(hypotenuse(5, 12), 13, "Hypotenuse of 5, 12 should be 13")
        self.assertAlmostEqual(hypotenuse(-6, 8), 10, "Hypotenuse of -6, 8 should be 10")

    def test_sqrt(self): # 3 assertions
        self.assertEqual(square_root(9), 3, "Square root of 9 should be 3")
        self.assertEqual(square_root(0), 0, "Square root of 0 should be 0")
        with self.assertRaises(ValueError):
            square_root(-9)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()