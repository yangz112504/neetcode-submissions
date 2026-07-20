class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        numRows = len(matrix)
        numCols = len(matrix[0])-1
        #how do i perform a binary search on the rows to identify the row
        #i which the target value might fall?
        targetRow = 0
        for i in range(numRows):
            if matrix[i][0] <= target <= matrix[i][numCols]:
                targetRow = i
        
        l = 0
        r = numCols

        while l <= r:
            mid = (l+r)//2
            if target == matrix[targetRow][mid]:
                return True
            if target > matrix[targetRow][mid]:
                l = mid + 1
            if target < matrix[targetRow][mid]:
                r = mid - 1
        return False

            