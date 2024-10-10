class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        max_right = [0] * len(nums)
        i = len(nums) - 1
        prev_max = 0

        for n in reversed(nums):
            max_right[i] = max(n, prev_max)
            prev_max = max_right[i]
            i -= 1

        res = 0
        l = 0
        for r in range(len(nums)):
            if nums[l] <= max_right[r]:
                res = max(res, r - l)
            else:
                l += 1
        
        return res