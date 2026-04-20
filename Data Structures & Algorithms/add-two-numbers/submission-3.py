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

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        self.printList(l1, "l1")
        self.printList(l2, "l2")

        dummy = ListNode(None)
        curr = dummy
        carry = 0

        while l1 and l2:
            sum_ = l1.val + l2.val + carry
            if (sum_ > 9):
                carry, sum_ = divmod(sum_, 10)
            print(sum_, carry)


            curr.next = ListNode(sum_)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        

        if carry:
            curr.next = ListNode(carry)
        

        
        return dummy.next
            
            

        
        