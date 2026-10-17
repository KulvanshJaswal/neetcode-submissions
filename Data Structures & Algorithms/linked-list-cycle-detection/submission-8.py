# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        slow = head
        fast = head.next

        while fast != None and slow != None:
            if fast == slow:
                return True

            if fast.next and fast.next.next:
                fast = fast.next.next
            else:
                return False
            
            if slow.next != None:
                slow = slow.next
        return False