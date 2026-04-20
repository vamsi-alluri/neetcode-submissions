class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        n = len(nums) - 1
        while(i < n):
            _sum = nums[i] + nums[n]
            if _sum < target:
                i += 1
            elif (_sum > target):
                n -= 1
            else:
                return [i + 1, n + 1]
        return []