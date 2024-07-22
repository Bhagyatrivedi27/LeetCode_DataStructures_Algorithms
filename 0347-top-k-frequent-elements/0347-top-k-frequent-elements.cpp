class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> res;
        int n = nums.size();
        unordered_map<int, int>map;
        
        for(int i=0;i<n;i++){
            map[nums[i]]++;
        }
        
        auto cmp = [](pair<int, int> &p1, pair<int, int> &p2){
            return p1.second < p2.second;
        };
        
        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(cmp)>pq(cmp);
        
        for(const auto & pair : map){
            pq.push(pair);
        }
        
        for(int i=0;i<k;i++){
            res.push_back(pq.top().first);
            pq.pop();
        }
        return res;
    }
};