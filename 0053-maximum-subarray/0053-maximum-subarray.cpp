class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        
        int n = nums.size();
        vector<int>dp(n+1, 0);
        dp[0] = nums[0];
        int maxSum=dp[0];
        for(int i=1;i<n;i++){
            dp[i] = max(nums[i], nums[i]+dp[i-1]);
            maxSum = max(maxSum, dp[i]);
        }
        
        return maxSum;
    }
};