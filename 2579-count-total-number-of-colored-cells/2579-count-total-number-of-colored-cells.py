class Solution:
    def coloredCells(self, n: int) -> int:
        output = 1
        for i in range(1, n):
            output += 4*i
        return output