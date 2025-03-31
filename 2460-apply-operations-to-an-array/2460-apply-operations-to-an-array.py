class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
        
        output1, output2 = [], []
        for j in range(0, len(nums)):
            if nums[j]!=0:
                output1.append(nums[j])
            if nums[j]==0:
                output2.append(nums[j])
        return output1 + output2