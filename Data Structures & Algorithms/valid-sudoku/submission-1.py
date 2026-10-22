from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # list of set for row
        rowSets = [set() for _ in range(9)]
        # list of set for cols
        colSets = [set() for _ in range(9)]

        # checking boxes
        # hashTable for boxes because use r // 3 and c // 3 and increment all the way up the boxes from top left, top middle, top right, and so forth follow a pattern. All boxes in top left are going to be indexed to (0,0) | top middle to (0,1) | top right to (0,2)....
        boxTable = defaultdict(set)
        # checking rows and cols
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num == ".":
                    continue
                # check rows
                if num not in rowSets[row]:
                    rowSets[row].add(num)
                else:
                    return False
                # check cols
                if num not in colSets[col]:
                    colSets[col].add(num)
                else:
                    return False
                
                # check boxes
                boxIndex = (row//3,col//3)
                if num not in boxTable[boxIndex]:
                    boxTable[boxIndex].add(num)
                else:
                    return False
        return True
                

      