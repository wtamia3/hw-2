import unittest
from Shapes import rectangle_area, triangle_area, circle_area

class TestShapes(unittest.TestCase):
    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(5, 4), 20)

    def test_triangle_area(self):
        self.assertEqual(triangle_area(3, 4), 6)

    def test_circle_area(self):
        self.assertAlmostEqual(circle_area(2), 12.566370614359172, places=2)

if __name__ == '__main__':
    unittest.main()