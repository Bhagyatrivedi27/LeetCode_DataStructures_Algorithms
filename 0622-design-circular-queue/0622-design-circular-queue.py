class ListNode:    
    def __init__(self, value=None):
        self.value = value
        self.next = None


class MyCircularQueue:
    def __init__(self, k: int):
        self.max_size = k
        self.size = 0
        self.front = None
        self.rear = None

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        new_node = ListNode(value)

        if self.isEmpty():
            self.front = new_node
            self.rear = new_node
            new_node.next = self.front  
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front 

        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front

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
        return self.size == self.max_size


class MyCircularDeque:
    def __init__(self, k: int):
        self.max_size = k
        self.size = 0
        self.front = None
        self.rear = None

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        new_node = ListNode(value)

        if self.isEmpty():
            self.front = new_node
            self.rear = new_node
            new_node.next = self.front  
        else:
            new_node.next = self.front
            self.front = new_node
            self.rear.next = self.front  

        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        new_node = ListNode(value)

        if self.isEmpty():
            self.front = new_node
            self.rear = new_node
            new_node.next = self.front  
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front  

        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front

        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            current = self.front
            while current.next != self.rear:
                current = current.next
            current.next = self.front
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


class MyStack:
    def __init__(self):
        self.head = None

    def push(self, x: int) -> None:
        new_node = ListNode(x)
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


class Solution:
    def lowestCommonAncestor(self, root: 'Node', p: 'Node', q: 'Node') -> 'Node':
        current = root

        # Traverse the tree
        while current:
            if p.val < current.val and q.val < current.val:
                current = current.left
            elif p.val > current.val and q.val > current.val:
                current = current.right
            else:
                return current