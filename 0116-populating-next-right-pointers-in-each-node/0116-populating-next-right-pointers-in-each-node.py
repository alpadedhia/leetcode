"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from queue import Queue

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        
        q = Queue()
        if root.left:
            q.put(root.left)
        if root.right:
            q.put(root.right)

        while not q.empty():
            prev = None
            q_size = q.qsize()
            for _ in range(q_size):
                node = q.get()
                if prev:
                    prev.next = node
                prev = node
                
                if node.left:
                    q.put(node.left)
                
                if node.right:
                    q.put(node.right)
        
        return root

        