# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0

        counter = [0]  # Use a list to make counter mutable
        result = [None]  # Store the result here once the k-th element is found

        def inorder(node, counter, k):
            if not node:
                return

            inorder(node.left, counter, k)

            counter[0] += 1
            if counter[0] == k:
                result[0] = node.val
                return  # Stop further recursion once the element is found

            inorder(node.right, counter, k)

        inorder(root, counter, k)
        return result[0]  # Return the stored k-th smallest element
