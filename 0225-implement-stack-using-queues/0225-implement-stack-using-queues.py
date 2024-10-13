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
        self._start = None
        self._end = None
        self._count = 0

    # Method to add to the end of the list
    def append(self, value):
        node = ListNode(value)
        if self._start is None:
            self._start = node
            self._end = node
        else:
            self._end.next = node
            self._end = node
        self._count += 1

    # Method to add to the front of the list
    def prepend(self, value):
        node = ListNode(value)
        if self._start is None:
            self._start = node
            self._end = node
        else:
            node.next = self._start
            self._start = node
        self._count += 1

    # Method to remove and return the first element
    def remove_first(self):
        if self._start is None:
            return None
        val = self._start.val
        self._start = self._start.next
        self._count -= 1
        if self._start is None:
            self._end = None
        return val

    # Method to remove the last element
    def remove_last(self):
        if self._start is None:
            return None
        if self._start == self._end:
            val = self._start.val
            self._start = None
            self._end = None
            self._count = 0
            return val
        current = self._start
        while current.next != self._end:
            current = current.next
        val = self._end.val
        self._end = current
        self._end.next = None
        self._count -= 1
        return val

    # Method to get the first element's value
    def get_first(self):
        if self._start is None:
            return -1
        return self._start.val

    # Method to get the last element's value
    def get_last(self):
        if self._end is None:
            return -1
        return self._end.val

    # Check if the list is empty
    def is_empty(self):
        return self._count == 0

    # Return the current length of the list
    def length(self):
        return self._count

    # Reset the list
    def reset(self):
        self._start = None
        self._end = None
        self._count = 0


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