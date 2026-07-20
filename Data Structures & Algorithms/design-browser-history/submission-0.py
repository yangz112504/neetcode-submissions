class BrowserNode:
    
    def __init__(self,page: str):
        self.page = page
        self.next = None
        self.prev = None
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = BrowserNode(homepage)
        self.curr = self.head
        

    def visit(self, url: str) -> None:
        newNode = BrowserNode(url)
        self.curr.next = newNode
        newNode.prev = self.curr
        self.curr = newNode
        

    def back(self, steps: int) -> str:
        while self.curr.prev and steps > 0:
            self.curr = self.curr.prev
            steps-=1
        return self.curr.page

    def forward(self, steps: int) -> str:
        while self.curr.next and steps > 0:
            self.curr = self.curr.next
            steps-=1
        return self.curr.page


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)