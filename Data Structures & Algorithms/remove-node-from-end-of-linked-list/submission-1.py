# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        temp = head
        length = 0 

        while temp != None:
            length += 1
            temp = temp.next
    
        before = None
        current = head
        after = head.next
        i = 0

        while i < (length - n):
            before = current
            current = after

            if after.next == None:
                after = head
            else:
                after = after.next
            i += 1
            
        if current.next == None:
            before.next = None
            return head

        elif current == head:
            return after
        
        else:
            before.next = after
            return head

