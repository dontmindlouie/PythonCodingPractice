from math import floor
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
    
    def searchInsert35(self, nums: List[int], target: int) -> int:
        lowI = 0
        highI = len(nums) - 1
        if nums[len(nums)-1] < target:
            return len(nums)
        if nums[0] > target:
            return 0
        
        while lowI < highI:
            lowI, highI = LeetCode.binarySearch35(lowI, highI, target, nums)
        
        return lowI
        
    def binarySearch35(lowI: int, highI: int, target: int, nums: List[int]) -> (int, int):
        midI = floor((highI - lowI) / 2) + lowI
        if target == nums[midI]:
            return midI, midI
        if lowI + 1 == highI:
            return highI, highI
        if target > nums[midI]:
            return midI, highI
        return lowI, midI
    
    def mySqrt69(self, x) -> int: 
        if (x == 0): return 0
        if (x == 1): return 1
        temp = range(x) # todo use an integer instead lol
        lowI = 0
        highI = len(temp)
        return LeetCode.sqrt69BinarySearch(temp, lowI, highI, x)
        
    def sqrt69BinarySearch(temp, lowI, highI, target) -> int:
        midI = (lowI + highI) // 2
        if temp[midI] * temp[midI] == target:
            return midI
        if lowI + 1 == highI:
            return lowI
        if temp[midI] * temp[midI] > target:
            return LeetCode.sqrt69BinarySearch(temp, lowI, midI, target)
        return LeetCode.sqrt69BinarySearch(temp, midI, highI, target)
    
    #todo
    def convertToTitle168(self, columnNumber: int) -> str:
        alphaDict = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H",
                     9: "I", 10: "J", 11: "K", 12: "L", 13: "M", 14: "N", 15: "O",
                     16: "P", 17: "Q", 18: "R", 19: "S", 20: "T", 21: "U", 22: "V",
                     23: "W", 24: "X", 25: "Y", 26: "Z"}
        
        result = ""
        larger = columnNumber / 26
        smaller = columnNumber % 26
        resi = 0
        if columnNumber == 0:
            return ""
        result = "A"
        columnNumber -= 1
        # while columnNumber > 0 :
            # "Z" -> "A"
            # "AZ" -> "BA" 
            # "ZZ" -> "AAA"
            # "ZAZ" -> "ZBA"
            # "AZZ" -> "BAA"
            # if preResult[preI] == 26:
            #     tempI = preI
            #     tempI -= 1
            #     while tempI >= 0 and preResult[tempI] == 26:
            #         if preResult[tempI] < 26:
            #             preResult[tempI] = 1
            #             #return
            #         else: tempI -= 1
            #     else:
            #         #All A plus 1
            #         tempI -= 1
            # else:
            #     preResult[preI] += 1
            #     columnNumber -= 1
        return result
    
    def findKey(alphaDict, value): 
        for i in range(alphaDict):
            if alphaDict[i] == value:
                return i
            
    def majorityElement169(self, nums: List[int]) -> int:
        alphabetTracker = {}
        target = (len(nums))/2
        for i in nums:
            if i not in alphabetTracker:
                alphabetTracker[i] = 1
            else: alphabetTracker[i] += 1
            if alphabetTracker[i] > target:
                return i
        return None
    
    def titleToNumber171(self, columnTitle: str) -> int:
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        reverseTitle = columnTitle[::-1]
        result = 0
        for i in range(0,len(reverseTitle)):
            temp = 26**i*(alphabet.index(reverseTitle[i])+1)
            result += temp
        return result
        
    def reverseBits190(self, n: int) -> int:
        binaryInput = bin(n)
        trimmed = binaryInput[2:]
        reversedInput = trimmed[::-1]
        reversedFomrated = reversedInput + ("0"*(32-len(reversedInput)))
        result = int(reversedFomrated,2)
        return result
    
    def hammingWeight191(self, n: int) -> int:
        nString = bin(n)[2::]
        result = 0
        for i in nString:
            if i == '1':
                result += 1
        return result
    
    def isHappy(self, n: int) -> bool:
        tracker = {n}
        while(n != 1):
            stringN = str(n)
            interSum = 0
            for letter in stringN:
                interSum += int(letter) ** 2
            if interSum in tracker:
                return False
            tracker.add(interSum)
            n = interSum
        return True
        
    def compareListNode(self, listNode1: ListNode, listNode2: ListNode) -> bool:
        while(listNode1 != None and listNode2 != None):
            if listNode1.val != listNode2.val:
                return False
            listNode1 = listNode1.next
            listNode2 = listNode2.next
        if ((listNode1 != None) != (listNode2 != None)):
            return False
        return True
        
        
    def removeElements203(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # n
        if head == None: return head
        while(head.val == val):
            head = head.next
            if head == None: 
                return head
        node = head
        while(node.next != None):
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
            if node == None:
                return head
        return head

    def isIsomorphic205( s: str, t: str) -> bool:
        dS, dT = {}, {}
        if len(s) != len(t): 
            return False
        for iS, val in enumerate(s):
            if val not in dS:
                dS[val] = [iS]
            else:
                dS[val].append(iS)
        for iT, val in enumerate(t):
            if val not in dT:
                dT[val] = [iT]
            else:
                dT[val].append(iT)
        if sorted(list(dS.values())) == sorted(list(dT.values())):
            return True
        else: 
            return False
        
    def reverseList206(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return None
        if head.next == None:
            return head
        node1 = head
        node2 = head.next
        node3 = node2.next
        node1.next = None
        node2.next = node1
        
        while node3 != None:
            node1 = node2
            node2 = node3
            node3 = node3.next
            node2.next = node1
        
        return node2
            
    def reverseList206_recursion(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return None
        if head.next == None:
            return head
        node1 = head
        node2 = head.next
        node3 = node2.next
        node1.next = None
        node2.next = node1
        
        node2 = LeetCode.__reverseList206_reverse(node1, node2, node3)
        
        return node2
    
    def __reverseList206_reverse(node1: ListNode, node2: ListNode, node3: ListNode) -> Optional[ListNode]:
        if node3 == None: 
            return node2
        node1 = node2
        node2 = node3
        node3 = node3.next
        node2.next = node1
    
        return LeetCode.__reverseList206_reverse(node1, node2, node3)
    
    def containsDuplicate217(self, nums: List[int]) -> bool:
        nums_set = set()
        for i in nums:
            if i in nums_set:
                return True
            else:
                nums_set.add(i)
        return False
    
    def containsNearbyDuplicate219(self, nums: List[int], k: int) -> bool:
        numsList = {}
        for i, iVal in enumerate(nums):
            for j, jVal in enumerate(numsList):
                if nums[i] == numsList[j] and abs(i - (j)) <= k:
                    return True
            numsList[i] = iVal
                
        return False
                
        

        
        
        