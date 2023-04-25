import random


class StockPrice:

    def __init__(self):
        self.currentTime = -1
        self.currentPrice = 0
        self.maxPriceTime = -1
        self.minPriceTime = -1
        self.timeToPrice = {}

    def update(self, timestamp: int, price: int) -> None:
        if timestamp >= self.currentTime:
            self.currentTime = timestamp
            self.currentPrice = price

        self.timeToPrice[timestamp] = price

        if timestamp == self.maxPriceTime:
            self.maxPriceTime = max(self.timeToPrice, key=self.timeToPrice.get)

        if timestamp == self.minPriceTime:
            self.minPriceTime = min(self.timeToPrice, key=self.timeToPrice.get)

        if self.maxPriceTime == -1 or price > self.timeToPrice[self.maxPriceTime]:
            self.maxPriceTime = timestamp

        if self.minPriceTime == -1 or price < self.timeToPrice[self.minPriceTime]:
            self.minPriceTime = timestamp

    def current(self) -> int:
        return self.currentPrice

    def maximum(self) -> int:
        return self.timeToPrice[self.maxPriceTime]

    def minimum(self) -> int:
        return self.timeToPrice[self.minPriceTime]
    


if __name__ == "__main__":
    sl = StockPrice()

    if False:
        for i in range(10):
            r1, r2 = random.randint(1, 10), random.randint(1, 10)
            print(f"TS: {r1}")
            print(f" P: {r2}")
            sl.update(r1, r2)
            print(f"current: {sl.current()}")
            print(f"min: {sl.minimum()}")
            print(f"max: {sl.maximum()}")
    
    sl.update(1,10)
    sl.update(2,5)
    print(sl.current())
    print(sl.maximum())
    sl.update(1,3)
    print(sl.maximum())
    sl.update(4,2)
    print(sl.minimum())
