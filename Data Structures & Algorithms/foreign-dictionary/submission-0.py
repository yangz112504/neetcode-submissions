class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        for w in words:
            for c in w:
                adj[c] = set()
        # we want every character to be mapped into a set

        for i in range(len(words)-1):
            # compare adjacent words
            word1 = words[i]
            word2 = words[i+1]
            # check if word with prefix comes before prefix
            minLen = min(len(word1),len(word2))
            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ""
            
            # compare only equivalent length of the words and determine lexicographical order
            for j in range(minLen):
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
                    break
        
        visited = {} # False == visited, True == Current Path
        res = []

        def dfs(c):
            if c in visited:
                return visited[c]
            visited[c] = True
            for neighbor in adj[c]:
                if dfs(neighbor):
                    return True
            
            visited[c] = False
            res.append(c)
            return False
        
        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)