import math

def numDigits(n):
    if n < 0: n *= -1
    if n < 10: return [n]
    mx = 1
    digits = []
    while mx<n:
        mx *= 10

    while mx>1:
        mx /= 10
        digits.append(math.floor(n/mx))
        n -= mx * digits[-1]

    return digits

def switchKV(aDict):
    newDict = {v: [] for v in aDict.values()}
    for k,v in aDict.items():
        newDict[v].append(k)
    return newDict

SQUARED_DIGITS = set(numDigits(n*n)[-1] for n in range(1,10))
SQAURE_UNREACHABLE_DIGITS = set(filter(lambda x: x not in SQUARED_DIGITS, (n for n in range(1,10))))
SQAURE_FIRST_DIGITS = switchKV({n: numDigits(n*n)[-1] for n in range(1,10)})

def isSquareNumber(n):
    firstDigit = numDigits(n)[-1]
    
    if firstDigit in SQAURE_UNREACHABLE_DIGITS:
        return False
    
    for rootDigit in SQAURE_FIRST_DIGITS[firstDigit]:
        for i in range(rootDigit, n, 10):
            if i*i == n:
                return True
            elif i*i > n:
                break
        
    return False
    
if __name__=='__main__':
    print(isSquareNumber(4))
    print(isSquareNumber(81))
    print(isSquareNumber(9))
    print(isSquareNumber(24))
    print(isSquareNumber(72))