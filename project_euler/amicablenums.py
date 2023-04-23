from combs import makeSortedPairs
import math
from more_itertools import locate

def find_indices(list_to_check, item_to_find):
    indices = locate(list_to_check, lambda x: x == item_to_find)
    return list(indices)

LIMIT = 10000

divs = {}

def d(n):
    div = math.ceil(n / 2)
    divs[n] = set()

    while div > 0:
        if n % div == 0:
            divs[n].add(div)
            if n in divs:
                divs[n].update(divs[div])
        div -= 1

    return divs[n]

if __name__ == "__main__":
    properDivisorSums = {}

    for n in range(LIMIT):
        properDivisorSums[n] = sum(d(n))
    
    print(list(properDivisorSums.items())[:50])

    properDivisorSumsValues2 = list(properDivisorSums.values())
    properDivisorSumsList = list(properDivisorSums.keys())


    amicables = set()

    for n in range(LIMIT):
        # d(y) exists
        for index in find_indices(properDivisorSumsValues2, n):
            value = index
            if properDivisorSums[n] == value and value != n:
                print(f"{n} & {value}")
                print(f"{sum(d(n))} - {sum(d(value))}")
                amicables.add(n)

    print(sum(amicables))
