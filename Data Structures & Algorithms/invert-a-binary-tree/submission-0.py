# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return root

        print(f"Current evaluated: {root.val}")
        temp = TreeNode(root.val)
        temp.left = self.invertTree(root.right)
        temp.right = self.invertTree(root.left)
        root.left = temp.left
        root.right = temp.right

        return root