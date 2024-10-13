class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        # Initialize the circular queue with a fixed size
        self.capacity = k
        self.size = 0
        self.front = None
        self.rear = None

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        new_node = Node(value)
        
        if self.isEmpty():
            # If queue is empty, point front and rear to the new node
            self.front = new_node
            self.rear = new_node
            new_node.next = new_node  # Circular connection
        else:
            # Insert at the end (rear)
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front  # Maintain the circular link
        
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.front == self.rear:
            # Only one element in the queue
            self.front = None
            self.rear = None
        else:
            # Move front pointer to the next node
            self.front = self.front.next
            self.rear.next = self.front  # Maintain the circular link
        
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.front.value

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.rear.value

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity