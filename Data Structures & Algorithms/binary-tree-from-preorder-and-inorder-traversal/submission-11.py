# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # map of inorder values to their indexes
        # so we know what each subtree length is 
        inorderMap = {val : i for i,val in enumerate(inorder)}

        def builder(preLeft, preRight, inLeft, inRight):
            if preLeft > preRight or inLeft > inRight:
                return None
            root = TreeNode(preorder[preLeft]) # Create the new node of binary Tree
            inMid = inorderMap[preorder[preLeft]] # Where is the new node in the in order map so we know the sub trees of it
            leftSize = inMid - inLeft
            rightSize = inRight - inMid

            # left side
            newPreLeft = preLeft + 1 # incrementing one to go to the next root in the left subtree
            newPreRight = preLeft + leftSize # left side of the mid index root of in order which is the left subtree basically 
            newInLeft = inMid - leftSize # incrementing one to go to the next root in the right subtree
            newInRight = inMid-1 # just the right boundary of left subtree
            root.left = builder(newPreLeft, newPreRight, newInLeft, newInRight )

            # right side
            newPreLeft = preLeft + leftSize + 1
            newPreRight = preRight
            newInLeft = inMid + 1
            newInRight = inRight
            root.right = builder(newPreLeft, newPreRight, newInLeft, newInRight)
            return root
        
        return builder(0,len(preorder)-1, 0, len(inorder)-1)
    
        