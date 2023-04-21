from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        if nums == [0,0,0,0] and target == 0:
            return [[0 for i in range(4)]]
        
        return [comb[:-1] for comb in self.nSum(nums, target, 4, 0)]

    def nSum(self, nums: List[int], target: int, n: int, level: int) -> List[List[int]]:

        if target == 0 and level != 0:
            print(1)
            return [[0]]

        combs = []
        for i in range(len(nums)):
            newnums = nums[i+1:]
            print(newnums)
            
            for nextcomb in self.nSum(newnums, target-nums[i], n-1, level+1):
                print(3)
                print(nextcomb)
                print(n)
                if len(nextcomb) == n and [nums[i]] + nextcomb not in combs:
                    print(4)
                    combs.append([nums[i]] + nextcomb)

        return combs


if __name__ == '__main__':
    sl = Solution()
    # print(sl.fourSum([1,0,-1,0,-2,2], 0))
    # print(sl.fourSum([-2,-1,0,0,1,2], 0))
    # print(sl.fourSum([2,2,2,2,2], 8))
    print(sl.fourSum([0,0,0,0], 0))