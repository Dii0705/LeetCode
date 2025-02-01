class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # Floyd-Warshall Algorithm

        # create a matrix of 26 lists each list contains 26 elements
        graph = [[float('inf')] * 26 for _ in range(26)]
        for i in range(26):
            graph[i][i] = 0

        for old, new, c in zip(original,changed,cost):
            # convert character to ord 
            u, v = ord(old) - ord('a'), ord(new) - ord('a')
            graph[u][v] = min(graph[u][v], c)

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
        cost = 0
        for s, t in zip(source, target):
            src, dst = ord(s) - ord('a'), ord(t) - ord('a')
            cost += graph[src][dst]
        return cost if cost != float('inf') else -1

        return cost