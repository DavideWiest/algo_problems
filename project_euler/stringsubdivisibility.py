

numToDigits = lambda n: [int(d) for d in str(n)]
digitsToNum = lambda ds: int("".join(str(n) for n in ds))
allUnique = lambda x: len(x) == len(set(x))

END = 7
DIVISORS = [2,3,5,7,11,13,17]
STARTING_LIST = [a for a in range(100, 1000) if allUnique(numToDigits(a))]

class conditions():
    def __getitem__(self, i):
        return lambda x,y,z: digitsToNum(x,y,z) % DIVISORS[i] == 0
    
def recursivelyFindPandigitals(d1,d2, digitsUsed, level, conditions):
    if level >= END: return [[0]]

    fittingDigits = []
    for i in range(10):
        if i in digitsUsed: continue
        if not conditions[level](d1, d2, i): continue

        digitsUsed.append(i)
        fittingDigits += [[i] + followingNums \
            for followingNums in recursivelyFindPandigitals(d2, i, digitsUsed, level+1, conditions)]
        digitsUsed.remove(i)

    return fittingDigits

def recursivelyFindPandigitalsStart(startingList):
    pandigitals = []
    for num in startingList:
        digitsUsed = numToDigits(num)
        pandigitals += [
            digitsToNum(*digitsUsed, *fittingDigits[:-1]) \
            for fittingDigits in recursivelyFindPandigitals(digitsUsed[-2], digitsUsed[-1], digitsUsed, 0, conditions())]

    return pandigitals

if __name__ == '__main__':
    pandigitals = recursivelyFindPandigitalsStart(STARTING_LIST)
    print(sum(pandigitals))



class conditionsAsString():
    def __getitem__(self, i):
        return lambda x,y,z: f"{digitsToNum(x,y,z)} % {DIVISORS[i]} = {digitsToNum(x,y,z) % DIVISORS[i]}"

def testDivisions(pandigitals):
    numStartingDigits = len(str(STARTING_LIST[0]))
    conditionsAsStringInstance = conditionsAsString()
    for pandigital in pandigitals:
        pandigital = pandigital
        digitsToTest = numToDigits(pandigital)[numStartingDigits-2:]
        print(pandigital)
        for i, cond in enumerate(conditions):
            print(conditionsAsStringInstance[i](*digitsToTest[i:i+3]))
            print(cond(*digitsToTest[i:i+3]))