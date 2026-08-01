class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # insert into Trie
        root = TreeNode()
        wordIndex = 0
        for word in words:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TreeNode()
                curr = curr.children[c]
            curr.word = word
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
            newNode = currNode.children[ch]
            if newNode.word:
                res.append(newNode.word)
                newNode.word = None
            # not already seen and in children, so continue
            board[r][c] = "#"
            dfs(newNode, r+1,c)
            dfs(newNode, r-1,c)
            dfs(newNode, r,c+1)
            dfs(newNode, r,c-1)
            board[r][c]  = ch

            if not newNode.children and newNode.word is None:
                del currNode.children[ch]

            return

        for r in range(ROWS):
            for c in range(COLS):
                dfs(root, r, c)
        return res
                
class TreeNode():
    def __init__(self):
        self.children = {}
        self.word = None

        