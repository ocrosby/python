import random
import unittest

from algorithms.sorting import *


class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort_unsorted(self):
        self.assertEqual(insertion([34, 7, 23, 32, 5, 62]), [5, 7, 23, 32, 34, 62])

    def test_insertion_sort_empty(self):
        self.assertEqual(insertion([]), [])

    def test_insertion_sort_single(self):
        self.assertEqual(insertion([1]), [1])

    def test_insertion_sort_inorder(self):
        self.assertEqual(insertion([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_insertion_sort_reverse(self):
        self.assertEqual(insertion([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_insertion_sort_repeated(self):
        self.assertEqual(insertion([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_insertion_sort_large_random(self):
        # Generate a list of 10000 random integers between 1 and 5000
        lst = [random.randint(1, 5000) for _ in range(10000)]
        sorted_lst = insertion(lst)
        # Verify that the list is sorted
        self.assertEqual(sorted_lst, sorted(lst))


class TestQuicksort(unittest.TestCase):
    def test_quicksort_sorted(self):
        self.assertEqual(quick([34, 7, 23, 32, 5, 62]), [5, 7, 23, 32, 34, 62])

    def test_quicksort_empty(self):
        self.assertEqual(quick([]), [])

    def test_quicksort_single(self):
        self.assertEqual(quick([1]), [1])

    def test_quicksort_inorder(self):
        self.assertEqual(quick([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_quicksort_reverse(self):
        self.assertEqual(quick([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_quicksort_repeated(self):
        self.assertEqual(quick([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_selection_sort_large_random(self):
        # Generate a list of 10000 random integers between 1 and 5000
        lst = [random.randint(1, 5000) for _ in range(10000)]
        sorted_lst = quick(lst)
        # Verify that the list is sorted
        self.assertEqual(sorted_lst, sorted(lst))


class TestSelectionSort(unittest.TestCase):
    def test_selection_sort_sorted(self):
        self.assertEqual(selection([34, 7, 23, 32, 5, 62]), [5, 7, 23, 32, 34, 62])

    def test_selection_sort_empty(self):
        self.assertEqual(selection([]), [])

    def test_selection_sort_single(self):
        self.assertEqual(selection([1]), [1])

    def test_selection_sort_inorder(self):
        self.assertEqual(selection([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_selection_sort_reverse(self):
        self.assertEqual(selection([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_selection_sort_repeated(self):
        self.assertEqual(selection([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_selection_sort_large_random(self):
        # Generate a list of 10000 random integers between 1 and 5000
        lst = [random.randint(1, 5000) for _ in range(10000)]
        sorted_lst = selection(lst)
        # Verify that the list is sorted
        self.assertEqual(sorted_lst, sorted(lst))


if __name__ == "__main__":
    unittest.main()
