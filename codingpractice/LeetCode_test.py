

import LeetCode
import unittest

class LeetCode_test(unittest.TestCase, LeetCode.LeetCode):
    
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
    def test_increment(self):
        assert LeetCode.LeetCode.increment(3) == 4
    def test_descrement(self):
        assert LeetCode.LeetCode.decrement(3) == 2
    def test_1twoSum(self):
        nums = {1,2,3,4}
        target = 5
        assert LeetCode.LeetCode.twoSum1(LeetCode, nums, target) == {1,2,3,4}
    
        
