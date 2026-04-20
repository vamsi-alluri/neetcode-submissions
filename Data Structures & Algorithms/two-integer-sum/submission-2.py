class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        while(i < j):
            print(i, j)
            _sum = nums[i] + nums[j]
            if _sum < target:
                i += 1
            elif (_sum > target):
                j -= 1
            else:
                return [i, j]
        return []