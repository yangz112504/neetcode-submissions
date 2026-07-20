# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # if empty / doesnt exist, return False
        if not root:
            return False

        # subtract from target sum
        targetSum-=root.val

        # if a leaf node and not empty
        if not root.left and not root.right:
            if targetSum == 0:
                return True
            else:
                return False

        if self.hasPathSum(root.left,targetSum):
            return True
        if self.hasPathSum(root.right, targetSum):
            return True
        return False
        