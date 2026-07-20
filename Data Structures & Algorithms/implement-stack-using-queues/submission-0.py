from collections import deque

class MyStack:

    def __init__(self):
        self.storageQ = deque()
        self.opQ = deque()
        

    def push(self, x: int) -> None:
        # opQ always gonna start empty
        self.opQ.append(x)

        # use other queue to rearrange items and store old queue items
        while self.storageQ:
            num = self.storageQ.popleft()
            self.opQ.append(num) #adding rest of numbers onto it
        
        self.storageQ = self.opQ
    
        #reset opQ while making sure storageQ is updated
        self.opQ = deque()

    def pop(self) -> int:
        return self.storageQ.popleft() 
        
    def top(self) -> int:
        return self.storageQ[0]

    def empty(self) -> bool:
        return len(self.storageQ) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()