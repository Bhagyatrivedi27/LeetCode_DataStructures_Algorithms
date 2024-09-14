class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int n = candies.size();
        int maxEle = -1;
        for(int i=0;i<n;i++){
            maxEle = max(maxEle, candies[i]);
        }
        vector<bool>res(n);
        for(int i=0;i<n;i++){
            res[i] = ((candies[i]+extraCandies) >= maxEle) ? true  : false;
        }
        return res;
    }
};