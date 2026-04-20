import heapq
from collections import deque
class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freqMap = [0] * 26
        for task in tasks:
            freqMap[ord(task) - ord('A')] += 1

        heap = []
        for k, v in enumerate(freqMap):
            if v:
                heapq.heappush(heap, (-1 * v))

        currentTime = 0
        queue = deque()
        while heap or queue:
            currentTime += 1
            if heap:
                freq = heapq.heappop(heap) + 1
                if freq < 0: queue.append((freq, currentTime + n))
            
            # When queue's elements are ready, push it to heap
            if queue and queue[0][1] == currentTime:
                heapq.heappush(heap, queue.popleft()[0])

        return currentTime


