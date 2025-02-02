class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        # Count how many servers in each row and column
        row_counts = [0] * rows
        col_counts = [0] * cols
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    row_counts[r] += 1
                    col_counts[c] += 1
        
        # Now count how many servers can communicate
        result = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # This server communicates if row_counts[r] > 1 or col_counts[c] > 1
                    if row_counts[r] > 1 or col_counts[c] > 1:
                        result += 1
                        
        return result


            
