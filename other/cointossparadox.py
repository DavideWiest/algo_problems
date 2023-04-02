# https://en.wikipedia.org/wiki/St._Petersburg_paradox

import random, math
from matplotlib import pyplot as plt


boundsMemo = [0.5]

def getByNearestLowerBound(x):
    i = 0
    while x > boundsMemo[i]:
        i += 1
    return i

def populateMemoForRandInt(n):
    while n > boundsMemo[-1]:
        boundsMemo.append((boundsMemo[-1]+1)/2)

def getK():
    randInt = random.random()
    if randInt > boundsMemo[-1]:
        populateMemoForRandInt(randInt)
    return getByNearestLowerBound(randInt)


def getBreakEvenPrice(sampleSize, printEvery=0, returnHistoricalPrice=False, printProgress=False):
    if printEvery == 0:
        return sum(
            2 ** (getK()+1) for i in range(sampleSize)
        ) / sampleSize
    else:
        if returnHistoricalPrice:
            histPrice = {}

        priceUntilNow = 0
        iters = math.ceil(sampleSize/printEvery)

        for i in range(iters):
            currentSampleAvg = sum(2 ** (getK()+1) for i in range(printEvery)) / printEvery
            priceUntilNow = priceUntilNow + (currentSampleAvg - priceUntilNow) / (i+1)

            print(f"[{i+1}/{iters}]", priceUntilNow)

            if returnHistoricalPrice:
                histPrice[(i+1)*printEvery] = priceUntilNow

        if returnHistoricalPrice:
            return histPrice

if __name__ == '__main__':
    # print(getBreakEvenPrice(20000000, 10000))

    histPrice = getBreakEvenPrice(200000000, 2000, True, True)

    plt.plot(histPrice.keys(), histPrice.values())
    plt.show()