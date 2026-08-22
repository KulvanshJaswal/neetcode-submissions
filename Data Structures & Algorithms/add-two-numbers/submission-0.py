# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        left_num = ""
        left = l1

        while left != None:
            left_num += str(left.val)
            left = left.next
        
        right_num = ""
        right = l2

        while right != None:
            right_num += str(right.val)
            right = right.next

        left_num = int(left_num[::-1])
        right_num = int(right_num[::-1])

        summed = left_num + right_num

        summed = str(summed)
        summed = summed[::-1]

        head = None
        temp = None
        for num in summed:
            new_node = ListNode(int(num))
            if not head:
                head = new_node
                temp = head
            else:
                temp.next = new_node
                temp = temp.next
        return head