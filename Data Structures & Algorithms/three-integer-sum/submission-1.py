class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        n = len(numbers) - 1
        while(i < n):
            _sum = numbers[i] + numbers[n]
            if _sum < target:
                i += 1
            elif (_sum > target):
                n -= 1
            else:
                return [numbers[i], numbers[n]]
        return []

    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)  # n * log n
        
        _res = []
        for i in range(len(nums)): # n
            res = self.twoSum(nums[i+1:], -nums[i]) # n
            if (res != []):
                res.append(nums[i])
                _res.append(res)
            
        return list(set(_res))

        