class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        def helper(r,c, cache={}):
            if r >= rows or c >= cols:
                return 0
            if obstacleGrid[r][c] == 1:
                return 0
            if r == rows-1 and c == cols-1:
                return 1
            
            
            if (r,c) in cache: 
                return cache[(r,c)]
            
            cache[(r,c)] = helper(r+1, c, cache) + helper(r, c+1, cache)
            
            return cache[(r,c)]
        
        return helper(0,0)
