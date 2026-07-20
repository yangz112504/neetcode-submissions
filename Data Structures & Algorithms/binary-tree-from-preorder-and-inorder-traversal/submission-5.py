# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # We want the indexes of inorder so we can easily find indexes of the middles aka roots which are
        # exclusively found in inorder
        indexMap = {val: i for i,val in enumerate(inorder)}

        # pre order shows you the order that the roots go
        # in order shows you where each node goes once you figure out the root
        def builder(preorder, inorder):
            if not preorder or not inorder:
                return None
            root = TreeNode(preorder[0])
            mid = inorder.index(preorder[0])
            root.left = builder(preorder[1:mid+1], inorder[:mid])
            root.right = builder(preorder[mid+1:], inorder[mid+1:])
            return root
        return builder(preorder,inorder)
        
        


