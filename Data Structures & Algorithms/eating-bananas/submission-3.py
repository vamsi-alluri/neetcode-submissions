import math
class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        max_k = max(piles)    # This is how much the max_k could be.
        min_k = 1
        res = 0

        while(min_k <= max_k):
            k = (min_k + max_k) // 2
            print(f"l: {min_k}, r: {max_k}, k: {k}, ", end="")

            current_hr_cnt = 0

            for i in piles:
                current_hr_cnt += (math.ceil(i / k))
                if (current_hr_cnt > h):
                    break
            print(f"worked? {current_hr_cnt}")
                
            if (current_hr_cnt <= h):
                res = k
                max_k = k - 1
            else:
                min_k = k + 1
        return res
        