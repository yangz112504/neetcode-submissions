# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in order traversal
        stack = []
        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            stack.append(root.val)
            if len(stack) == k:
                return stack[-1]
            right = dfs(root.right)
            return max(left, right)
        return dfs(root)