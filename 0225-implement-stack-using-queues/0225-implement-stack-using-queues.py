class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class MyStack:
    def __init__(self):
        self.head = None

    def push(self, x: int) -> None:
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def pop(self) -> int:
        if self.head is None:
            return None
        
        popped_value = self.head.value
        self.head = self.head.next
        
        return popped_value

    def top(self) -> int:
        if self.head is None:
            return None
        
        return self.head.value

    def empty(self) -> bool:
        return self.head is None