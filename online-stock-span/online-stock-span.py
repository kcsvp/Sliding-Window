class StockSpanner:

    def __init__(self):
        self.stack = []
        self.base = []
        

    def next(self, price: int) -> int:
        if self.stack == []:
            if price == []:
                return []
            self.stack.append(price)
            self.base.append(1)
            return 1
        elif price < self.stack[-1]:
            self.stack.append(price)
            self.base.append(1)
            return 1
        else:
            count = 1
            while self.stack != [] and price >= self.stack[-1]:
                self.stack.pop()
                count += self.base[-1]
                self.base.pop()
                
            self.stack.append(price)
            self.base.append(count)
            return count



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)