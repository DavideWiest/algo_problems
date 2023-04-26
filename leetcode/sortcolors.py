from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        offset = 0
        for iOuter in range(len(nums)):

            i = offset+iOuter
            color = nums[i]
            if color == 0:
                i2 = i-1
                i3 = i
                while i2>=0:
                    nums[i3] = nums[i2]
                    i2 -= 1
                    i3 -= 1
                if iOuter != 0:
                    offset -= 1
                nums[0] = 0
            elif color == 2:
                i2 = i+1
                i3 = i
                while i2<=len(nums)-1:
                    nums[i3] = nums[i2]
                    i2 += 1
                    i3 += 1
                if iOuter != 0:
                    offset -= 1
                nums[len(nums)-1] = 2
        
        for i in range(offset):
            i = len(nums)-1-offset

            color = nums[i]
            if color == 0:
                i2 = i-1
                i3 = i
                while i2>=0:
                    nums[i3] = nums[i2]
                    i2 -= 1
                    i3 -= 1
                if iOuter != 0:
                    offset -= 1
                nums[0] = 0
            elif color == 2:
                i2 = i+1
                i3 = i
                while i2<=len(nums)-1:
                    nums[i3] = nums[i2]
                    i2 += 1
                    i3 += 1
                if iOuter != 0:
                    offset -= 1
                nums[len(nums)-1] = 2



sl = Solution()
arr = [1,0,0]
sl.sortColors(arr)
print(arr)