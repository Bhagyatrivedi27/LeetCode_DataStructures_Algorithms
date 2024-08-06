class Solution {
public:
    int longestValidParentheses(string s) {
        
        int n = s.size(), res=0;
        if(n==0)
            return 0;
        int i;
        vector<int>dp(n,0);
        
        dp[0] = 0;
        
        for(i=1;i<n;i++){
            if(s[i]=='(')
                dp[i]=0;
            else{
                if(i-dp[i-1]-1 >= 0 && s[i-dp[i-1]-1]=='('){
                    dp[i] = 2+dp[i-1];
                    
                    if(i-dp[i-1]-2 >= 0)
                        dp[i] += dp[i-dp[i-1]-2];       
                }
            }
            res = max(res,dp[i]);
        }
        return res;
        
    }
};