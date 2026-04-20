class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = r = 0
        queue = collections.deque()
        res = []

        while (r < len(nums)):
            while queue and queue[0] < nums[r]:
                queue.popleft()

            queue.append(nums[r])
            if (r - l + 1 >= k):
                l += 1
            r += 1

            if (r - l + 1 == k and queue):
                res.append(queue[0])
                
            print(queue)
    
        return res
            