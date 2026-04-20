from heapq import heappush, heappop
import math

class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        minHeap = []
        for point in points:
            eucDist = math.sqrt((point[0])**2 + (point[1])**2)
            print(f"Euclidean distance for {point[0]}, {point[1]}: {eucDist}")
            heappush(minHeap, (eucDist, point))
        

        res = []

        while k:
            res.append(heappop(minHeap)[1])
            k -= 1
        return res
