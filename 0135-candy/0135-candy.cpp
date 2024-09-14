class Solution {
public:
    int candy(vector<int>& ratings) {
        int n = ratings.size();
        if(n == 0) return 0;
        
        // Initialize candies for each child to 1
        vector<int> candies(n, 1);
        
        // Left to Right pass
        for(int i = 1; i < n; ++i){
            if(ratings[i] > ratings[i-1]){
                candies[i] = candies[i-1] + 1;
            }
        }
        
        // Right to Left pass
        for(int i = n-2; i >=0; --i){
            if(ratings[i] > ratings[i+1]){
                candies[i] = max(candies[i], candies[i+1] + 1);
            }
        }
        
        // Calculate the total candies
        int total = 0;
        for(auto c : candies){
            total += c;
        }
        
        return total;
    }
};