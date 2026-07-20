# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #when deleting a node in a BST, there are 3 cases.
        #one child exists, both child exists, no child exists.
        #if one child exists, return it
        #if both child exists, return successor
        #if null, just delete it

        def findMin(root):
            curr = root
            while curr and curr.left:
                curr = curr.left
            #returns leftmost value before null
            return curr

        if not root:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else: #val == root.val
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            else: #both children exist
                minNode = findMin(root.right)
                root.val = minNode.val
                #now changing the key to be deleted from key to root.val
                root.right = self.deleteNode(root.right, root.val)
        return root


        