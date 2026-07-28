class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # we're going to define it so that every square represents a subsquare starting from 0,0 to i,j
        # that way, if we want an area, we can do total square - left - right + top
        ROWS = len(matrix)
        COLS = len(matrix[0])
        self.matrix = [[0]*(COLS+1) for r in range(ROWS+1)] #extra column and row of 0's for padding because we need to get above nd this will solve our null pointer problem
        for r in range(1,ROWS+1):
            prefixSum = 0
            for c in range(1, COLS+1):
                prefixSum+=matrix[r-1][c-1]
                above = self.matrix[r-1][c]
                self.matrix[r][c] = prefixSum + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1+=1
        col1+=1
        row2+=1
        col2+=1
        total = self.matrix[row2][col2]
        left = self.matrix[row2][col1-1]
        top = self.matrix[row1-1][col2]
        upperLeft = self.matrix[row1-1][col1-1]
        return total-left-top+upperLeft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)