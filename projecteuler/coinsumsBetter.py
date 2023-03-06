# not mine


def coinCounts(target,value,*rest):
    if not rest: return 0 if target % value else 1    # Only one coin value
    return sum( coinCounts(target-used,*rest)         # Total of ways using
                for used in range(0,target+1,value) ) # varying numbers of the first coin value


answer = coinCounts(200,*[1,2,5,10,20,50,100,200])
print(answer) # 73682




def coinsUsed (target,value,*rest):
    if target % value == 0 :
        yield [f"{target//value} x {value}p"]*(target>0)
    if not rest: return
    for total in range(0,target,value):
        for others in coinsUsed(target-total,*rest):
            yield next(coinsUsed(total,value))+others

for solution in coinsUsed(200,*[1,2,5,10,20,50,100,200]):
    print(*solution,sep=" + ")   