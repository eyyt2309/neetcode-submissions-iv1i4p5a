class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        if not self.prices:
            self.prices.append(price)
            return 1
        else:
            days = 1
            i = len(self.prices) - 1
            while self.prices[i] <= price and i >= 0:
                days += 1
                i -= 1
            self.prices.append(price)
            return days


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)