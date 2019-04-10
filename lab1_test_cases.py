import unittest
from lab1 import *

# A few test cases.  Add more!!!


class TestLab1(unittest.TestCase):

    def test_max_list_iter_value_error(self):
        """this tests the max_list_iter function for a list that is None"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_iter_empty_list(self):
        """this tests the max_list_iter function for a empty list"""
        list1 = []
        self.assertEqual(max_list_iter(list1), None)

    def test_max_list_iter_other_tests(self):
        """this tests the max_list_iter function for other necessary tests such as
        if there are multiple maxes, negative maxes, even-odd length list """
        list1 = [2, 5, 10, -12, 0]
        list2 = [4, 200, 200, 9, 10]
        list3 = [1, 1, 1, 1, 1]
        list4 = [-19, -1022, -123, -50]
        list5 = [1, 2, 2, -2, -12]
        list6 = [4, 5, 100, 1, 100, 1]
        list7 = [9, 102, -100, 20, -1293, 1203, 1932, 9, -10, 1230]

        self.assertEqual(max_list_iter(list1), 10)
        self.assertEqual(max_list_iter(list2), 200)
        self.assertEqual(max_list_iter(list3), 1)
        self.assertEqual(max_list_iter(list4), -19)
        self.assertEqual(max_list_iter(list4), -19)
        self.assertEqual(max_list_iter(list5), 2)
        self.assertEqual(max_list_iter(list6), 100)
        self.assertEqual(max_list_iter(list7), 1932)

    def test_reverse_rec_value_error(self):
        """this tests the reverse_rec function for a list that is None"""
        list1 = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(list1)

    def test_reverse_rec_empty_list(self):
        """this tests the reverse_rec function for a list that is empty"""
        self.assertEqual(reverse_rec([]), [])

    def test_reverse_rec_other_tests(self):
        """this tests the reverse_rec functions for other necessary tests
        with varying list lengths"""
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_rec([4]), [4])
        self.assertEqual(reverse_rec([0, 0]), [0, 0])
        self.assertEqual(reverse_rec([10, 2, 9, 8, -4]), [-4, 8, 9, 2, 10])
        self.assertEqual(reverse_rec([1, -1, 1]), [1, -1, 1])
        self.assertEqual(reverse_rec([1, 9, -100, 10, 2, 9, 20]), [20, 9, 2, 10, -100, 9, 1])

    def test_bin_search_value_error(self):
        """this tests the bin_search function if the list is None"""
        list1 = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(9, 0, 4, list1)

    def test_bin_search_empty_list(self):
        """this tests the bin_search function if the list is empty"""
        list_val = []
        self.assertEqual(bin_search(10, 0, 1, list_val), None)

    def test_bin_search_no_value(self):
        """this tests the bin_search function if the target is not in the list"""
        list_val = [2, 10, 11, 30]
        list_val2 = [-80, -20, 0, 20, 50]
        list_val3 = [1, 3]
        list_val4 = [1]

        self.assertEqual(bin_search(-2, 0, len(list_val) - 1, list_val), None)
        self.assertEqual(bin_search(2, 1, 2, list_val), None)
        self.assertEqual(bin_search(100, 0, len(list_val) - 1, list_val), None)
        self.assertEqual(bin_search(99, 0, len(list_val2) - 1, list_val2), None)
        self.assertEqual(bin_search(0, 0, 1, list_val3), None)
        self.assertEqual(bin_search(-2, 0, 1, list_val3), None)
        self.assertEqual(bin_search(2000, 0, 1, list_val3), None)
        self.assertEqual(bin_search(100, 0, 0, list_val4), None)
        self.assertEqual(bin_search(-100, 0, 0, list_val4), None)

    def test_bin_search_target_present(self):
        """this tests the bin_search function if the target is present at various
        positions in the list"""
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        list_val2 = [0, 4, 6, 10, 11, 19]
        list_val3 = [0, 1, 5, 10, 30, 89]
        list_val4 = [0, 1, 4, 7, 10]
        list_val5 = [5, 8, 10, 23, 90, 102, 202]
        list_val6 = [1, 5]
        list_val7 = [2]

        self.assertEqual(bin_search(4, 0, len(list_val) - 1, list_val), 4)
        self.assertEqual(bin_search(19, 0, len(list_val2) - 1, list_val2), 5)
        self.assertEqual(bin_search(0, 0, len(list_val2) - 1, list_val2), 0)
        self.assertEqual(bin_search(10, 0, len(list_val3) - 1, list_val3), 3)
        self.assertEqual(bin_search(7, 1, len(list_val4) - 1, list_val4), 3)
        self.assertEqual(bin_search(23, 2, 5, list_val5), 3)
        self.assertEqual(bin_search(10, 2, 5, list_val5), 2)
        self.assertEqual(bin_search(102, 2, 5, list_val5), 5)
        self.assertEqual(bin_search(1, 0, 1, list_val6), 0)
        self.assertEqual(bin_search(2, 0, 0, list_val7), 0)


if __name__ == "__main__":
    unittest.main()
