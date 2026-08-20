# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next or not head.next.next:
            return False

        current = head.next.next
        behind = head.next

        while current != None:
            if current == behind:
                return True
            else:
                behind = behind.next
                current = current.next
                if current != None:
                    current = current.next
            
        return False