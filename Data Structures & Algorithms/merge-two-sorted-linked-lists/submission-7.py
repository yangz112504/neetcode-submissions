# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # use currentnode to iterate throughthe list
        curr = ListNode()
        # Use dummy node to keep track of start
        startNode = curr
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                curr = list1
                list1 = list1.next
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next
        # we can just append the next node in the list because it points to the rest of the list
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        return startNode.next