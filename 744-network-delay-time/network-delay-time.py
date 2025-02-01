class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra's Algorithm
        # You can't use negative weight if there is a cycle (there is)
        adj = collections.defaultdict(list)

        for i in range(len(times)):
            src, dst, w = times[i]
            adj[src].append((dst,w))
        
        start = k
        min_heap = [(0, start)]
        shortest = {}

        while min_heap:
            w, node = heapq.heappop(min_heap)
            if node in shortest:
                continue
            shortest[node] = w
            
            for neighbor, weight in adj[node]:
                if neighbor not in shortest:
                    heapq.heappush(min_heap, (weight + w, neighbor))
        
        if len(shortest) != n:
            return -1
        
        return max(shortest.values())
