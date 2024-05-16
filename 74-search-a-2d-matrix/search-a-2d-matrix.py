class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        l, r = 0, m*n - 1

        while l <= r:
            m = (l+r)//2
            midVal = matrix[m//n][m % n]
            # row = i//n
            # col = i%n

            if midVal == target:
                return True
            if midVal < target:
                l = m + 1
            else:
                r = m - 1
        return False