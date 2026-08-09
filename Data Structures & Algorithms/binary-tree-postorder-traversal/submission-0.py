# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = [root] # keep track of current node
        visited = [False] # keep track of visited already so we don't double visit
        res = []    
        while stack:
            currStack = stack.pop()
            currVisited = visited.pop()
            if currVisited:
                res.append(currStack.val)
            else: 
                # not visited, so first append current node val to be visited last
                stack.append(currStack)
                visited.append(True)
                if currStack.right:
                    stack.append(currStack.right)
                    visited.append(False)
                if currStack.left:
                    stack.append(currStack.left)
                    visited.append(False)
        return res
                
        

        