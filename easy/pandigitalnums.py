import math
from tqdm import trange

DIGITS = [n for n in range(1,10)]

def digitsOfNum(n):
    if n < 0: n *= -1
    if n < 10: return [n]
    mx = 1
    digits = []
    while mx<n:
        mx *= 10

    while n>1:
        mx /= 10
        digits.append(math.floor(n/mx))
        n -= mx * digits[-1]

        return digits

def isPandigital(m1,m2,p) -> bool:
    "True if arguments have all digits from 1 to 9"
    
    combinedDigits = digitsOfNum(m1) + digitsOfNum(m2) + digitsOfNum(p)
    if len(combinedDigits) != 10: return False
    

    return all(d in combinedDigits for d in DIGITS)

def findAllPandigital() -> list:
    "find all pandigital numbers until some limit"
    # avoid switched multipliers (m1 always smaller than m2)

    pandigitals = []
    # multiplicators 
    m1_lo, m1_hi = 10, 100
    m2_lo, m2_hi = 100, 1000

    for m1 in trange(m1_lo, m1_hi):
        for m2 in range(m2_lo, m2_hi):
            if isPandigital(m1,m2,m1*m2):
                pandigitals.append(m1*m2)
       
    return pandigitals

if __name__ == '__main__':
    print(sum(findAllPandigital()))

# m1 * m2 * p has 10 digits
# check for pandigital only if thats true for the nums
# break if nums reach 11 digits combined (multiplicators must be incremented that way)


# 
