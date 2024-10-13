############################################################
# Write code in file solution.py 
# Post solution.py in Canvas along with 4 screenshots that show Leetcode has passed.
# Cut and paste the whole solution.py file in Leetcode and run. All tests must pass
# You should do this 4 times for problems 225, 232, 622, and 641.
# TA will run solution.py file 4 times for 225, 232, 622, and 641.
# All tests must pass for 100% credit.
###########################################################

class ListNode:
    #NOTHING CAN BE CHANGED HERE
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
         
            
############################################################
#  class  Slist
###########################################################   
class Slist:
    def __init__(self):
        #NOTHING CAN BE CHANGED HERE
        self._first = None
        self._last = None
        self._len = 0 
        
    #############################
    # WRITE All public functions BELOW
    # YOU CAN HAVE ANY NUMBER OF PRIVATE FUNCTIONS YOU WANT
    #############################
    
    def append(self, val):
        # Append value to the list
        new_node = ListNode(val)
        if self._first is None:
            self._first = new_node
            self._last = new_node
        else:
            self._last.next = new_node
            self._last = new_node
        self._len += 1
    
    def remove_first(self):
        # Remove first element of the list
        if self._first is not None:
            value = self._first.val
            self._first = self._first.next
            if self._first is None:
                self._last = None
            self._len -= 1
            return value
        return None
    
    def get_first(self):
        # Get the first element's value
        if self._first is not None:
            return self._first.val
        return None
    
    def get_last(self):
        # Get the last element's value
        if self._last is not None:
            return self._last.val
        return None
    
    def is_empty(self):
        return self._len == 0
    
    def length(self):
        return self._len
    
    def reset(self):
        # Reset the list
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
        self._s = Slist()

    def push(self, x: int) -> None:
        self._s.append(x)

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
        new_node = ListNode(value)
        if self._s._first is None:
            self._s._first = new_node
            self._s._last = new_node
        else:
            new_node.next = self._s._first
            self._s._first = new_node
        self._s._len += 1
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
        if self._s._len == 1:
            self._s.reset()
            return True
        current = self._s._first
        while current.next != self._s._last:
            current = current.next
        current.next = None
        self._s._last = current
        self._s._len -= 1
        return True

    def getFront(self) -> int:
        return self._s.get_first() if not self.isEmpty() else -1

    def getRear(self) -> int:
        return self._s.get_last() if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self._s.is_empty()

    def isFull(self) -> bool:
        return self._s.length() == self._K
