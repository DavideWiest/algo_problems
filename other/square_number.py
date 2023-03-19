import math
import random
import numpy as np
from matplotlib import pyplot as plt
import sys

from _performance import compare_speed, abline, visualize_speed

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
    new = (lo+hi)*0.5
    newSq = new**2
    if newSq == target: return new
    if hi-lo <= 1:
        if lo**2 == target: return lo
        elif hi**2 == target: return hi
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
    if firstDigit == 10: firstDigit = 0
    
    if firstDigit in SQAURE_UNREACHABLE_DIGITS: return False
    
    for rootDigit in SQAURE_FIRST_DIGITS[firstDigit]:
        if rootDigit > math.floor(n/2): continue

        a = squareNumInRange(n, rootDigit, math.floor(n/2))
        if a != False: return a
        
    return False
    
def isSquareNumber3(n):
    sqrt = math.sqrt(n)
    if sqrt == round(sqrt):
        return sqrt
        
    return False

def isSquareNumber4(n):
    d = str(n)[-1]
    if d in SQAURE_UNREACHABLE_DIGITS_STR: return False
    f = math.floor(n/2)
    
    for rootDigit in [r for r in SQAURE_FIRST_DIGITS_STR[d] if r <= f]:
        a = squareNumInRange(n, rootDigit, f)
        if a != False: return a
    
    return False

def isSquareNumber5(n):
    d = str(n)[-1]
    if d in SQAURE_UNREACHABLE_DIGITS_STR: return False
    f = math.floor(n/2)
    
    for rootDigit in [r for r in SQAURE_FIRST_DIGITS_STR[d] if r <= f]:
        a = squareNumInRange(n, rootDigit, f)
        if a != False: return a
    
    return False

# lo = 10 ** (math.floor((len(str(n))+1)/2)-1)

if __name__=='__main__':
    # print(isSquareNumber2(4))
    # print(isSquareNumber2(81))
    # print(isSquareNumber2(9))
    # print(isSquareNumber2(24))
    # print(isSquareNumber2(72))

    # inputs = [[n] for n in [0,1,4,9,16,25,36,49,64,81,100,121,144,3034564,2205225,2238016]] + \
    inputs = [[a] for a in range(1,100_000_00) if random.randint(1,1000) == 69]
    # filterLambda = lambda x: x == True
    # inputs = [[n] for n in [0,1,4,9,16,25,36,49,64,81,100,121,144,3034564,2205225,2238016]]
    filterLambda = lambda x: True
    fnList = [isSquareNumber3, isSquareNumber4, isSquareNumber5]
    input_time_dict = compare_speed(fnList, inputs, print_inputs=True, timeUnit="ns", filterByOutputLambda=filterLambda)

    visualize_speed(fnList, input_time_dict)
