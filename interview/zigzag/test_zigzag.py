import unittest

from zigzag import ZigzagIterator


class TestZigzag(unittest.TestCase):
    def test_case1(self):
        v1 = [1, 2]
        v2 = [3, 4, 5, 6]
        z = ZigzagIterator(v1, v2)
        self.assertEqual(z.next(), 1)
        self.assertEqual(z.next(), 3)
        self.assertEqual(z.next(), 2)
        self.assertEqual(z.next(), 4)
        self.assertEqual(z.next(), 5)
        self.assertEqual(z.next(), 6)
        self.assertFalse(z.has_next())

    def test_case2(self):
        v1 = [1]
        v2 = []
        z = ZigzagIterator(v1, v2)
        self.assertEqual(z.next(), 1)
        self.assertFalse(z.has_next())

    def test_case3(self):
        v1 = []
        v2 = [1]
        z = ZigzagIterator(v1, v2)
        self.assertEqual(z.next(), 1)
        self.assertFalse(z.has_next())


if __name__ == "__main__":
    unittest.main()
