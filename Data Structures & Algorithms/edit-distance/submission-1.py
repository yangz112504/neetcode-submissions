class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        ROWS = len(word1)
        COLS = len(word2)
        if ROWS == 0:
            return COLS
        if COLS == 0:
            return ROWS

        cache = [[-1] * COLS for _ in range (ROWS)] # stores min num of operations to get to a subsequence

        # Ex: Monkey and Money
        # When deleting, index1 goes forward but index 2 stays same
        # this mimics just moving the index ahead as if that char isn't part of the word anymore
        # when inserting, index1 stays the same but index 2 goes forward
        # this mimics just moving adding padding to current position so the curr position can be checked with word2's next position
        # when replacing they both go forward
        def dfs(index1,index2,word1,word2):
            if index1 == len(word1):
                return len(word2) - index2 # how many you need to add
            if index2 == len(word2):
                return len(word1) - index1 # how many you need to delete
            
            if cache[index1][index2] != -1:
                return cache[index1][index2]
            
            if word1[index1] != word2[index2]:
                # delete, add, replace
                cache[index1][index2] = 1+ min(dfs(index1+1,index2,word1,word2), dfs(index1,index2+1,word1,word2), dfs(index1+1,index2+1,word1,word2))
            else:
                cache[index1][index2] = dfs(index1+1,index2+1,word1,word2)

            return cache[index1][index2]
        
        return dfs(0,0,word1,word2)
            

            

            
            
            
        