class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        sIndex = 0
        for i in range(len(p)):
            c = p[i]
            
            if c == "*":
                cPrev = p[i-1]

                while self.charsMatch(s[sIndex], cPrev):
                    sIndex += 1

                    if sIndex >= len(s):
                        break

                    print(f"Checking match: {s[sIndex:]} & {p[i:]}")
                    if self.isMatch(s[sIndex:], p[i:]):
                        return True

            elif self.isNotStarStatement(p, i+1):
                print(sIndex)
                print(s)
                print(c)
                if not self.charsMatch(s[sIndex], c):
                    return False
                sIndex += 1
        
        if sIndex < len(s):
            return False
        
        return True
    
    def isNotStarStatement(self, p, i):
        if i < len(p):
            return p[i] != "*"
        
        return False
    
    def charsMatch(self, sc, pc):
        if pc == ".":
            return True
        
        return pc == sc
        


if __name__ == '__main__':
    sl = Solution()

    sppairs = [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("mississippi", "mis*is*ip*.", True)
    ]

    for sppair in sppairs:
        result = sl.isMatch(sppair[0], sppair[1])
        isCorrect = result == sppair[2]
        print(f"{result} - {isCorrect}")