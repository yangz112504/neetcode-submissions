class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # so i have a target that i should check the value against the m rows and the binary search the n columns
        numRows = len(matrix)
        numCols = len(matrix[0])

        targetRow = 0

        # #ORR we could do binary search
        l = 0
        r = numRows - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[m][0] <= target <= matrix[m][numCols-1]:
                targetRow = m
                break
            elif target > matrix[m][numCols-1]:
                l = m + 1
            else:
                r = m - 1

        # perform binary search to find
        l = 0
        r = numCols-1
        while l <= r:
            m = (l + r) // 2
            if target == matrix[targetRow][m]:
                return True
            elif target > matrix[targetRow][m]:
                l = m + 1
            else:
                r = m - 1
        return False