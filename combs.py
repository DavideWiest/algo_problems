



def makePairs(l: list) -> set:
    combs = set()
    for i, item in enumerate(l):
        combs.update({
            (item, item2) for item2 in l[i:]
        })
    return combs

def makeSortedPairs(l: list) -> set:
    combs = set()
    for i, item in enumerate(l):
        combs.update({
            (item if item <= item2 else item2, 
            item2 if item2 >= item else item) for item2 in l[i:]
        })
    return combs

def makePairsSums(l: list) -> set:
    combs = set()
    for i, item in enumerate(l):
        combs.update({
            item+item2 for item2 in l[i:]
        })
    return combs

def numericCombsToTarget(availableNums: list, target: int):
    if target <= 0:
        return []
    combs = []
    for num in availableNums:
        if num <= target:
            c2 = numericCombsToTarget(availableNums, target-num)
            combs += [[num] + subCombs for subCombs in c2]
    
    return combs

if __name__ == '__main__':
    a = [1,2,34,5,6]
    print(makePairs(a))
    print(makeSortedPairs(a))