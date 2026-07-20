# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = k
        def dfs(root):
            if not root:
                return None
            left = dfs(root.left)
            if left is not None:
                return left
            
            self.count -= 1 # to make sure we return when k == 0
            if self.count == 0:
                return root.val
            return dfs(root.right)
        return dfs(root)




#  # in order traversal
#         stack = []
#         def dfs(root):
#             if not root:
#                 return -1
#             left = dfs(root.left)
#             stack.append(root.val)
#             if len(stack) == k:
#                 return stack[-1]
#             right = dfs(root.right)
#             return max(left, right)
#         return dfs(root)