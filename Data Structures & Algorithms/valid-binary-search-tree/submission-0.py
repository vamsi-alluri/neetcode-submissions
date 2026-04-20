# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def dfsIsValidBST(self, root: TreeNode) -> int:

        if not root:
            return True

        if root.left.val < root.val < root.right.val:
            return self.dfsIsValidBST(root.left) and self.dfsIsValidBST(root.right)
        else:
            return False

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.dfsIsValidBST(root)
        