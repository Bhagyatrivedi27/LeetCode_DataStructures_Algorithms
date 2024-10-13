class ListNode:
    # NOTHING CAN BE CHANGED HERE
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


############################################################
#  class  Slist
###########################################################
class Slist:
    def __init__(self):
        # NOTHING CAN BE CHANGED HERE
        self._first = None
        self._last = None
        self._len = 0

    # Public method to add to the end of the list
    def append(self, value):
        new_node = ListNode(value)
        if self._first is None:
            self._first = new_node
            self._last = new_node
        else:
            self._last.next = new_node
            self._last = new_node
        self._len += 1

    # Public method to add to the front of the list
    def prepend(self, value):
        new_node = ListNode(value)
        if self._first is None:
            self._first = new_node
            self._last = new_node
        else:
            new_node.next = self._first
            self._first = new_node
        self._len += 1

    # Public method to remove and return the first element
    def remove_first(self):
        if self._first is None:
            return None
        value = self._first.val
        self._first = self._first.next
        self._len -= 1
        if self._first is None:
            self._last = None
        return value

    # Public method to remove the last element
    def remove_last(self):
        if self._first is None:
            return None
        if self._first == self._last:
            value = self._first.val
            self._first = None
            self._last = None
            self._len = 0
            return value
        current = self._first
        while current.next != self._last:
            current = current.next
        value = self._last.val
        self._last = current
        self._last.next = None
        self._len -= 1
        return value

    # Public method to get the first element's value
    def get_first(self):
        if self._first is None:
            return -1
        return self._first.val

    # Public method to get the last element's value
    def get_last(self):
        if self._last is None:
            return -1
        return self._last.val

    # Check if the list is empty
    def is_empty(self):
        return self._len == 0

    # Return the current length of the list
    def length(self):
        return self._len

    # Reset the list
    def reset(self):
        self._first = None
        self._last = None
        self._len = 0


############################################################
#  class  MyStack
# 225. Implement Stack using Queues
# https://leetcode.com/problems/implement-stack-using-queues
###########################################################
class MyStack:
    def __init__(self):
        # Use Slist for stack implementation
        self._s = Slist()

    def push(self, x: int) -> None:
        self._s.prepend(x)

    def pop(self) -> int:
        return self._s.remove_first()

    def top(self) -> int:
        return self._s.get_first()

    def empty(self) -> bool:
        return self._s.is_empty()


############################################################
#  class  MyQueue
# 232. Implement Queue using Stacks
# https://leetcode.com/problems/implement-queue-using-stacks/
###########################################################
class MyQueue:
    def __init__(self):
        # Use Slist for queue implementation
        self._s = Slist()

    def push(self, x: int) -> None:
        self._s.append(x)

    def pop(self) -> int:
        return self._s.remove_first()

    def peek(self) -> int:
        return self._s.get_first()

    def empty(self) -> bool:
        return self._s.is_empty()


############################################################
#  MyCircularQueue
# 622. Design Circular Queue
# https://leetcode.com/problems/design-circular-queue/
###########################################################
class MyCircularQueue:
    def __init__(self, k: int):
        self._K = k
        self._s = Slist()

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self._s.append(value)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self._s.remove_first()
        return True

    def Front(self) -> int:
        return self._s.get_first() if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self._s.get_last() if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self._s.is_empty()

    def isFull(self) -> bool:
        return self._s.length() == self._K


############################################################
#  MyCircularDeque
# 641. Design Circular Deque
# https://leetcode.com/problems/design-circular-deque
###########################################################
class MyCircularDeque:
    def __init__(self, k: int):
        self._K = k
        self._s = Slist()

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self._s.prepend(value)
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self._s.append(value)
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self._s.remove_first()
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self._s.remove_last()
        return True

    def getFront(self) -> int:
        return self._s.get_first() if not self.isEmpty() else -1

    def getRear(self) -> int:
        return self._s.get_last() if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self._s.is_empty()

    def isFull(self) -> bool:
        return self._s.length() == self._K
