from typing import List

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        return self.profitableSchemesInner(n, minProfit, group, profit) % (1_000_000_007)

    def profitableSchemesInner(self, n: int, minProfit: int, group: List[int], profit: List[int], memo={}) -> int:
        s = 0
        
        if minProfit <= 0:
            s += 1
        
        for i in range(len(group)):
            if n-group[i] >= 0:
                
                s2, memo = self.profitableSchemesInner(n-group[i], minProfit-profit[i], group[i+1:], profit[i+1:], memo)
                s += s2

        return s


if __name__ == '__main__':
    sl = Solution()
    # print(sl.profitableSchemes(5, 3, [2,2], [2,3]))
    print("----")
    print(sl.profitableSchemes(10, 5, [2,3,5], [6,7,8]))
