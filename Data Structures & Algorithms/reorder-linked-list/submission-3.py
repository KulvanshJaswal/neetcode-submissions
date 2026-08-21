# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return None

        mid = head
        fast = head.next

        while fast != None and fast.next != None:
            mid = mid.next
            fast = fast.next.next
            
        before = None
        current = mid.next
        mid.next = None
        
        while current != None:
            temp = current.next
            current.next = before
            before = current
            current = temp

        first = head
        after = before

        while after:
            temp1 = first.next
            temp2 = after.next

            first.next = after
            after.next = temp1
            
            first = temp1
            after = temp2