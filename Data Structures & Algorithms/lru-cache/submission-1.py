class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        """we initialize and connect left and right nodes because left is 
        least recently used and right is most recently used and we 
        want to swap them whenever 
        and if we want to insert new node we can put it in between left
        and right"""

        self.left = Node(0,0) # dummy node pointing to LRU node
        self.right = Node(0,0) # dummy node POINTING to MRU node
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        """Remove node from current position"""
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        """Insert at rightmost position to make it the MRU"""
        # prev pointer
        prev = self.right.prev

        #next pointer
        nxt = self.right

        #setting pointers from prev and next to node
        prev.next = node
        nxt.prev = node

        #setting pointers from node to next and prev
        node.next = nxt
        node.prev = prev


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key]) # take from curr pos
            self.insert(self.cache[key]) # make it MRU
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # no matter what position it is remove it and make it MRU
            self.remove(self.cache[key]) 
        self.cache[key] = Node(key, value) #actually insterting it into hashap
        self.insert(self.cache[key]) 

        # if over capacity
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key] #delete it from hashmap

        
