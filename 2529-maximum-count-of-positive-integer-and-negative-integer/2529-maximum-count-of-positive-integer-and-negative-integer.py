class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        idx_neg = bisect.bisect_left(nums, 0)
        idx_pos = bisect.bisect_right(nums, 0)
        return max(idx_neg, n - idx_pos)