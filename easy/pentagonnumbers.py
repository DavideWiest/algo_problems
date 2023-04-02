

pentagonal = lambda x: x*(3*x-1)/2

pentagonalNums = [pentagonal(x) for x in range(1,1000)]

def makePairsDiffs(l: list) -> set:
    combs = {}
    i = 1
    for i, item in enumerate(l):
        if i+1 == len(l): continue
        for item2 in l[i+1:]:
            if abs(item-item2) in pentagonalNums and item+item2 in pentagonalNums:
                combs[(item,item2)] = abs(item-item2)
            
    return combs

result = makePairsDiffs(pentagonalNums)
result = sorted(result, key=lambda x: result[x], reverse=True)
print(result)

print(min(result))