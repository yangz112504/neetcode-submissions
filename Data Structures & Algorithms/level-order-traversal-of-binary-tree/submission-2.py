# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        queue = deque() # queue to append elements to the tail and remove from head level by level

        if root:
            queue.append(root)
        
        while len(queue) > 0:
            subarray = []
            for i in range(len(queue)):
                curr = queue.popleft()
                subarray.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(subarray)
        return res

        