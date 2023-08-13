

import LeetCode
import unittest
import LeetCodeObject

class LeetCode_test(unittest.TestCase, LeetCode.LeetCode):
    
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
    def test_increment(self):
        assert LeetCode.LeetCode.increment(3) == 4
        
    def test_descrement(self):
        assert LeetCode.LeetCode.decrement(3) == 2
        
    def test_1twoSum1a(self):
        nums = [2,7,11,15]
        target = 9
        assert LeetCode.LeetCode.twoSum1(LeetCode, nums, target) == [0,1]
        
    def test_twoSum1b(self):
        nums = [3,2,4]
        target = 6
        result = LeetCode.LeetCode.twoSum1(LeetCode, nums, target)
        assert result == [1,2]
        
    def test_twoSum1c(self):
        nums = [3,3]
        target = 6
        result = LeetCode.LeetCode.twoSum1(LeetCode, nums, target)
        assert result == [0,1]
        
    def test_palendrome1a(self):
        x = 121
        expected = True
        result = LeetCode.LeetCode.palendrome9(LeetCode, x)
        assert result == expected
        
        
    def test_palendrome1b(self):
        x = -121
        expected = False
        result = LeetCode.LeetCode.palendrome9(LeetCode, x)
        assert result == expected
        
    def test_palendrome1c(self):
        x = 10
        expected = False
        result = LeetCode.LeetCode.palendrome9(LeetCode, x)
        assert result == expected
        

    def test_palendrome1a1(self):
        x = 121
        expected = True
        result = LeetCode.LeetCode.palendrome9a(LeetCode, x)
        assert result == expected
        
    def test_romanToInt13a1(self):
        s = "III"
        expected = 3
        result = LeetCode.LeetCode.romanToInt13(LeetCode, s)
        assert result == expected
    
    def test_romanToInt13a2(self):
        s = "IV"
        expected = 4
        result = LeetCode.LeetCode.romanToInt13(LeetCode, s)
        assert result == expected
        
    def test_romanToInt13a2(self):
        s = "LVIII"
        expected = 58
        result = LeetCode.LeetCode.romanToInt13(LeetCode, s)
        assert result == expected
        
    def test_romanToInt13a3(self):
        s = "MCMXCIV"
        expected = 1994
        result = LeetCode.LeetCode.romanToInt13(LeetCode, s)
        assert result == expected
        
    def test_longestCommonPrefix14a1(self):
        strs = ["flower","flow","flight"]
        expected = "fl"
        result = LeetCode.LeetCode.longestCommonPrefix14a(self, strs)
        assert result == expected
    
    def test_longestCommonPrefix14a2(self):
        strs = ["dog","racecar","car"]
        expected = ""
        result = LeetCode.LeetCode.longestCommonPrefix14a(self, strs)
        assert result == expected
        
    def test_longestCommonPrefix14a3(self):
        strs = ["ab", "a"]
        expected = "a"
        result = LeetCode.LeetCode.longestCommonPrefix14a(self, strs)
        assert result == expected
        
    def test_validParenthesis20a1(self):
        s = "()"
        expected = True
        result = LeetCode.LeetCode.validParenthesis20a(self, s)
        assert result == expected
        
    def test_validParenthesis20a2(self):
        s = "()[]{}"
        expected = True
        result = LeetCode.LeetCode.validParenthesis20a(self, s)
        assert result == expected
        
    def test_validParenthesis20a3(self):
        s = "(]"
        expected = False
        result = LeetCode.LeetCode.validParenthesis20a(self, s)
        assert result == expected
        
    def test_validParenthesis20a4(self):
        s = "([)]"
        expected = False
        result = LeetCode.LeetCode.validParenthesis20a(self, s)
        assert result == expected
        
    def test_validParenthesis20a5(self):
        s = "{[]}"
        expected = True
        result = LeetCode.LeetCode.validParenthesis20a(self, s)
        assert result == expected
        
    def test_validParenthesis20a6(self):
        s = "]"
        expected = False
        result = LeetCode.LeetCode.validParenthesis20a(self, s)
        assert result == expected
        
    def test_validParenthesis20a7(self):
        s = "["
        expected = False
        result = LeetCode.LeetCode.validParenthesis20a(self, s)
        assert result == expected
        
    # def test_mergeTwoList21a1(self):
    #     list1: [1,2,3]
    #     list2: [1,3]
    #     expected = [1,1,2,3,3]
    #     result = LeetCode.LeetCode.mergeTwoLists21(self, list1, list2)
    #     assert result == expected
    