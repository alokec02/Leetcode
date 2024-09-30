class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = [0] * maxSize
        self.inc = [0] * maxSize
        self.top = -1    

    def push(self, x: int) -> None:
        if self.top < len(self.stack) - 1:
            self.top += 1
            self.stack[self.top] = x

    def pop(self) -> int:
        if self.top < 0:
            return -1
        res = self.stack[self.top] + self.inc[self.top]

        if self.top > 0:
            self.inc[self.top - 1] += self.inc[self.top]
        self.inc[self.top] = 0
        self.top -= 1
        return res

    def increment(self, k: int, val: int) -> None:
        if self.top >= 0:
            index = min(self.top, k - 1)

            self.inc[index] += val

            


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)