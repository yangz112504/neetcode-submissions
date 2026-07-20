"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # bfs implementation
        if not node:
            return None
        queue = deque()
        queue.append(node)

        copy = Node(node.val)
        oldToNew = {}
        oldToNew[node] = copy
        while queue:
            for i in range(len(queue)):
                n = queue.popleft()
                for nei in n.neighbors:
                    if nei not in oldToNew:
                        oldToNew[nei] = Node(nei.val)
                        queue.append(nei)
                    oldToNew[n].neighbors.append(oldToNew[nei])
        return oldToNew[node]
        