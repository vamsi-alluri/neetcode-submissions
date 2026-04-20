# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        fast = head
        slow = head
        
        if not fast.next:
            return False

        slow = slow.next
        fast = fast.next.next

        while (slow and fast and slow != fast):
            if not fast.next:
                return False
            fast = fast.next.next
            slow = slow.next
        
        if (slow == fast):
            return True
        else:
            return False
