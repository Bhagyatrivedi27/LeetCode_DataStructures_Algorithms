#define MOD 1000000007
class Solution {
public:
    int countOrders(int n) {
        vector<long long int> dp(n+1, 0);
        
        dp[1] = 1;
        long long int temp;
        for(long long int i=2;i<=n;i++){
            temp = i * (2*i-1);
            dp[i] = ((dp[i-1] %MOD) * (temp%MOD)%MOD);
            
        }
        return dp[n];
    }
};