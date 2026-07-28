# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # get middle of list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse linked list
        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        maxTwinSum = 0
        while prev:
            maxTwinSum = max(maxTwinSum, prev.val + head.val)
            prev = prev.next
            head = head.next
        return maxTwinSum
        
