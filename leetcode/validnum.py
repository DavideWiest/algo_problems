class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.lower()

        if len(s) == 0 or s[0].lower() == "e":
            return False

        s = self.removeOptionalOperator(s)

        if s.count(".") > 1 or s.count("e") > 1:
            return False

        if "e" in s:
            s2 = s.split("e")[1]
            if len(s2) == 0:
                return False
            s2 = self.removeOptionalOperator(s2)
            if not s2.isdigit():
                return False
        
        if len(s) == 0:
            return False

        if s[0] == "e":
            return False
            

        return self.isInteger(s) or self.isFloat(s)
    
    def isInteger(self, s):
        return s.split("e")[0].isdigit()

    def isFloat(self, s):
        if s[0] == "." and len(s) == 1 or s.startswith(".e"):
            return False
        
        return all(self.isDigitOrDot(c) for c in s.split("e")[0])
    
    def removeOptionalOperator(self, s):
        if s[0] in ("+", "-"):
            s = s[1:]
        return s
    
    def isDigitOrDot(self, c):
        return c.isdigit() or c == "."

if __name__ == "__main__":
    sl = Solution()
    for nStr in ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", "-.2e-4", "46.e3"]:
        print(sl.isNumber(nStr))
    print("----")
    for nStr in ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53", "aaah", "", "1e", "-.", "+E3", "+.e", "+2.e", "+.e2"]:
        print(sl.isNumber(nStr))