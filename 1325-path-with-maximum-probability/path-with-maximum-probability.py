class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        from heapq import heappop, heappush

        adj = defaultdict(list)

        for i in range(len(edges)):
            src, dst = edges[i]
            adj[src].append((dst, succProb[i]))
            adj[dst].append((src, succProb[i]))
        
        min_heap = [(-1, start_node)]
        visited = set()

        while min_heap:
            prob, node = heappop(min_heap)
            visited.add(node)

            if node == end_node:
                return -prob

            for neighbor, edge_prob in adj[node]:
                if neighbor not in visited:
                    heappush(min_heap, (prob * edge_prob, neighbor))
        return 0
