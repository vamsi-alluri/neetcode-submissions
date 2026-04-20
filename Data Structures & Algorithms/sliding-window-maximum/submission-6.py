class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = r = 0
        queue = collections.deque()
        res = []

        while (r < len(nums)):
            while queue and (queue[0] < nums[r] or (len(queue) > k - 1)):
                queue.popleft()

            while queue and (queue[-1] < nums[r]):
                queue.pop()
            
            queue.append(nums[r])

            print(l, r)
            if (r - l + 1 == k and queue and (len(queue) < k + 1)):
                res.append(queue[0])

            if (r - l + 1 >= k):
                l += 1
            r += 1

                
            print(queue)
    
        return res
            