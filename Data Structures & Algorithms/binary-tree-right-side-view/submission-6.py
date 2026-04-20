# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def levelOrder(self, root: Optional[TreeNode]):
        queue = deque([])
        queue.appendleft(root)
        res = []

        while queue:
            queue_len = len(queue)

            for i in range(queue_len):
                element = queue.pop()
                temp = None
                if element:
                    temp = element.val
                    print(f"{element.val} -> l{element.left.val if element.left else None}, r{element.right.val if element.right else None}")
                    queue.appendleft(element.left)
                    queue.appendleft(element.right)
            if temp:
                res.append(temp)
        return res


    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return self.levelOrder(root)



        