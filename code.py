from itertools import *
import unittest

def twosum(nums, target):
    storage = {}
    for i, n in enumerate(nums):
        n2 = target - n
        if n2 in storage:
            return [storage[n2], i]
        storage[n] = i
    return None

class TestMath(unittest.TestCase):
    def example1(self):
        self.assertEqual(twosum([2,7,11,15], 9), [0, 1])
    def example2(self):
        self.assertEqual(twosum([3,2,4], 6), [1, 2])
    def example3(self):
        self.assertEqual(twosum([3, 3], 6), [0, 1])

unittest.main(argv=[''], verbosity=2, exit=False)

