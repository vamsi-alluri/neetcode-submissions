# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([])
        queue.appendleft(root)
        res = []

        while queue:
            queue_len = len(queue)
            result_level = []

            for i in range(queue_len):
                element = queue.pop()
                if element:
                    result_level.append(element.val)
                    print(f"{element.val} -> l{element.left}, r{element.right}")
                    queue.appendleft(element.left)
                    queue.appendleft(element.right)
            if result_level:
                res.append(result_level)
        return res


    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        self.levelOrder(root)

        while root:
            res.append(root.val)
            root = root.right if root.right else root.left
        
        return res



        