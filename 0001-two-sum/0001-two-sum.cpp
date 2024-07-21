class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        unordered_map<int, int>map;
        vector<int>ans;
        for(int i=0;i<n;i++){
            if(map.find(nums[i])!=map.end()){
                ans.push_back(map[nums[i]]);
                ans.push_back(i);
            }
            else{
                map.insert({target-nums[i], i});
            }
        }
        return ans;
    }
};