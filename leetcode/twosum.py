from typing import List

import math

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:    
        prevIndices = list(range(len(nums)))
        prevIndices.sort(key=lambda x: nums[x])
        nums.sort()

        for i, n in enumerate(nums):
            foundIndex = self.findIndexBinarySearch(target-n, nums[i+1:])
            if foundIndex != -1:
                return [prevIndices[i], prevIndices[i+1+foundIndex]]
    
    def findIndexBinarySearch(self, target, nums: List[int]):
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if target == nums[0] else -1

        splitIndex = math.floor(len(nums)/2)

        if nums[splitIndex] < target:
            result = self.findIndexBinarySearch(target, nums[splitIndex+1:])
            if result != -1:
                return splitIndex+1+result
            else:
                return -1
        elif nums[splitIndex] > target:
            return self.findIndexBinarySearch(target, nums[:splitIndex])
        else:
            return splitIndex

if __name__ == "__main__":
    sl = Solution()
    print(sl.twoSum([3,2,3], 6))