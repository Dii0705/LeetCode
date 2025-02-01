class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict) # default methods for matrix

        # initialize
        for (u,v), val in zip(equations, values):
            graph[u][u] = 1 # 0 for regular Floyd-Warshall application
            graph[u][v] = val # repeating squaring
            graph[v][u] = 1/ val
        
        for k in graph:
            for i in graph[k]:
                for j in graph[k]:
                    graph[i][j] = graph[i][k] * graph[k][j] if i != j else 1
        
        answers = []
        for u,v in queries:
            answers.append(graph[u].get(v, -1)) # find val in graph[u][v], else return -1
        
        return answers