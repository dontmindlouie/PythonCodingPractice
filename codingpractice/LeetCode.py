from typing import List

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