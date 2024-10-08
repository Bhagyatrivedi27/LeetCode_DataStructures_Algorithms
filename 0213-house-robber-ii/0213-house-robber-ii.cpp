class Solution {
public:
    int rob(vector<int>& nums) {
        
        int n = nums.size();
        if(n==1)
            return nums[0];
        if(n==0)
            return 0;
        vector<int>dp1(n+1,0);
        vector<int>dp2(n+1, 0);
        
        dp1[n] = 0;
        dp1[n-1] = nums[n-1];
        
        for(int i=n-2;i>0;i--){
            dp1[i] = max(dp1[i+1], nums[i]+dp1[i+2]);
        }
        
        dp2[n] =0;
        dp2[n-1] =0;
        
        for(int i=n-2;i>=0;i--){
            dp2[i] = max(dp2[i+1], nums[i]+dp2[i+2]);
        }
        
        return max(dp1[1], dp2[0]);
    }
};