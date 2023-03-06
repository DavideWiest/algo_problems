import math, sys
from combs import makePairsSums

R = 28123
# R = 30

properDivsOf, posInts = {}, []

for n in range(R):
    div = math.ceil(n / 2)
    properDivsOf[n] = set()

    while div > 0:
        if n % div == 0:
            properDivsOf[n].add(div)
            if n in properDivsOf:
                properDivsOf[n].update(properDivsOf[div])
        div -= 1

abundantNums = [
    n for n in range(R)
    if n < sum(properDivsOf[n])
]

abundantNumsCombsSums = [
    c for c in makePairsSums(abundantNums) if c < R
]

resultList = [
    n 
    for n in range(R)
    if n not in abundantNumsCombsSums
]

print(sum(resultList))

# for n1 in abundantNums:
#     for n2 in abundantNums:
#         if n1+n2 < R:
#             resultList.append(n1+n2)

# print(sum(resultList))