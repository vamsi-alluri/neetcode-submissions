class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h >= len(piles): 
            return max(piles)
        return 2
        