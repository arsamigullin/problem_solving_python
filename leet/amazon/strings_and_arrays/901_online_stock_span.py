# monotonous stack
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span_days = 1
        while (self.stack and self.stack[-1][0] <= price):
            span_days += self.stack.pop()[1]
        self.stack.append((price, span_days))
        return span_days



class StockSpanner:

    def __init__(self):
        self.arr = []

    def next(self, price: int) -> int:
        if not self.arr:
            self.arr.append((price,1,-1))
            return 1
        else:
            lastprice, count, parent = self.arr[-1]
            if price < lastprice:
                self.arr.append((price,1,len(self.arr)-1))
                return 1
            else:
                cnt = 1 + count
                while parent!=-1 and self.arr[parent][0] <= price:
                    cnt += self.arr[parent][1]
                    parent = self.arr[parent][2]
                self.arr.append((price, cnt, parent))
                return cnt
