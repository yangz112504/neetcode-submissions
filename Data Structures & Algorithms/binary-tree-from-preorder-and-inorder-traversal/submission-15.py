# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder is for the order of the roots that are going to be in the binary tree
        # in order is for the size of the subtrees

        # in order map shows us where each value(index) each root in inorder traversal appears
        inorderMap = {val : i for i,val in enumerate(inorder)}
        def builder(preLeft, preRight, inLeft, inRight):
            if preLeft > preRight:
                return None
            root = TreeNode(preorder[preLeft])
            inMid = inorderMap[preorder[preLeft]]
            leftSize = inMid - inLeft # gives you size of left subtree
            # in left stays the same bc it's the absolute boundary of left subtree 
            # inRight is going to be the value right before inMid for left subtree
            root.left = builder(preLeft + 1, preLeft + leftSize, inLeft, inMid-1)
            # in right stays the same bc it's the absolute boundary of right subtree
            # in left is going to be value right after inMid for right subtree
            root.right = builder(preLeft + leftSize + 1, preRight, inMid + 1, inRight)
            return root
        n = len(preorder)-1
        return builder(0,n,0,n)