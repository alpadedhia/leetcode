# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def helper(self, root, q, values, level):
        if not root:
            return 
        
        while not q.empty():
            q_size = q.qsize()
                
            for _ in range(q_size):
                node = q.get()
                if node.left or node.right:
                    if len(values) == level:
                        values.append([])
                if node.left:
                    q.put(node.left)
                    values[level].append(node.left.val)

                if node.right:
                    q.put(node.right)
                    values[level].append(node.right.val)
   
            level += 1

        return values

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = Queue()
        q.put(root)

        return self.helper(root, q, [[root.val]], 1)