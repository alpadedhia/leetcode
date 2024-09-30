# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        # Initialize result list to store all valid paths
        result = []
        
        # Call the helper function with the initial parameters
        self.helper(root, [], targetSum, result)
        
        return result

    def helper(self, root, current_path, target_sum, result):
        if not root:
            return
        
        # Add the current node to the path
        current_path.append(root.val)
        
        # Check if it's a leaf node and the path sum matches target_sum
        if not root.left and not root.right and target_sum == root.val:
            result.append(list(current_path))  # Add a copy of current_path to result
        
        # Recurse on the left and right children with updated target_sum
        self.helper(root.left, current_path, target_sum - root.val, result)
        self.helper(root.right, current_path, target_sum - root.val, result)
        
        # Backtrack by removing the current node from the path
        current_path.pop()