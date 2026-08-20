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
                 
    
        dummy = ListNode(0)
        dummy.next = head

        current = dummy
        fast = fast
        
        while fast != None:
            current = current.next
            fast = fast.next 

        if current == dummy:
            return head.next
        
        else:
            current.next = current.next.next
            return head

