#! python
import unittest

def binary_search(x, array):
    lo = 0
    hi = len(array) - 1
    while lo <= hi:
        mid = int((lo + hi) / 2)
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return False

class TestSearchAlgorythms(unittest.TestCase):
    def test_binary_search_with_value_missing(self):
        x = 5
        array = [0,1,2,3,4]
        self.assertEqual(binary_search(x,array), False)

    def test_binary_search_with_value_found(self):
        x = 5
        array = [1,2,3,4,5,6,7]
        self.assertEqual(binary_search(x, array), 4)

unittest.main()
