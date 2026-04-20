"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:


    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloned = collections.defaultdict(lambda: Node(0))
        cloned[None] = None
        seen = set()

        def dfs(node):
            if node in cloned:
                return cloned[node]

            cloned[node] = Node(node.val)
            seen.add(node)
            
            for neighbor in node.neighbors:
                cloned[node].neighbors.append(dfs(neighbor))
                
            return cloned[node]
        
        return dfs(node)

        