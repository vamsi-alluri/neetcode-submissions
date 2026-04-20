from heapq import heapify, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapify(nums)

        prev = None
        duplicateCount = 0
        while len(nums) - k + duplicateCount > k:
            print(nums)
            prev = heappop(nums)
            
        res = heappop(nums)
        print(prev, res)
        if prev == res:
            res = heappop(nums)
        return -res
