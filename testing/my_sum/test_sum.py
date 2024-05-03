import unittest


class TestSum(unittest.TestCase):
    def test_sum(self):
        """
        Test that it can add a list of integers
        """
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        """
        Test that it can add a tuple of integers
        """
        self.assertEqual(sum((1, 2, 2)), 5, "Should be 5")


if __name__ == '__main__':
    unittest.main()
