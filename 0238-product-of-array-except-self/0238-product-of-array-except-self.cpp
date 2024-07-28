class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int>Lprod(n);
        vector<int>Rprod(n);

        Lprod[0] =1;
        Rprod[n-1]=1;
        for(int i=1;i<n;i++){
            Lprod[i] = Lprod[i-1]*nums[i-1];
        }
        for(int i=n-2;i>=0;i--){
            Rprod[i] = Rprod[i+1]*nums[i+1];
        }
        vector<int>ans(n);
        for(int i=0;i<n;i++){
            ans[i] = Lprod[i] * Rprod[i];
        }
        return ans;
        
    }
};