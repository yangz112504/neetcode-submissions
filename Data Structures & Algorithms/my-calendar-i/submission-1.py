class TreeNode():
    def __init__(self,start,end):
        self.left = None
        self.right = None
        self.start = start
        self.end = end
    def insert(self, newStart, newEnd):
        curr = self
        while True:
            if newStart >= curr.end:
                if not curr.right:
                    curr.right = TreeNode(newStart, newEnd)
                    return True
                curr = curr.right
            if newEnd <= curr.start:
                if not curr.left:
                    curr.left = TreeNode(newStart, newEnd)
                    return True
                curr = curr.left
            else:
                return False

class MyCalendar:
    
    def __init__(self):
        self.root = None 
        

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.root:
            self.root = TreeNode(startTime,endTime)
            return True
        return self.root.insert(startTime, endTime)
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)