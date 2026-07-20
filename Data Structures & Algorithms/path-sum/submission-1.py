# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def builder(root, currSum):
            # if empty / doesnt exist, return False
            if not root:
                return False

            # add it to the total sum
            currSum+=root.val

            # if a leaf node and not empty
            if not root.left and not root.right:
                if currSum == targetSum:
                    return True
                else:
                    return False

            if builder(root.left,currSum):
                return True
            if builder(root.right, currSum):
                return True
            return False
        return builder(root, 0)
        