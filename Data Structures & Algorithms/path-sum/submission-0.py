# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # base case
        currSum = 0
        def dfs(root, currSum, targetSum):
            if not root:
                return False
            currSum+=root.val

            # if it's a leaf
            if not root.left and not root.right:
                if currSum == targetSum:
                    return True
                else:
                    return False
            
            # if it's not a leaf
            if dfs(root.left, currSum, targetSum):
                return True
            if dfs(root.right, currSum, targetSum):
                return True
            return False

        return dfs(root, 0, targetSum)

        