class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = []
        neg = []
        for n in nums:
            if n < 0:
                neg.append(n)
            if n > 0:
                pos.append(n)
        return max(len(pos), len(neg))  