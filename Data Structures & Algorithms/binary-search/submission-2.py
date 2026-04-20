class Solution:

    def search(self, nums: List[int], target: int) -> int:

        r = len(nums) - 1
        l = 0

        print([x for x in range(len(nums))])

        while (l <= r):
            print(f"l: {l}, r: {r}")
            print("Considered array:", nums[l:r])
            mid_idx = (l + r) // 2
            print(f"target: {target} <=> nums[{mid_idx}]: {nums[mid_idx]}")

            if (target < nums[mid_idx]):
                r = mid_idx - 1
            elif(target > nums[mid_idx]):
                l = mid_idx + 1
            else:
                return mid_idx 
        return -1