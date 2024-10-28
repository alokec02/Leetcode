class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        s = set(nums)
        res = -1
        for n in nums:
            if n ** (1 / 2) not in s:
                ans = 1
                while n * n in s:
                    ans += 1
                    n = n * n
                res = max(res, ans)
        return res if res > 1 else -1   