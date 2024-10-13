class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class Solution:
    def lowestCommonAncestor(self, root: 'Node', p: 'Node', q: 'Node') -> 'Node':
        current = root
        
        # Simulate traversal while keeping track of the path using a singly linked list
        ancestor_path = ListNode(current.val)  # Head of the singly linked list
        
        # Traverse the tree
        while current:
            # Add current node's value to the ancestor path
            new_node = ListNode(current.val)
            new_node.next = ancestor_path
            ancestor_path = new_node
            
            # If both p and q are smaller than current, go to the left subtree
            if p.val < current.val and q.val < current.val:
                current = current.left
            # If both p and q are larger than current, go to the right subtree
            elif p.val > current.val and q.val > current.val:
                current = current.right
            else:
                # We have found the split point, this is the LCA
                return current
