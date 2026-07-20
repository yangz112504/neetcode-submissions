class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True
        

    def search(self, word: str) -> bool:

        curr = self.root
        
        def dfs(node, index):
            if index == len(word):
                return node.word # want to return whether it is a word or not

            curr = node
            char = word[index]
            if char in curr.children:
                return dfs(curr.children[char], index+1)
            elif char == '.':
                for ch, chNode in curr.children.items():
                    if dfs(chNode, index+1):
                        return True
            # all . possibilities is exhausted and char not in curr.children
            return False
        return dfs(curr, 0)



        
