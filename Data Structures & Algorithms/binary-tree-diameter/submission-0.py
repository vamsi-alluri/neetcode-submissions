# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node: Optional[TreeNode]) -> (int, int):
        if not node:
            return 0, 0   # (height, diameter)

        left_h, left_d = self.dfs(node.left)
        right_h, right_d = self.dfs(node.right)

        height = 1 + max(left_h, right_h)
        diameter = max(left_d, right_d, left_h + right_h)

        return height, diameter

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)[1]

