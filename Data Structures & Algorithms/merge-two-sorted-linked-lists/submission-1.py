# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Add to left.
        # Define pointers: curr1, curr2, next1, next2
        curr1 = list1
        curr2 = list2
        # Instead of starting to add into a list, keeping dummy as an anchor as the first node. This'll be my pointer as I add to the list.
        dummy = ListNode()
        curr = dummy
        
        while (curr1 and curr2):
            # Only add values that are lesser
            if curr1.val <= curr2.val:
                curr.next = curr1 # Assign this to the first node.
                curr1 = curr1.next
            else:
                curr.next = curr2 # Assign this to the first node.
                curr2 = curr2.next
                # 3 -> 4 -> 6
                # 1 -> 5 -> 6
                # 1 -> 3 -> 4 -> 5 -> 6 -> 6
            curr = curr.next

        if curr1:
            curr.next = curr1
        elif curr2:
            curr.next = curr2
        
        return dummy.next # From the anchor

        