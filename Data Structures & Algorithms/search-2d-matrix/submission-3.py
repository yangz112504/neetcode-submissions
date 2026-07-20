class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        numRows = len(matrix)-1
        numCols = len(matrix[0])-1
            
        #Finding target row
        l = 0
        r = numRows
        targetRow = 0
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] <= target <= matrix[mid][numCols]:
                targetRow = mid
                break
            if target > matrix[mid][numCols]:
                l = mid + 1
            if target < matrix[mid][0]:
                r = mid -1

        #Finding target column

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

            