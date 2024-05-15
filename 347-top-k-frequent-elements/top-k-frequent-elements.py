class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []
        for num, freq in count.items(): # for key, value in count
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap) # pop the root, which will be the k-smallest
            
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        
        return res