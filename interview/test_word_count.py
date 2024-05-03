import unittest

from interview.word_count import get_token, longest_word


class TestWordCount(unittest.TestCase):
    def test_get_token_empty(self):
        self.assertEqual(get_token("", 0), ("", 0))

    def test_get_token(self):
        self.assertEqual(get_token("This is a test", 0), ("This", 4))
        self.assertEqual(get_token("This is a test", 5), ("is", 7))
        self.assertEqual(get_token("   leading spaces", 0), ("leading", 10))

    def test_longest_word_empty(self):
        self.assertIsNone(longest_word(""))

    def test_longest_word(self):
        self.assertEqual(longest_word("This is a test"), "This")
        self.assertEqual(longest_word("This is a longer test"), "longer")
        self.assertEqual(longest_word("This is the longest test"), "longest")
        self.assertEqual(longest_word("equal length words"), "length")


if __name__ == '__main__':
    unittest.main()