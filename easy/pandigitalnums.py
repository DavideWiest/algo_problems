import math

def digitsOfNum(n) -> list:
    "find digits of a number"
    digits = []
    # use remainder division
    div = 1
    while n / div > 1:
        digits.append(math.floor(n % div))
        div *= 10
    return digits

def isPandigital(m1,m2,p) -> bool:
    "True if arguments have all digits from 1 to 9"

    digits = [n for n in range(1,10)]

    for d in digitsOfNum(m1):
        digits.remove(d)
    
    for d in digitsOfNum(m2):
        digits.remove(d)

    for d in digitsOfNum(p):
        digits.remove(d)

    return digits == []

def findAllPandigital() -> list:
    "find all pandigital numbers until some limit"
    # avoid switched multipliers (m1 always smaller than m2)

    pandigitals = []
    # multiplicators 
    m1_lo, m1_hi = 10, 100
    m2_lo, m2_hi = 100, 1000

    for m1 in range(m1_lo, m1_hi):
        for m2 in range(m2_lo, m2_hi):
            if isPandigital(m1,m2,m1*m2):
                pandigitals.append(m1*m2)



if __name__ == '__main__':
    # print(sum(findAllPandigital()))
    print(digitsOfNum(199))

# m1 * m2 * p has 10 digits
# check for pandigital only if thats true for the nums
# break if nums reach 11 digits combined (multiplicators must be incremented that way)


# 