from string import ascii_uppercase

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""

        while columnNumber > 0:
            mod = (columnNumber - 1) % 26
            result = ascii_uppercase[mod] + result
            columnNumber = int((columnNumber - mod) / 26)

        return result
    
if __name__ == "__main__":
    sl = Solution()
    print(sl.convertToTitle(1))
    print(sl.convertToTitle(26))
    print(sl.convertToTitle(702))
    print(sl.convertToTitle(701))