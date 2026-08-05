class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hashset = set() # because number of connceted comonents = unique roots
        parent = [i for i in range(n)]
        def find(v):
            if parent[v] == v:
                return v
            parent[v] = find(parent[v])
            return parent[v]
        
        def union(a,b):
            rootA = find(a)
            rootB = find(b)
            if rootA == rootB: #already union
                return False
            # if not union
            parent[rootA] = rootB
            return True
        
        for a,b in edges:
            union(a,b)
        for num in parent:
            res = find(num)
            if res not in hashset:
                hashset.add(res)
        return len(hashset)
            
