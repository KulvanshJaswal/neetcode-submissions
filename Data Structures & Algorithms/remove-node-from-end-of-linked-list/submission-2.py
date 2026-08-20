# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        fast = head
        i = 0 

        while i < n:
            fast = fast.next
            i += 1
                 
    
        before = None
        current = head
        after = head.next
        
        while fast != None:
            before = current
            current = after
            after = after.next
            fast = fast.next 

        if current.next == None:
            before.next = None
            return head

        elif current == head:
            return after
        
        else:
            before.next = after
            return head

