import math
import random
import numpy as np
from matplotlib import pyplot as plt

from performance import compare_speed

def abline(slope, intercept, color, label):
    """Plot a line from slope and intercept"""
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, '--', c=color, label=label)

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

def numDigitsByStr(n):
    return [int(d) for d in str(n)]

def switchKV(aDict):
    newDict = {v: [] for v in aDict.values()}
    for k,v in aDict.items():
        newDict[v].append(k)
    return newDict

SQUARED_DIGITS = set(numDigits(n*n)[-1] for n in range(10))
SQAURE_UNREACHABLE_DIGITS = set(filter(lambda x: x not in SQUARED_DIGITS, (n for n in range(10))))
SQAURE_UNREACHABLE_DIGITS_STR = set([str(n) for n in SQAURE_UNREACHABLE_DIGITS])
SQAURE_FIRST_DIGITS = switchKV({n: numDigits(n*n)[-1] for n in range(10)})
SQAURE_FIRST_DIGITS_STR = {str(k):v for k,v in SQAURE_FIRST_DIGITS.items()}

def squareNumInRange(target, lo, hi):
    new = (lo+hi)*0.5
    newSq = new**2
    if newSq == target: return new
    if hi-lo <= 1:
        if lo**2 == target: return lo
        elif hi**2 == target: return hi
        return False
    if newSq > target: return squareNumInRange(target, lo, math.ceil(new)) # check for bigger first because new*new will statistically more often be too large
    elif newSq < target: return squareNumInRange(target, math.floor(new), hi)

def squareNumInRange(target, lo, hi):
    f = lo-hi
    new = lo+f*0.5
    newSq = new**2
    if newSq == target: return new
    if f <= 1:
        g = lo**2
        if g == target: return lo
        elif g + 2*lo*f + f**2 == target: return hi
        return False
    if newSq > target: return squareNumInRange(target, lo, math.ceil(new)) # check for bigger first because new*new will statistically more often be too large
    elif newSq < target: return squareNumInRange(target, math.floor(new), hi)

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

def isSquareNumber2(n):
    firstDigit = numDigits(n)[-1]
    
    if firstDigit in SQAURE_UNREACHABLE_DIGITS: return False
    
    for rootDigit in SQAURE_FIRST_DIGITS[firstDigit]:
        if rootDigit > math.floor(n/2): continue

        a = squareNumInRange(n, rootDigit, math.floor(n/2))
        if a != True: return a
        
    return False
    
def isSquareNumber3(n):
    sqrt = math.sqrt(n)
    if sqrt == round(sqrt):
        return True
    return False

def isSquareNumber4(n):    
    if str(n)[-1] in SQAURE_UNREACHABLE_DIGITS_STR: return False
    
    for rootDigit in [r for r in SQAURE_FIRST_DIGITS_STR[str(n)[-1]] if r > math.floor(n/2)]:
        a = squareNumInRange(n, rootDigit, math.floor(n/2))
        if a != True: return a
        
    return False

if __name__=='__main__':
    # print(isSquareNumber(4))
    # print(isSquareNumber(81))
    # print(isSquareNumber(9))
    # print(isSquareNumber(24))
    # print(isSquareNumber(72))
    # print("-------")
    # print(isSquareNumber2(4))
    # print(isSquareNumber2(81))
    # print(isSquareNumber2(9))
    # print(isSquareNumber2(24))
    # print(isSquareNumber2(72))

    # inputs = [[n] for n in [0,1,4,9,16,25,36,49,64,81,100,121,144,3034564,2205225,2238016]] + \
    inputs = [[a] for a in range(1,500_000_0) if random.randint(1,1000) == 69]
    # filterLambda = lambda x: x == True
    # inputs = [[n] for n in [0,1,4,9,16,25,36,49,64,81,100,121,144,3034564,2205225,2238016]]
    filterLambda = lambda x: True
    fnList = [isSquareNumber2,isSquareNumber3, isSquareNumber4]
    input_time_dict = compare_speed(fnList, inputs, print_inputs=True, timeUnit="ns", filterByOutputLambda=filterLambda)

    colorByIndex = ["g", "r", "m", "c"]

    for fnIndex in input_time_dict:
        fnName = fnList[fnIndex]
        color = colorByIndex[fnIndex]
        keys = list(input_time_dict[fnIndex].keys())
        values = list(input_time_dict[fnIndex].values())
        plt.scatter(keys, values, c=color)
        out = np.polyfit(keys, values, 1)
        slope, intercept = out[0], out[1]
    
        abline(slope, intercept, color, fnName)

    plt.show()
