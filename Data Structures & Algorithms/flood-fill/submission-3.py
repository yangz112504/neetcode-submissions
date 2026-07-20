class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        ROWS = len(image)
        COLS = len(image[0])
        visited = set()

        def helper(r,c, visited, startingColor):
            if min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visited or image[r][c] != startingColor:
                return #first 3 make sure that it's in bounds and last checks that it's stargingColor
            image[r][c] = color
            visited.add((r,c))
            helper(r+1,c,visited,startingColor)
            helper(r-1,c,visited,startingColor)
            helper(r,c+1,visited,startingColor)
            helper(r,c-1,visited,startingColor)
            # no need to backtrack because we want them to remain visited
            return

        
        helper(sr,sc, visited,image[sr][sc])
        return image



        