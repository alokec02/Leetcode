class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = 0
        expected = sorted(heights)
        for i in range(0, len(heights)):
            if expected[i]!=heights[i]:
                res += 1
        return res    