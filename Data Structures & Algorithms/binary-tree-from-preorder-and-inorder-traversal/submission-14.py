# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderMap = {val:i for i, val in enumerate(inorder)}

        def builder(preLeft, preRight, inLeft,inRight):
            if preLeft > preRight:
                return None
            
            root = TreeNode(preorder[preLeft])
            # Find where this root splits the inorder array
            inMid = inorderMap[preorder[preLeft]]

            # Calculate exactly how many nodes are in the left subtree
            # (Everything from the current start 'inLeft' up to 'inMid - 1')
            leftSize = inMid - inLeft

            # Build Left Subtree
            # - preLeft: Skip the current root -> preLeft + 1
            # - preRight: Start at (preLeft + 1) and move right by 'leftSize' positions -> preLeft + leftSize
            # - inLeft: Stays exactly the same as the current boundary
            # - inRight: Stops right before the mid point -> inMid - 1
            root.left = builder(preLeft+1, preLeft + leftSize, inLeft, inMid-1 )

            # Build Right Subtree
            # - preLeft: Starts right after the left subtree ends -> preLeft + leftSize + 1
            # - preRight: Goes all the way to the end of the current preorder boundary -> preRight
            # - inLeft: Starts right after the mid point -> inMid + 1
            # - inRight: Goes all the way to the end of the current inorder boundary -> inRight
            root.right = builder(preLeft + leftSize + 1, preRight, inMid+1, inRight)
            return root
        n = len(preorder)-1
        return builder(0,n,0,n )

            
        
        
    