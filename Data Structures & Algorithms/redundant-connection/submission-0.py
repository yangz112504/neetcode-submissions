class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        [0,1,2,3,4,5]

        def find(v):
            if parent[v] == v:
                return v
            parent[v] = find(parent[v])
            return parent[v]

        def union(a,b):
            rootA = find(a)
            rootB = find(b)
            if rootA == rootB:
                return False
            parent[rootA] = rootB
            return True

        for ai, bi in edges:
            if not union(ai,bi):
                return [ai,bi]

    
        