# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode()
        startNode = curr
        while list1 and list2:
            if list1.val < list2.val:
                newNode = ListNode(list1.val)
                list1 = list1.next
            else:
                newNode = ListNode(list2.val)
                list2 = list2.next
            curr.next = newNode
            curr = newNode
        while list1:
            newNode = ListNode(list1.val)
            curr.next = newNode
            curr = newNode
            list1 = list1.next
        while list2:
            newNode = ListNode(list2.val)
            curr.next = newNode
            curr = newNode
            list2 = list2.next
        return startNode.next