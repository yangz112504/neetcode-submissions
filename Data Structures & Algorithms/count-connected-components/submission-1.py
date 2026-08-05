class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        totalN = n # because number of connceted comonents = unique components
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
            # everytime u union successfully the number of components decrease, so return numebr of left components!
            if union(a,b):
                totalN-=1
        return totalN
            
