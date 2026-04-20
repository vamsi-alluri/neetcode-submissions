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
                return [i + 1, n + 1]
        return []

            
