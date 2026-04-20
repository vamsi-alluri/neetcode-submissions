class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        i = 1
        while (l <= r and i <= 100):
            i += 1
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid

            if (nums[l] <= target < nums[mid]): # left side is sorted 
                if (nums[l] <=  nums[mid]):
                    l = mid - 1
                else:
                    r = mid + 1
            else:
                if (nums[l] <=  nums[mid]):
                    l = mid + 1
                else:
                    r = mid - 1
        return -1