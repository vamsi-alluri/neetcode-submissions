class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = [0] * (n + 1)
        def rec(k):
            if cache[k]:
                return cache[k]
            
            if k <= 0:
                return 1
            
            return min(rec(k-1), rec(k-2)) + 1
        return rec(n)

            