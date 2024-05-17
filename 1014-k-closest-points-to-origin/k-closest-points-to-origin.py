class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # based on distance to origin on a x-y plane, return k closest 
        # use heap to store the distance and then pop k elements
        
        # distance
        minHeap = []
        for x, y in points:
            dis = x ** 2 + y ** 2
            heapq.heappush(minHeap, (dis,x,y))

        res = []
        for _ in range(k):
            _,x,y = heapq.heappop(minHeap)
            res.append((x,y))
        return res