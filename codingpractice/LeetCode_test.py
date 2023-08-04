

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
        nums = [2,7,11,15]
        target = 9
        assert LeetCode.LeetCode.twoSum1(LeetCode, nums, target) == [0,1]
        
    def test_1twoSum2(self):
        nums = [3,2,4]
        target = 6
        result = LeetCode.LeetCode.twoSum1(LeetCode, nums, target)
        assert result == [1,2]
        
    def test_1twoSum3(self):
        nums = [3,3]
        target = 6
        result = LeetCode.LeetCode.twoSum1(LeetCode, nums, target)
        assert result == [0,1]
    
        
