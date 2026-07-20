# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Craft hashmap that tells is where each value in inorder is
        indices = {}
        for index, value in enumerate(inorder):
            indices[value] = index
        
        self.preOrderIndex = 0
        def dfs(l, r):
            # If no subtree exists, return None
            if l > r:
                return None
            # Current preorder value becomes the root of this subtree
            rootVal = preorder[self.preOrderIndex]
            self.preOrderIndex+=1

            #Create a new node
            root = TreeNode(rootVal)

            #Find where new node is in inorder to get subtrees
            rootIndex = indices[rootVal]
            
            root.left = dfs(l, rootIndex-1)
            root.right = dfs(rootIndex+1, r)
            return root
        return dfs(0, len(inorder)-1)

