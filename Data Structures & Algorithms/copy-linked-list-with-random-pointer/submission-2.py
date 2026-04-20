"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        seen = collections.defaultdict(lambda: Node(0))
        seen[None] = None

        itr = head

        while itr:

            seen[itr].val = itr.val
            seen[itr].next = seen[itr.next]
            seen[itr].random = seen[itr.random]
            itr = itr.next
        
            self.printList(seen[head], "new list")
            self.printList(itr, "old list")

        return seen[head]
        