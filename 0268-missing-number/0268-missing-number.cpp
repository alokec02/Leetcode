class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int currentSum = 0;
        for (int i = 0; i < n; i++) {
            currentSum += nums[i];
        }
        int intendedSum = 0;
        for (int i = 0; i <= n; i++) {
            intendedSum += i;
        }
        return intendedSum - currentSum;
    }
};