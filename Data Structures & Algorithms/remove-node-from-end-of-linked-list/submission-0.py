# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        first, second = head, head
        prev = None
        while n:
            first = first.next
            n -= 1
        
        while first:
            first = first.next
            prev = second
            second = second.next
        
        if prev and prev.next:
            prev.next = prev.next.next
        else:
            return None

        return head

        