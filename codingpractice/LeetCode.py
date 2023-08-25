from typing import List, Optional
from LeetCodeObject import ListNode

class LeetCode():
    def __init__(self) -> None:
        pass
    def increment(x):
        print("increment")
        return x + 1

    def decrement(x):
        print("decrement")
        return x - 1
    
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        numTemp = {}
        
        for i in range(len(nums)):
            compl = target - nums[i]
            if compl in numTemp and numTemp[compl] != i:
                return [numTemp[compl], i]
            numTemp[nums[i]] = i
            
        return []
    
    def palendrome9(self, x):
        if x < 0: return False
        backward = str(x) [::-1]
        if x == int(backward):
            return True
        else:
            return False
        
    def palendrome9a(self, x):
        if x < 0: return False
        
        xi = x
        reversed = 0
        
        while xi != 0:
            digit = xi % 10
            reversed = reversed * 10 + digit
            xi //= 10
        
        return reversed == x
    
    def romanToInt13(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        test = len(s)
        result = 0
        i = 0
        while i < len(s):
            match s[i]:
                case "I":
                    if i + 1 >= len(s):
                        return result + 1
                    elif s[i + 1] == "V":
                        result += 4
                        i += 1
                    elif s[i + 1] == "X":
                        result += 9
                        i += 1
                    else:
                        result += 1
                case "V":
                    result += 5
                case "X":
                    if i + 1 >= len(s):
                        return result + 10
                    elif s[i + 1] == "L":
                        result += 40
                        i += 1
                    elif s[i + 1] == "C":
                        result += 90
                        i += 1
                    else: result += 10
                case "X":
                    result += 10
                case "L":
                    result += 50
                case "C":
                    if i + 1 >= len(s):
                        return result + 100
                    elif s[i + 1] == "D":
                        result += 400
                        i += 1
                    elif s[i + 1] == "M":
                        result += 900
                        i += 1
                    else: result += 100
                case "D":
                    result += 500
                case "M":
                    result += 1000
            i += 1
        return result
    
    def longestCommonPrefix14a(self, strs: List[str]) -> str:
        result = ""
        iLetter = 0
        while iLetter < len(strs[0]):
            letter = strs[0][iLetter]
            for iWord in range(len(strs)):
                if iLetter + 1 > len(strs[iWord]):
                    return result
                if strs[iWord][iLetter] != letter:
                    return result
            result += letter
            iLetter += 1
        return result
    
    def validParenthesis20a(self, s: str) -> bool:
        bracketTracker = []
        for i in range(len(s)):
            match s[i]:
                case "(":
                    bracketTracker.append("(")
                case "[":
                    bracketTracker.append("[")
                case "{":
                    bracketTracker.append("{")
                case ")":
                    if len(bracketTracker) == 0:
                        return False
                    if bracketTracker[-1] == "(":
                        del bracketTracker[-1]
                    else: return False
                case "]":
                    if len(bracketTracker) == 0:
                        return False
                    if bracketTracker[-1] == "[":
                        del bracketTracker[-1]
                    else: return False
                case "}":
                    if len(bracketTracker) == 0:
                        return False
                    if bracketTracker[-1] == "{":
                        del bracketTracker[-1]
                    else: return False
        if len(bracketTracker) > 0: return False
        return True
    
    def mergeTwoLists21(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        result = ListNode()
        resultHead = result
        
        while(list1 != None or list2 != None):
            result.next = ListNode()
            result = result.next
            if list1 != None: 
                if list2 != None:
                    if list1.val > list2.val:
                        result.val = list2.val
                        list2 = list2.next
                    else: 
                        result.val = list1.val
                        list1 = list1.next
                else: 
                    result.val = list1.val
                    list1 = list1.next
            else:
                if list2 != None:
                    result.val = list2.val
                    list2 = list2.next
        resultHead = resultHead.next
        return resultHead
        
    def removeDuplicates25(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return 1
        dupli = 0
        findDupl = False
        i = 1
        while(i < len(nums)):
            while nums[i] == nums[dupli]:
                i += 1
                if i >= len(nums): return dupli + 1
            dupli += 1
            nums[dupli] = nums[i]
            i += 1
        
        return dupli + 1
    
    def removeElement27(self, nums: List[int], val: int) -> int:
        if len(nums) == 0: return 0
        iremoved = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[iremoved] = nums[i]
                iremoved += 1
        return iremoved
    
    def strStr28(self, haystack: str, needle: str) -> int:

        hayI = 0
        while hayI < len(haystack): 
            if needle[0] == haystack[hayI]:
                needI = 0
                tempHayI = hayI
                while needI < len(needle) and tempHayI < len(haystack) and needle[needI] == haystack[tempHayI]:
                    needI += 1
                    tempHayI += 1
                if needI == len(needle):
                    return hayI
                elif tempHayI >= len(haystack):
                    return -1
            hayI += 1
        return -1