class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [0] * (n + 1)
        def rec(k):

            if k < 0:
                return 0
            if cache[k]:
                return cache[k]
            
            if k == 0:
                return 1
            cache[k] = rec(k-1) + rec(k-2)
            return cache[k]
        
        return rec(n)
