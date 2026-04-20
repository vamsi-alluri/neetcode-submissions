# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def dfsIsValidBST(self, root: Optional[TreeNode], low=float("-inf"), high=float("inf")) -> bool:
        if not root:
            return True

        if not (low < root.val < high): # Each node should be within bounds of it's ancestors.
            return False
        else:
            return (self.dfsIsValidBST(root.left, low, root.val) and
                self.dfsIsValidBST(root.right, root.val, high))

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfsIsValidBST(root)
        