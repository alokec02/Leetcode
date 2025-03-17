class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = defaultdict(int)
        for num in nums:    
            count[num] += 1
        
        for num in nums:
            if count[num] % 2 == 0:
                continue
            else: 
                return False
        return True