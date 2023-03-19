

def numDigitsByStr(n):
    return [int(d) for d in str(n)]

def mergeDigitsToNum(*nums):
    return int("".join(str(num) for num in nums))


# END = 9
END = 4

# DIVISORS = [3,5,7,11,13,17]
DIVISORS = [3,5,7,11]

conditions = [
    lambda x,y,z: mergeDigitsToNum(x,y,z) % div == 0
    for div in DIVISORS
]

conditionsAsRemainder = [
    lambda x,y,z: mergeDigitsToNum(x,y,z) % div
    for div in DIVISORS
]

# startingList = [a for a in range(1000, 9999, 2)]
startingList = [a for a in range(100, 999, 2)]

def recursivelyFindPandigitals(d1,d2, digitsUsed, level, conditions):
    if level >= END: return [[0]]

    fittingDigits = []
    for i in range(10):
        if i in digitsUsed: continue
        print(level)
        if not conditions[level](d1, d2, i): continue

        digitsUsed.append(i)
        fittingDigits += [[i] + followingNums \
            for followingNums in recursivelyFindPandigitals(d2, i, digitsUsed, level+1, conditions)]
        digitsUsed.remove(i)

    return fittingDigits

def recursivelyFindPandigitalsStart(startingList):
    pandigitals = []
    for num in startingList:
        digitsUsed = numDigitsByStr(num)
        pandigitals += [
            mergeDigitsToNum(*digitsUsed, *fittingDigits[:-1]) \
            for fittingDigits in recursivelyFindPandigitals(digitsUsed[-2], digitsUsed[-1], digitsUsed, 0, conditions)]

    return pandigitals

def testDivisions(pandigitals):
    numStartingDigits = len(str(startingList[0]))
    
    for pandigital in pandigitals:
        digitsToTest = numDigitsByStr(pandigital)[numStartingDigits-2:]
        print(pandigital)
        for i, cond in enumerate(conditions):
            print(digitsToTest[i:i+3])
            print(f"{mergeDigitsToNum(*digitsToTest[i:i+3])} % {DIVISORS[i]} = ", end="")
            print(mergeDigitsToNum(*digitsToTest[i:i+3]) % DIVISORS[i])
            print(conditionsAsRemainder[i](*digitsToTest[i:i+3]))
            print(cond(*digitsToTest[i:i+3]))
    

if __name__ == '__main__':
    # print(sum(recursivelyFindPandigitalsStart(startingList)))
    pandigitals = recursivelyFindPandigitalsStart(startingList)
    print(pandigitals)
    testDivisions(pandigitals)