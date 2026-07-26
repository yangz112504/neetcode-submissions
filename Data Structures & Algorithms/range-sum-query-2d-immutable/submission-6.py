class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS = len(matrix)
        COLS = len(matrix[0])
        self.sumMatrix = [[0]*(COLS+1) for c in range(ROWS+1)]
        # we have an extra row and col for 0s when getting the above section
        # whole premise of this is that each square in the 2d matrix is a sum of
        # the whole rectangle from (0,0)
        # so when we want to query a specific sub matrix, we can do that
        # minus left and top + topleft which we subtracted twice
        for r in range(ROWS):
            prefixSum = 0
            for c in range(COLS):
                prefixSum += matrix[r][c]
                above = self.sumMatrix[r][c+1] # square directly above
                # we offset col and rows here bc first row and col are 0's
                self.sumMatrix[r+1][c+1] = prefixSum + above 

    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1 = row1+1
        r2 = row2+1
        c1 = col1+1
        c2 = col2+1
        total = self.sumMatrix[r2][c2]
        top = self.sumMatrix[r1-1][c2]
        left = self.sumMatrix[r2][c1-1]
        topLeft = self.sumMatrix[r1-1][c1-1] # gets both 3 and 5 if you were wodnering
        return total-top-left+topLeft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)