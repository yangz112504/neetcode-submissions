# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        dummy = newHead = ListNode()
        while curr1 and curr2:
            if curr1.val < curr2.val:
                newHead.next = curr1
                curr1 = curr1.next
            else:
                newHead.next = curr2
                curr2 = curr2.next
            newHead = newHead.next
        if curr1:
            newHead.next = curr1
        if curr2:
            newHead.next = curr2
        return dummy.next

        