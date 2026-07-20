"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # we create a map so we can keep track of if we already cloned a node
        if node is None:
            return None
        oldToNew = {} # in bfs this is the hashmap that you will return
        queue = deque()
        queue.append(node)
        newNode = Node(node.val)
        oldToNew[node] = newNode

        while len(queue) > 0:
            currNode = queue.popleft()
            for neighbor in currNode.neighbors:
                if neighbor not in oldToNew:
                    oldToNew[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                oldToNew[currNode].neighbors.append(oldToNew[neighbor])
        return oldToNew[node]







# def dfs(node):
#             if node in oldToNew:
#                 return oldToNew[node]
            
#             # need to clone new node
#             newNode = Node(node.val)
#             oldToNew[node] = newNode

#             # need to add the og neighbors to new node neighbors
#             for neighbor in node.neighbors:
#                 newNode.neighbors.append(dfs(neighbor))
#             return newNode
        
#         return dfs(node) if node else None