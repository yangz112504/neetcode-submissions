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
            inMid = inorderMap[preorder[preLeft]]
            leftSize = inMid - inLeft
            rightSize = inRight - inMid
            # Left side:
            # preLeft is just increased by 1
            # preRight is the size of the left Subtree
            # inLeft 
            # inRight is just the middle index decreased by 1 because that is the boundary of new subtree
            root.left = builder(preLeft+1, preLeft + leftSize, inLeft, inMid-1 )
            # Right Side:
            # preLeft is the wherever the left subtree started + the remaining size of left subtree + 1
            # preRight is just the end of the preorder array
            # inLeft is just one to the right of inMid, signaling the start of right subtree
            # in right is just to the end of inOrder array, signaling the end of the right subtree
            root.right = builder(preLeft + leftSize + 1, preRight, inMid+1, inRight)
            return root
        n = len(preorder)-1
        return builder(0,n,0,n )

            
        
        
    