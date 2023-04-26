from typing import List
import sys, math

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        ik = 0
        while k>0:
            ck = k % 10
            k = math.floor(k / 10)

            ik += 1
            i = len(num)-ik

            if i<0:
                num.insert(0, ck)
                continue

            if ck == 0:
                continue

            carry = (num[i]+ck) // 10
            num[i] = (num[i]+ck) % 10

            i2 = i
            while carry:
                i2 -= 1
                if i2 == -1:
                    num = [1] + num
                    break
                carry = (num[i2]+1) // 10
                num[i2] = (num[i2]+1) % 10

        return num


if __name__ == "__main__":
    sl = Solution()

    print(sl.addToArrayForm([0], 1000))
    # print(sl.addToArrayForm([9,0,9], 110))

    sys.exit(0)
    
    for num in range(1000):
        for k in range(20):
            if int("".join([str(y) for y in sl.addToArrayForm([int(x) for x in str(num)], k)])) != num+k:
                print(list(str(num)))
                print(k)
                print("-")
                print(sl.addToArrayForm([int(x) for x in str(num)], k))
                print("-----")