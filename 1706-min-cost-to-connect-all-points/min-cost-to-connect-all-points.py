class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        # create the adjacency list
        adj = {i:[] for i in range(N)} # list of [cost, node]
        
        for i in range(N):
            x1,y1 = points[i]
            for j in range(i+1, N):
                # for each point i, calculate the distance to all other points
                x2, y2 = points[j]
                dist = abs(x1-x2)+abs(y1-y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        # Prim's algorithm
        ans = 0
        visited = set()
        minHeap = [[0,0]]
        while minHeap:
            cost, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            ans += cost
            for nextCost, nextNode in adj[node]:
                if nextNode not in visited:
                    heapq.heappush(minHeap, [nextCost, nextNode])
        return ans