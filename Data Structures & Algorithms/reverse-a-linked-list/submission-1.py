# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def printList(self, head: Optional[ListNode], formatted_str: str):
        pointer = head
        print(formatted_str, end=": ")
        while pointer:
            print(pointer.val, end=",")
            pointer = pointer.next
        print()

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        pointer = head
        reversed_head = None

        while pointer.next:
            temp_next = pointer.next
            pointer.next = pointer.next.next
            if reversed_head == None:
                temp_next.next = pointer
                reversed_head = temp_next
            else:
                temp_next.next = reversed_head
                reversed_head = temp_next
        
            self.printList(pointer, "pointer")
            self.printList(reversed_head, "Reversed Head")
        return reversed_head if reversed_head else head




        