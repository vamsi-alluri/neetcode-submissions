from heapq import heapify, heappush, heappop

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self._k = k
        heapify(self.heap)

        while len(self.heap) > k:
            heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self._k:
            heappush(self.heap, val)
        elif val > self.heap[0]:
            heappop(self.heap)
            heappush(self.heap, val)
        return self.heap[0]

        
