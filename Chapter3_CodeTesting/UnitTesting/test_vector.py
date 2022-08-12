'''Test code
'''
import unittest

from .vector import Vector2D

class VectorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.v1 = Vector2D(0,0)
        self.v2 = Vector2D(-1,1)
        self.v3 = Vector2D(2.5,-2.5)

    def test_equality(self) -> None:
        '''Tests the equality operator
        '''
        self.assertNotEqual(self.v1, self.v2)
        expected_result = Vector2D(-1,1)
        self.assertEqual(self.v2, expected_result)

    def test_add(self) -> None:
        '''Test the addition operator
        '''
        result = self.v1 + self.v2
        expected_result = Vector2D(-1,1)
        self.assertEqual(result, expected_result)




if __name__ == '__main__':
    unittest.main()