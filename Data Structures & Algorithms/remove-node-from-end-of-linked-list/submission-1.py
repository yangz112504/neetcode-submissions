# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        #creates a n-size gap between left and right ptrs
        while n > 0 and right:
            right = right.next
            n-=1
        
        #left gets to right before the node that needs to be removed
        while right:
            left = left.next
            right = right.next
        
        #skipping over the node
        left.next = left.next.next
        
        return dummy.next