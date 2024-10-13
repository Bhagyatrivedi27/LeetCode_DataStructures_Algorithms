class ListNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class MyCircularDeque:
    def __init__(self, k: int):
        # Initialize the deque with a given maximum size
        self.max_size = k
        self.size = 0
        self.front = None  # Front pointer of the deque
        self.rear = None   # Rear pointer of the deque
    
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        
        new_node = ListNode(value)
        
        if self.isEmpty():
            # The first element, front and rear will point to the same node
            self.front = new_node
            self.rear = new_node
            new_node.next = None
        else:
            # Add the new node to the front of the deque
            new_node.next = self.front
            self.front = new_node
        
        self.size += 1
        return True
    
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        
        new_node = ListNode(value)
        
        if self.isEmpty():
            # The first element, front and rear will point to the same node
            self.front = new_node
            self.rear = new_node
            new_node.next = None
        else:
            # Add the new node at the rear of the deque
            self.rear.next = new_node
            self.rear = new_node
        
        self.size += 1
        return True
    
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.front == self.rear:
            # Only one element in the deque
            self.front = None
            self.rear = None
        else:
            # Remove the front node and update the front pointer
            self.front = self.front.next
        
        self.size -= 1
        return True
    
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.front == self.rear:
            # Only one element in the deque
            self.front = None
            self.rear = None
        else:
            # Traverse the list to find the second-to-last node
            current = self.front
            while current.next != self.rear:
                current = current.next
            # Update rear and break the link to the last node
            current.next = None
            self.rear = current
        
        self.size -= 1
        return True
    
    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.front.value
    
    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.rear.value
    
    def isEmpty(self) -> bool:
        return self.size == 0
    
    def isFull(self) -> bool:
        return self.size == self.max_size