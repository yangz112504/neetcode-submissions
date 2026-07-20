# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root
        newNode = TreeNode(val)
        if root is None:
            return newNode

        while True:
            if val > curr.val:
                if curr.right is None:
                    curr.right = newNode
                    return root
                curr = curr.right
            else:
                if curr.left is None:
                    curr.left = newNode
                    return root
                curr = curr.left
        return root



# if not root:
#             return TreeNode(val)
#         if val > root.val:
#             root.right = self.insertIntoBST(root.right,val)
#         else:
#             root.left = self.insertIntoBST(root.left,val)
#         return root