class Solution {
public:
    int longestArithSeqLength(vector<int>& A) {
        int n =A.size(),res=1;
        
        vector<unordered_map<int,int>>dp(n);
        int cd;
        //smallest problem
        for(int i=1;i<n;i++){
            //Compute LAS ending at i
            //iterate through all its predecessors
            for(int j=0;j<i;j++){
                cd = A[i]-A[j];
                
                //you dont get any sequence ending at j with that cd
                if(dp[j].find(cd)==dp[j].end()){
                    dp[i][cd] = max(dp[i][cd],2);
                }
                else{
                    dp[i][cd] = max(dp[i][cd],dp[j][cd]+1);
                }
                
                res = max(res,dp[i][cd]);
            }
        }
        return res;
    }
};