# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def dfs_by_value(self, tree1: Optional[TreeNode], search_term: int) -> bool:

        if not tree1:
            return None

        if tree1.val == search_term:
            return tree1
        else:
            return self.dfs_by_value(tree1.left, search_term) or self.dfs_by_value(tree1.right, search_term) 

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

        root_subRoot = self.dfs_by_value(root, subRoot.val)

        if not root_subRoot:
            return False
        else:
            return self.dfs_equal(root_subRoot, subRoot)