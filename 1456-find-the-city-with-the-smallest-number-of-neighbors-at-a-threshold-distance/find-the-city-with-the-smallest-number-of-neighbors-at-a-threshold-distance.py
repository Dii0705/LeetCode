class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Dijkstra's Algorithm 
        def dijkstra(start):
            adj = collections.defaultdict(list)

            for src, dst, w in edges:  
                adj[src].append((dst, w))
                adj[dst].append((src, w))

            min_heap = [(0,start)]
            shortest = {}

            while min_heap:
                w, node = heapq.heappop(min_heap)
                if node in shortest:
                    continue
                shortest[node] = w
                for neighbor, weight in adj[node]:
                    if neighbor not in shortest:
                        heapq.heappush(min_heap, (w + weight, neighbor))
            return shortest
        
        minReachableCities = float('inf')
        city = -1 # can't set as 0, since n starts from 0
        for i in range(n):
            distance = dijkstra(i)
            reachableCities = sum(1 for d in distance.values() if d <= distanceThreshold)

            if reachableCities <= minReachableCities:
                minReachableCities = reachableCities
                city = i

        return city