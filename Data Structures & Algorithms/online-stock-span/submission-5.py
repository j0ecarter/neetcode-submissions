class StockSpanner:

    def __init__(self):
        self.res = []

    def next(self, price: int) -> int:
        self.res.append(price)
        i = len(self.res) - 1
        count = 0
        while i>=0 and self.res[i] <= price:
            i -= 1
            count+=1
        return count
