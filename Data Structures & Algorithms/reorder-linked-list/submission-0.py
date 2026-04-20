# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # Find mid using slow and fast pointers
        mid, end_elem = head, head.next
        while end_elem and end_elem.next:
            mid = mid.next
            end_elem = end_elem.next.next
        
        second_half = mid.next

        # Splitting the second half after mid. So mid points to null and second_half is divided into it's own list.
        prev = mid.next = None
        head2 = second_half
        # Reverse the second half:
        while head2:
            tmp = head2.next
            head2.next = prev   # For the first one, point it to None, denoting the end of list.
            prev = head2
            head2 = tmp

        first_half, second_half = head, prev
        while second_half:   # Second half will be equal or shorter (by 1 in odd length) than first half
            temp1, temp2 = first_half.next, second_half.next
            first_half.next = second_half
            second_half.next = temp1
            first_half, second_half = temp1, temp2


