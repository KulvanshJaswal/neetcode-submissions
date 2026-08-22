#Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        temp = dummy
        carry = 0

        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
            else:
                val1 = 0
            if l2:
                val2 = l2.val
            else:
                val2 = 0

            summed = val1 + val2 + carry
            carry = summed // 10

            temp.next = ListNode(summed % 10)
            temp = temp.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next