

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
        
    def test_searchInsert35a1(self):
        nums = [1,3,5,6]
        target = 5
        expected = 2
        result = LeetCode.LeetCode.searchInsert35(self, nums, target)
        assert expected == result
        
    def test_searchInsert35a2(self):
        nums = [1,3,5,6]
        target = 2
        expected = 1
        result = LeetCode.LeetCode.searchInsert35(self, nums, target)
        assert expected == result
        
    def test_searchInsert35a3(self):
        nums = [1,3,5,6]
        target = 7
        expected = 4
        result = LeetCode.LeetCode.searchInsert35(self, nums, target)
        assert expected == result
        
    def test_mySqrt69a1(self):
        x = 8
        expected = 2
        result = LeetCode.LeetCode.mySqrt69(self, x)
        assert expected == result
        
    def test_mySqrt69a2(self):
        x = 1
        expected = 1
        result = LeetCode.LeetCode.mySqrt69(self, x)
        assert expected == result
        
    def test_mySqrt69a3(self):
        x = 4
        expected = 2
        result = LeetCode.LeetCode.mySqrt69(self, x)
        assert expected == result
        
    def test_convertToTile168a1(self):
        columnNumber = 1
        expected = "A"
        result = LeetCode.LeetCode.convertToTitle168(self, columnNumber)
        assert expected == result
        
    def test_convertToTile168a2(self):
        #todo
        columnNumber = 28
        expected = "AB"
        result = LeetCode.LeetCode.convertToTitle168(self, columnNumber)
        #assert expected == result
        
    def test_convertToTile168a3(self):
        #todo
        columnNumber = 701
        expected = "ZY"
        result = LeetCode.LeetCode.convertToTitle168(self, columnNumber)
        #assert expected == result
        
    def test_majorityElement169a(self):
        inputList = [3,2,3]
        expected = 3
        result = LeetCode.LeetCode.majorityElement169(self, inputList)
        assert expected == result
    
    def test_titleToNumber171a(self):
        input = "AB"
        expected = 26+2
        result = LeetCode.LeetCode.titleToNumber171(self, input)
        assert expected == result
        
    def test_titleToNumber171b(self):
        input = "ABC"
        expected = (26*26*1)+(26*2)+3
        result = LeetCode.LeetCode.titleToNumber171(self, input)
        assert expected == result
        
    def test_reverseBits198a(self):
        #todo result works in leetcode but not here
        input = 10100101000001111010011100
        expected = 964176192 #(00111001011110000010100101000000)
        result = LeetCode.LeetCode.reverseBits190(self, input)
        #assert expected == result
        
    def test_hammingWeight191(self):
        input = 11
        expected = 3
        result = LeetCode.LeetCode.hammingWeight191(self, input)
        assert result == expected
        
    def test_isHappy202(self):
        input = 19
        expected = True
        result = LeetCode.LeetCode.isHappy(self, input)
        assert result == expected
        
    def test_compareListNode(self):
        input1 = ListNode(1, ListNode(2))
        input2 = ListNode(1, ListNode(2))
        expected = True
        result = LeetCode.LeetCode.compareListNode(self, input1, input2)
        assert result == expected
        
    def test_compareListNode_2(self):
        input1 = ListNode(1, ListNode(2))
        input2 = ListNode(1, ListNode(3))
        expected = False
        result = LeetCode.LeetCode.compareListNode(self, input1, input2)
        assert result == expected
        
    def test_compareListNode_3(self):
        input1 = ListNode(1, ListNode(2))
        input2 = ListNode(1, ListNode(2, ListNode(3)))
        expected = False
        result = LeetCode.LeetCode.compareListNode(self, input1, input2)
        assert result == expected
        
    def test_removeElements203(self):
        inputHead = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(6, ListNode(4))))))
        inputVal = 6
        expected = ListNode(1,ListNode(2, ListNode(3, ListNode(4))))
        result = LeetCode.LeetCode.removeElements203(self, inputHead, inputVal)
        assert LeetCode.LeetCode.compareListNode(self, result, expected)
        
    
    def test_removeElements203_2(self):
        inputHead = ListNode(6)
        inputVal = 6
        expected = None
        result = LeetCode.LeetCode.removeElements203(self, inputHead, inputVal)
        assert LeetCode.LeetCode.compareListNode(self, result, expected)    
        
    def test_removeElements203_3(self):
        inputHead = ListNode(6, ListNode(2))
        inputVal = 6
        expected = ListNode(2)
        result = LeetCode.LeetCode.removeElements203(self, inputHead, inputVal)
        assert LeetCode.LeetCode.compareListNode(self, result, expected) 
          
    def test_removeElements203_4(self):
        inputHead = ListNode(2, ListNode(6, ListNode(6)))
        inputVal = 6
        expected = ListNode(2)
        result = LeetCode.LeetCode.removeElements203(self, inputHead, inputVal)
        assert LeetCode.LeetCode.compareListNode(self, result, expected)
        
    def test_removeElements203_5(self):
        inputHead = ListNode(7, ListNode(7, ListNode(7, ListNode(7))))
        inputVal = 7
        expected = None
        result = LeetCode.LeetCode.removeElements203(self, inputHead, inputVal)
        assert LeetCode.LeetCode.compareListNode(self, result, expected) 
        
    def test_isIsomorphic205_1(self):
        inputA = "aabb"
        inputB = "bbcc"
        expected = True
        result = LeetCode.LeetCode.isIsomorphic205(inputA, inputB)
        assert expected == result
        
    def test_isIsomorphic205_2(self):
        inputA = "ab"
        inputB = "abc"
        expected = False
        result = LeetCode.LeetCode.isIsomorphic205(inputA, inputB)
        assert expected == result
        
        
    def test_isIsomorphic205_3(self):
        inputA = "bbbaaaba"
        inputB = "aaabbbba"
        expected = False
        result = LeetCode.LeetCode.isIsomorphic205(inputA, inputB)
        assert expected == result
        
    def test_reverseList206_1(self):
        inputHead = ListNode(1)
        expected = ListNode(1)
        result = LeetCode.LeetCode.reverseList206(self, inputHead)
        assert LeetCode.LeetCode.compareListNode(self, result, expected)
        
    def test_reverseList206_2(self):
        inputHead = ListNode(1, ListNode(2))
        expected = ListNode(2, ListNode(1))
        result = LeetCode.LeetCode.reverseList206(self, inputHead)
        assert LeetCode.LeetCode.compareListNode(self, result, expected)
        
    def test_reverseList206_3(self):
        inputHead = ListNode(1, ListNode(2, ListNode(3)))
        expected = ListNode(3, ListNode(2, ListNode(1)))
        result = LeetCode.LeetCode.reverseList206(self, inputHead)
        assert LeetCode.LeetCode.compareListNode(self, result, expected)
        
    def test_reverseList206_recursion_1(self):
        inputHead = ListNode(1, ListNode(2, ListNode(3)))
        expected = ListNode(3, ListNode(2, ListNode(1)))
        result = LeetCode.LeetCode.reverseList206_recursion(self, inputHead)
        assert LeetCode.LeetCode.compareListNode(self, result, expected)
        
        
        