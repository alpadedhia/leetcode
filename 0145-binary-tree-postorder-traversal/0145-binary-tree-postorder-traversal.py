# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
         return []
         
        result = []
        stack = [(root, None)]
    
        while len(stack) != 0:
            node, zone = stack[-1]
        
            if not zone:
                stack[-1] = (node, "preorder")
                if node.left:
                    stack.append((node.left, None))
            elif zone == "preorder":
                stack[-1] = (node, "inorder")
                if node.right:
                    stack.append((node.right, None))
            else:
                stack[-1] = (node, "postorder")
                result.append(node.val)
                stack.pop()
            
        return result
        