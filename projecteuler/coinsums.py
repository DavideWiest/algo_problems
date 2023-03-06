from combs import numericCombsToTarget

def skip():
    AVAILABLE_COINS = [
        1,2,5,10,20,50,100,200
    ]

    TARGET = 200

    # AVAILABLE_COINS = [1,2,5]
    # TARGET = 10

    # combs = numericCombsToTarget(AVAILABLE_COINS, TARGET)

    def numericCombsNumToTarget2(availableNums: list, target: int, memo={}):
        if target <= 0:
            return [[0]], memo
        
        combs = []
        for num in availableNums:
            if num <= target:
                if target-num not in memo:
                    memo[target-num], memo = numericCombsNumToTarget2(availableNums, target-num, memo)
                combs += [[num] + subCombs for subCombs in memo[target-num]]

        return combs, memo

    def numericCombsNumToTarget2(availableNums: list, target: int, memo={}):
        combs = []
        if target <= 0:
            combs.append([0])
        else:
            for num in availableNums:
                if num <= target:
                    if target-num not in memo:
                        _, memo = numericCombsNumToTarget2(availableNums, target-num, memo)
                    combs += [[num] + subCombs for subCombs in memo[target-num]]

        memo[target] = combs

        return combs, memo

    def numericCombsNumToTarget3(availableNums: list, target: int, memo={}):
        if target <= 0: return 1, memo
        
        numCombs = 0
        for num in availableNums:
            for subNum in range(0,target+1,num):
                if num <= target:
                    if num not in memo:
                        memo[subNum], memo = numericCombsNumToTarget3(availableNums, target-subNum, memo)
                    
                    numCombs += memo[subNum]

        memo[target] = numCombs

        return numCombs, memo



def coinVariations(target, value, *rest):
    if not rest: return 0 if target % value else 1
    return sum(coinVariations(target-used, *rest)
        for used in range(0, target+1, value))


# AVAILABLE_COINS = sorted(AVAILABLE_COINS)
# combs = coinVariations(TARGET, *AVAILABLE_COINS)

# # print(memo)
# print(combs)

answer = coinVariations(200,*[1,2,5,10,20,50,100,200])
print(answer) # 73682