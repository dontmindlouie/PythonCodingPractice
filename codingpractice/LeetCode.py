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
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i + j == target:
                    return {i,j}
        
        return nums