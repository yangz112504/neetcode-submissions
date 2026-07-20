# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def successorVal(self, curr: Optional[TreeNode]):
        while curr and curr.left:
            curr = curr.left
        return curr.val
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # we need to keep track of the whole tree's path, so we keep pointers to left and right
        if not root:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # 2 cases, has 0 or 1 children or has 2 children
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minNodeVal = self.successorVal(root.right)
                root.val = minNodeVal
                root.right = self.deleteNode(root.right, minNodeVal)
        return root
        