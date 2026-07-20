class ListNode:
    def __init__(self, val = 0, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        curr = self.head
        for i in range(0,index+1):
            curr = curr.next
        return curr.val
        

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        if self.size == 0:
            self.head.next = newNode
            newNode.prev = self.head
            newNode.next = self.tail
            self.tail.prev = newNode
        else:
            afterHead = self.head.next
            self.head.next = newNode
            newNode.prev = self.head
            newNode.next = afterHead
            afterHead.prev = newNode
        self.size+=1

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        if self.size == 0:
            self.head.next = newNode
            newNode.prev = self.head
            newNode.next = self.tail
            self.tail.prev = newNode
        else:
            beforeTail = self.tail.prev
            self.tail.prev = newNode
            newNode.next = self.tail
            newNode.prev = beforeTail
            beforeTail.next = newNode
        self.size+=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index == self.size:
            self.addAtTail(val)
        else:
            curr = self.head.next
            for i in range(0,index):
                curr = curr.next
            newNode = ListNode(val)
            prevNode = curr.prev

            prevNode.next = newNode
            newNode.prev = prevNode
            newNode.next = curr
            curr.prev = newNode
            self.size+=1
        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        else:
            curr = self.head.next
            for i in range(0,index):
                curr = curr.next
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            self.size -=1

    
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)