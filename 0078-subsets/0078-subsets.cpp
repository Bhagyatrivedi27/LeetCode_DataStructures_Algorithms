class Solution {
public:
    void subsetsHelper(vector<int> &nums, int i, vector<int> &curr, vector<vector<int>> & res){
        int n = nums.size();
        
        // base cases
        if(i>=n){
            res.push_back(curr);
            return;
        }
        
        //decisions 
        
        //1. Excluding 
        subsetsHelper(nums, i+1, curr, res);
        
        //2. Including 
        curr.push_back(nums[i]);
        subsetsHelper(nums, i+1, curr, res);
        curr.pop_back();
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        int n = nums.size();
        
        vector<int> curr;
        vector<vector<int>>res;
        
        subsetsHelper(nums, 0, curr, res);
        return res;
    }
};