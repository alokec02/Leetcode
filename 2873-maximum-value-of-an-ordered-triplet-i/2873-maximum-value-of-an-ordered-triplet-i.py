class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        max_diff = 0 #max(mums[i] - nums[j])
        max_num = 0 # max(nums[i])

        for num in nums:
            res = max(res, max_diff * num)
            max_diff = max(max_diff, max_num - num)
            max_num = max(max_num, num)
        return res