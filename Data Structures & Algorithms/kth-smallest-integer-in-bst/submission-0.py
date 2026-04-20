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

        while queue:
            queue_len = len(queue)

            for i in range(queue_len):
                element = queue.pop()
                if element:
                    print(f"{element.val} -> l{element.left.val if element.left else None}, r{element.right.val if element.right else None}")
                    queue.appendleft(element.left)
                    queue.appendleft(element.right)

    def inorder(self, root: Optional[TreeNode]) -> List[int]:
        inorderArr = []

        if not root:
            return []

        print(f"curr root: {root.val}")
        inorderArr.extend(self.inorder(root.left))
        inorderArr.append(root.val)
        inorderArr.extend(self.inorder(root.right))
        print(inorderArr)
        return inorderArr

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.levelOrder(root)
        return self.inorder(root)[k - 1]