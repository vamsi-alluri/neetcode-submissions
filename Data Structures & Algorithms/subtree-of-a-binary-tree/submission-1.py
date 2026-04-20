# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def dfs_equal(self, tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:

        if tree1 and tree2:
            if tree1.val == tree2.val:
                 return self.dfs_equal(tree1.left, tree2.left) and self.dfs_equal(tree1.right, tree2.right)
            else:
                return False
        elif not tree1 and not tree2:
            return True
        else:
            return False 

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not subRoot:
            return False

        if not root:
            return False

        if self.dfs_equal(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) 




