# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        return self.helper(root, 0, targetSum)

    def helper(self, root, current_sum, target_sum):
        if not root:
            return False
        
        current_sum += root.val
    
        # Check if we have reached a leaf node and targetSum becomes 0
        if not root.left and not root.right:  # it's a leaf node
            return current_sum == target_sum
    
        # Recursively check the left and right subtrees
        return self.helper(root.left, current_sum, target_sum) or self.helper(root.right, current_sum, target_sum)
        