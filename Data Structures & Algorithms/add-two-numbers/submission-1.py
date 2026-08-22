# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        temp = None
        carry = 0

        while l1 or l2 or carry:
            
            if l1 and l2:
                summed = l1.val + l2.val + carry
            elif l1:
                summed = l1.val + carry
            elif l2:
                summed = l2.val + carry
            else:
                summed = carry
            carry = summed // 10

            newNode = ListNode(summed % 10)
            if not head:
                head = newNode
                temp = head
            else:
                temp.next = newNode
                temp = temp.next
            
            if l1 and l2:
                l1 = l1.next
                l2 = l2.next
            elif l1:
                l1 = l1.next
            elif l2:
                l2 = l2.next
            
        return head
            