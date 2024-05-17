class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # maxHeap to pop two heaviest stones, get the difference
        # insert the difference back into the heap

        stones = [ -s for s in stones] # trick for maxHeap implementation in Python
        heapq.heapify(stones)

        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)

            if s1 != s2:
                heapq.heappush(stones, -abs(s1-s2)) # since it's a maxHeap, we negate the val
        
        stones.append(0)
        return -stones[0]

