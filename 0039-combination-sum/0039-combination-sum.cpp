class Solution {
public:
    void combinationSumHelper(vector<int>& candidates, int i, vector<int>& currSet, vector<vector<int>>& res, int target){
        int n = candidates.size();
        
        //base cases
        if(target<0 or i>=n){
            return;  
        }
        
        if(target==0){
            res.push_back(currSet);
            return;
        }
        
        //exclude
        combinationSumHelper(candidates, i+1, currSet, res, target);
        
        //include
        currSet.push_back(candidates[i]);
        combinationSumHelper(candidates, i, currSet, res, target-candidates[i]);
        currSet.pop_back();
        
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> currSet;
        vector<vector<int>>res;
        
        combinationSumHelper(candidates, 0, currSet, res, target);
        return res;
    }
};