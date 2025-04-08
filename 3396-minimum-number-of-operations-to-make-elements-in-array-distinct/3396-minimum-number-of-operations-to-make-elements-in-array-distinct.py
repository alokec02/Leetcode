class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        last = {}
        res = 0
        
        
        for index, num in enumerate(nums):
                if num in last and last[num] >= 3 * res:
                    res = ceil((last[num] + 1)/ 3)
                last[num] = index
                    
        return res
