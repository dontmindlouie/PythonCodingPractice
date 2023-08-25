

import LeetCode
import unittest
from LeetCodeObject import ListNode

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
        
    def test_mergeTwoList21a1(self):
        list1 = ListNode(1, ListNode(3))
        list2 = ListNode(1,ListNode(2))
        expected = ListNode(1,ListNode(1, 
            ListNode(2, ListNode(3))))
        result = LeetCode.LeetCode.mergeTwoLists21(self, list1, list2)
        while(expected != None):
            assert result.val == expected.val
            result = result.next
            expected = expected.next
            
    def test_removeDuplicates25a1(self):
        nums = [1,1,1,2,2,3]
        expected = 3
        expectedNums = [1,2,3]
        result = LeetCode.LeetCode.removeDuplicates25(self,nums)
        assert expected == result
        for i in range(len(expectedNums)):
            assert expectedNums[i] == nums[i]
            
    def test_removeDuplicates25a2(self):
        nums = [1,1]
        expected = 1
        expectedNums = [1]
        result = LeetCode.LeetCode.removeDuplicates25(self,nums)
        assert expected == result
        for i in range(len(expectedNums)):
            assert expectedNums[i] == nums[i]
            
    def test_removeElement27a1(self):
        nums = [3,2,2,3]
        val = 3
        expected = 2
        expectedNums = [2,2]
        result = LeetCode.LeetCode.removeElement27(self, nums, val)
        assert result == expected
        for i in range(len(expectedNums)):
            assert expectedNums[i] == nums[i]
            
    def test_removeElement27a2(self):
        nums = [3,3]
        val = 3
        expected = 0
        expectedNums = []
        result = LeetCode.LeetCode.removeElement27(self, nums, val)
        assert result == expected
        for i in range(len(expectedNums)):
            assert expectedNums[i] == nums[i]
            
    def test_strStr28a1(self):
        haystack = "sadbutsad"
        needle = "sad"
        expected = 0
        result = LeetCode.LeetCode.strStr28(self, haystack, needle)
        assert expected == result
        
    def test_strStr28a2(self):
        haystack = "butsad"
        needle = "sad"
        expected = 3
        result = LeetCode.LeetCode.strStr28(self, haystack, needle)
        assert expected == result
        
    def test_strStr28a3(self):
        haystack = "aaa"
        needle = "aaaa"
        expected = -1
        result = LeetCode.LeetCode.strStr28(self, haystack, needle)
        assert expected == result
        
        
        
        
    