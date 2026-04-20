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

    def dfs(self, root: TreeNode, maxVal: int) -> int:
        goodNodesCount = 0

        if not root:
            return 0

        if root.val >= maxVal:
            maxVal = root.val
            print(root.val)
            goodNodesCount += 1
            
        goodNodesCount += self.dfs(root.left, maxVal)
        goodNodesCount += self.dfs(root.right, maxVal)

        return goodNodesCount

    def goodNodes(self, root: TreeNode) -> int:
        self.levelOrder(root)
        return self.dfs(root, -1)

        