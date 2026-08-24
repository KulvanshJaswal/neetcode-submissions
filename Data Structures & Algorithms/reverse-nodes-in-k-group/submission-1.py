class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
    
        dummy = ListNode(0)
        dummy.next = head
        jump = dummy 
        
        while True:
            pivot = jump
            for i in range(k):
                pivot = pivot.next
                if not pivot:
                    return dummy.next
            
            starter = jump.next
            after = pivot.next
        
            pivot.next = None
            
            before = None
            current = starter
            while current:
                temp = current.next
                current.next = before
                before = current
                current = temp

            jump.next = before         
            starter.next = after       
            
            jump = starter
