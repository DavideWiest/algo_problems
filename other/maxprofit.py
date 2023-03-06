
prices = [7,1,5,3,6,4]
comprices = [*prices]
maxprof = 0
maxprofindex = []

for price in prices:

    for comprice in comprices:
        if comprice - price > maxprof or maxprof == 0:
            maxprof = comprice - price
            maxprofindex = [prices.index(price), prices.index(comprice)]
    comprices.remove(price)

print(maxprof)
print(f"Buy on day {maxprofindex[0]+1} at {prices[maxprofindex[0]]} and sell on day {maxprofindex[1]+1} at {prices[maxprofindex[1]]}")