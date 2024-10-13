# Definition of a node in a singly linked list
class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


# Circular Queue using singly linked list
class MyCircularQueue:
    def __init__(self, k: int):
        self.capacity = k
        self.current_size = 0
        self.front = None
        self.rear = None

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        new_node = Node(value)

        if self.isEmpty():
            self.front = new_node
            self.rear = new_node
            new_node.next = self.front  # Circular link
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front  # Maintain circularity

        self.current_size += 1
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

        self.current_size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.front.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.rear.val

    def isEmpty(self) -> bool:
        return self.current_size == 0

    def isFull(self) -> bool:
        return self.current_size == self.capacity


# Circular Deque using singly linked list
class MyCircularDeque:
    def __init__(self, k: int):
        self.limit = k
        self.length = 0
        self.front = None
        self.rear = None

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        new_node = Node(value)

        if self.isEmpty():
            self.front = new_node
            self.rear = new_node
            new_node.next = self.front  # Circular link
        else:
            new_node.next = self.front
            self.front = new_node
            self.rear.next = self.front  # Maintain circularity

        self.length += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        new_node = Node(value)

        if self.isEmpty():
            self.front = new_node
            self.rear = new_node
            new_node.next = self.front  # Circular link
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front  # Maintain circularity

        self.length += 1
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

        self.length -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            temp = self.front
            while temp.next != self.rear:
                temp = temp.next
            temp.next = self.front
            self.rear = temp

        self.length -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.front.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.rear.val

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.limit


# Stack implementation using singly linked list
class MyStack:
    def __init__(self):
        self.top_node = None

    def push(self, x: int) -> None:
        new_node = Node(x)
        new_node.next = self.top_node
        self.top_node = new_node

    def pop(self) -> int:
        if self.top_node is None:
            return None
        top_value = self.top_node.val
        self.top_node = self.top_node.next
        return top_value

    def top(self) -> int:
        if self.top_node is None:
            return None
        return self.top_node.val

    def empty(self) -> bool:
        return self.top_node is None


# Lowest Common Ancestor for a Binary Search Tree (BST)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current = root

        # Traversing the BST
        while current:
            if p.val < current.val and q.val < current.val:
                current = current.left
            elif p.val > current.val and q.val > current.val:
                current = current.right
            else:
                return current
