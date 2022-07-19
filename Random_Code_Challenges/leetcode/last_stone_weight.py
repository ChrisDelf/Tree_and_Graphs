def lastStoneWeight(self, stones: List[int]) -> int:
   # going to use a minHeap since python does not have a maxHeap
   stones = [-s for s in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        first = heapq.heappop(stones)
        second = heapq.heappop(stones)
        
        # since we are working with minHeap we have all negative 
        # values 
        if second > first:
            heapq.heappush(stones, first - second)
    ## this handles a none case
    stones.append(0)
    return abs(stones[0])
            
