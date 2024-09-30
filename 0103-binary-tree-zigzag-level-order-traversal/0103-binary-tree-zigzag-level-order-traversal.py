# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = Queue()
        q.put(root)
        return self.helper(root, [[root.val]], q)

    def helper(self, root, values, q):
        level = 1

        while not q.empty():
            q_size = q.qsize()
            arr = []
            for _ in range(q_size):
                node = q.get()

                if node.left:
                    q.put(node.left)
                    arr.append(node.left.val)

                if node.right:
                    q.put(node.right)
                    arr.append(node.right.val)

            if arr:
                if len(values) == level:
                    values.append([])
                if level%2 != 0:
                    values[level] = arr[::-1]
                else:
                    values[level] = arr

            level += 1
        
        return values

        