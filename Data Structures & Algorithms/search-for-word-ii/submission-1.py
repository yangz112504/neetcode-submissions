class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # insert into Trie
        root = TreeNode()
        curr = root
        wordIndex = 0
        for word in words:
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TreeNode()
                curr = curr.children[c]
            curr.word = True
            curr.index = wordIndex
            curr = root
            wordIndex+=1
        # back tracking to find it

        ROWS = len(board)
        COLS = len(board[0])
        res = []
        def dfs(currNode, r, c):
            if r == ROWS or c == COLS or min(r,c) < 0:
                return
            ch = board[r][c]
            if ch == "#" or ch not in currNode.children:
                return
            # character
            currNode = currNode.children[ch]
            if currNode.word:
                res.append(words[currNode.index])
                currNode.word = False
            # not already seen and in children, so continue
            board[r][c] = "#"
            dfs(currNode, r+1,c)
            dfs(currNode, r-1,c)
            dfs(currNode, r,c+1)
            dfs(currNode, r,c-1)
            board[r][c]  = ch
            return

        for r in range(ROWS):
            for c in range(COLS):
                dfs(root, r, c)
        return res
                
class TreeNode():
    def __init__(self):
        self.children = {}
        self.word = False
        self.index = -1

        