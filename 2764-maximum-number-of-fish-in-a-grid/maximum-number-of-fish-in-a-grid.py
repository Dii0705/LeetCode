class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r,c):
            # Out of bounds:
            if r<0 or c<0 or r>=ROWS or c>=COLS:
                return 0
            if grid[r][c] == 0:
                return 0

            num = grid[r][c]

            # reset to 0 so the algorithm will skip the visited cells
            grid[r][c] = 0

            num += dfs(r, c+1)
            num += dfs(r, c-1)
            num += dfs(r+1, c)
            num += dfs(r-1, c)

            return num 
        
        maxium = 0
        for i in range(ROWS):
            for j in range(COLS):
                num = dfs(i,j)
                if num and num > maxium:
                    maxium = num

        return maxium