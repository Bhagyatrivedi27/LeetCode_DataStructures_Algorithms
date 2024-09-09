class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        int n = s.size();
        int i, j;
        string t;
        
        unordered_set<string> dict;
        for(i=0;i<wordDict.size();i++){
            dict.insert(wordDict[i]);
        }
        
        vector<bool> dp(n+1, false);
        
        //Smallest Subproblem
        dp[n] = true;
        
        for(i=n-1;i>=0;i--){
            t = "";
            for(j=i;j<n;j++){
                t+= s[j];
                
                if(dict.find(t)==dict.end())
                    continue;
                
                if(dp[j+1])
                    dp[i] = true;
            }
        }
        return dp[0];
    }
};