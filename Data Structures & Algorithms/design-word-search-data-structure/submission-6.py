class WordDictionary:

    def __init__(self):
        self.root = TreeNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TreeNode()
            curr = curr.children[c]
        curr.word = True
        

    def search(self, word: str) -> bool:
        curr = self.root

        def dfs(index, curr, word):
            # base case assuming no dots how would i do dfs
            if index == len(word):
                return curr.word

            letter = word[index]
            if letter == '.':
                for nextLetter in curr.children:
                    if dfs(index+1, curr.children[nextLetter], word):
                        return True
            else:
                if letter not in curr.children:
                    return False
                curr = curr.children[letter]
                if dfs(index+1,curr, word):
                    return True
            return False

        return dfs(0,curr,word)

        
class TreeNode:
    def __init__(self):
        self.children = {}
        self.word = False