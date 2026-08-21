# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return None

        mid = None
        fast = head

        while fast != None:
            if mid == None:
                mid = head
            else:
                mid = mid.next
            fast = fast.next
            if fast != None:
                fast = fast.next
            
        before = None
        current = mid.next
        
        while current != None:
            temp = current.next
            current.next = before
            before = current
            current = temp
    
        mid.next = None

        first = head
        second = before

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1
            
            first = temp1
            second = temp2