from heapq import heapify, heappush

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self._k = k
        self.len_heap = len(self.heap)
        heapify(self.heap)

    def add(self, val: int) -> int:
        print("Before pushing:", self.heap)
        heappush(self.heap, val)
        self.len_heap += 1
        print("After pushing:", self.heap)

        return self.heap[self.len_heap - self._k]

        
