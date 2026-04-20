class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        mid = (l + r) // 2

        result = nums[0]
        i = 1
        while (l <= r and i <= 100):
            i += 1

            if nums[l] < nums[r]:
                result = min(result, nums[l])
                break
            

            print("Considered array:", nums[l:r+1])
            mid_idx = (l + r) // 2
            result = min(nums[mid_idx], result)

            print(f'Current min: {result}')
            print(f"l: {l}, r: {r}, mid_idx: {mid_idx}")

            if (nums[l] <= nums[mid_idx]):
                l = mid_idx + 1
            else:
                r = mid_idx - 1
        return result