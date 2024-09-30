"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
from queue import Queue
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        q = Queue()
        q.put(root)

        return self.helper(root, q, [[root.val]], 1)
        
    def helper(self, root, q, values, level):
        if not root:
            return 
        
        while not q.empty():
            q_size = q.qsize()
                
            for _ in range(q_size):
                node = q.get()
                if node.children:
                    if len(values) == level:
                        values.append([])

                for children in node.children:
                    q.put(children)
                    values[level].append(children.val)
   
            level += 1

        return values    
        
        