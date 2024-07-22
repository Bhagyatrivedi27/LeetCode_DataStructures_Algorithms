class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if(n==1)
            return nums[0];
        vector<int>dp1(n+1, 0);
        vector<int>dp2(n+1, 0);

        //rob last house 
        dp1[n]=0;
        dp1[n-1]=nums[n-1];

        //dont rob last house
        dp2[n] = 0;
        dp2[n-1] = 0;

        for(int i=n-2;i>0;i--){
            dp1[i] = max(dp1[i+1], dp1[i+2]+nums[i]);
        }
        for(int i=n-2;i>=0;i--){
            
            dp2[i] = max(dp2[i+1], dp2[i+2]+nums[i]);
        }

        return max(dp1[1], dp2[0]);
    }
};