class Solution:
    
    def find_subsets_dfs(self, nums: List[int], i: int, subset: List[int]):
        if i >= len(nums):
            return [subset[:]]

        # For the left side, add the remaining elements to the subset list.
        # For the right side, just increment i, and let the inner left handle - duplicates are not considered at all. 
        return self.find_subsets_dfs(nums, i + 1, subset + [nums[i]]) + self.find_subsets_dfs(nums, i + 1, subset)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.find_subsets_dfs(nums, 0, [])
        
