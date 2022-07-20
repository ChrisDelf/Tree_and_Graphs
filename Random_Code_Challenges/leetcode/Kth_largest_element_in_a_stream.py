
    def __init__(self, k: int, nums: List[int]):
        #going to use a minHeap to store our values its logn to search
        # creating the minHeap
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        # Want keep poping for elements until we reach the k values
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)


    def add(self, val: int) -> int:
        # adding the to minHeap
        heapq.heappush(self.minHeap, val)
        # only want pop off elements if we are above k
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

