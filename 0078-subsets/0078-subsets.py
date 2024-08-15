class Solution:
    def subsetsHelper(self, nums, i, currSet, res):
        n = len(nums)
        
        if i >= n:
            res.append(currSet[:])
            return
        
        self.subsetsHelper(nums, i+1, currSet, res)
        
        currSet.append(nums[i])
        self.subsetsHelper(nums, i+1, currSet, res)
        currSet.pop()
            
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        currSet = []
        self.subsetsHelper(nums, 0, currSet, res)
        return res