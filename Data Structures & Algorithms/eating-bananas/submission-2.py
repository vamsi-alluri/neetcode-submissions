import math
class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        max_k = max(piles)    # This is how much the max_k could be.

        min_k = 1

        min_k_res = max_k
        while(min_k <= max_k):
            k = (min_k + max_k) // 2
            print(f"l: {min_k}, r: {max_k}, k: {k}, ", end="")

            itr = 0
            current_hr_cnt = 0

            for i in piles:
                current_hr_cnt += (math.ceil(i / k))
            print(f"worked? {current_hr_cnt}")
                
            if (current_hr_cnt <= h):
                min_k_res = min(min_k_res, k)
                max_k = k - 1
            else:
                min_k = k + 1
        return min_k_res





        
        