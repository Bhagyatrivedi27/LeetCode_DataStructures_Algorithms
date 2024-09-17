class Solution {
public:
    void combinationSumHelper(vector<int> &candidates, int target, int i, vector<int> &currSet, vector<vector<int>> &res){
        
        int n = candidates.size();
        
        //base cases
        
        if(target == 0 and i <=n){
            res.push_back(currSet);
            return;
        }
        if(i>=n or target<0){
            return;
        }
        
        
        //exclude 
        combinationSumHelper(candidates, target, i+1, currSet, res);
        
        //include
        currSet.push_back(candidates[i]);
        combinationSumHelper(candidates, target-candidates[i], i, currSet, res);
        currSet.pop_back();
        
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        
        int n = candidates.size();
        
        vector<int>currSet;
        vector<vector<int>>res;
        
        combinationSumHelper(candidates, target, 0, currSet, res);
        return res;
        
    }
};