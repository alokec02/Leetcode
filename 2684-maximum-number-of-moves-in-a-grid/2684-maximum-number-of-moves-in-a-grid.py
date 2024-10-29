class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        dp = [[-1] * C for _ in range(R)]

        for i in range(R):
            dp[i][0] = 0

        for i in range(C):
            for j in range(R):
                if dp[j][i]<0:
                    continue

                if i == C - 1:
                    continue

                for dj in range(-1, 2):
                    if 0 <= j + dj < R and dp[j + dj][i + 1] < dp[j][i] + 1 and grid[j + dj][i + 1] > grid[j][i]:
                        dp[j + dj][i + 1] = dp[j][i] + 1
                    
        best = 0
        for i in range(C):
            for j in range(R):
                best = max(dp[j][i], best)
        return best
