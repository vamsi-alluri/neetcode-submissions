class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = [0] * (n + 1)
        test = 0
        def rec(k):
            nonlocal test
            test += 1

            if k < 0:
                return 0
            if cache[k]:
                return cache[k]
            
            if k == 0:
                return 1
            cache[k] = rec(k-1) + rec(k-2)
            return cache[k]
        temp = rec(n)
        print(test)
        
        return temp
