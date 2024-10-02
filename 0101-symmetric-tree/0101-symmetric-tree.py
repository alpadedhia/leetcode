# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = Queue()

        q.put(root.left)
        q.put(root.right)
    
        while not q.empty():
            left = q.get()
            right = q.get()

            if not left and not right:
                continue

            if not left or not right or left.val != right.val:
                return False 

            q.put(left.left)
            q.put(right.right)
            q.put(left.right)
            q.put(right.left)

        return True