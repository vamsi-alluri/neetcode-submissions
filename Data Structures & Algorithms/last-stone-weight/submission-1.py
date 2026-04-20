from heapq import heapify, heappop, heappush
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-s for s in stones]
        heapify(stones)

        while len(stones) > 1:
        
            x = -heappop(stones)
            y = -heappop(stones)

            print("x and y", x, y)

            if x == y:
                continue
            elif x < y:
                y -= x
                heappush(stones, -y)
            else:
                x -= y
                heappush(stones, -x)
        return -stones[0] if stones else 0


