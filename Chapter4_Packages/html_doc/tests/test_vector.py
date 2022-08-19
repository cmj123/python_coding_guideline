'''Test code
'''

import unittest

from fastvector import Vector2D

class VectorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.v1 = Vector2D(0,0)
        self.v2 = Vector2D(-1,1)
        self.v3 = Vector2D(2.5,-2.5)

    def test_init(self) -> None:
        result = Vector2D(-1, 1)
        self.assertEqual(result, self.v2)
        self.assertRaises(TypeError, Vector2D, 0, 'a')
        self.assertRaises(TypeError, Vector2D, 'B', 1)

    def test_comparison(self) -> None: 
        # Test equality
        self.assertNotEqual(self.v1, self.v2)
        expected_result = Vector2D(-1, 1)
        self.assertEqual(self.v2, expected_result)
        # Test less
        result = self.v1 + self.v2
        self.assertLess(result, self.v3)
        # Test greater
        self.assertGreater(self.v3, result)
        self.assertNotEqual(self.v3, self.v1)

    def test_call(self) -> None:
        result = self.v1()
        expected_result = repr(self.v1)
        self.assertEqual(result, expected_result)

    # def test_add(self) -> None:
    #     '''Test the addition operator
    #     '''
    #     result = self.v1 + self.v2
    #     expected_result = Vector2D(-1,1)
    #     self.assertEqual(result, expected_result)

    # def test_sub(self):
    #     '''Tests the subtraction operator
    #     '''
    #     result = self.v2 - self.v3
    #     expected_result = Vector2D(-3.5, 3.5)
    #     self.assertEqual(result, expected_result)

    # def test_mul(self):
    #     '''Tests the multiplication operator
    #     '''
    #     result1 = self.v1 * 5
    #     expected_result1 = Vector2D(0.0,0.0)
    #     self.assertEqual(result1, expected_result1)
    #     result2 = self.v1 * self.v2
    #     expected_result2 = 0.0
    #     self.assertEqual(result2, expected_result2)

    # def test_div(self):
    #     '''Tests the division operator
    #     '''
    #     result = self.v3 / 5 
    #     expected_result = Vector2D(0.5, -0.5)
    #     self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()