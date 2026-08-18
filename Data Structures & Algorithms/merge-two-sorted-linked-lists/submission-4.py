# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        
        if not list2:
            return list1

        head = None
        temp = head

        while list1 and list2:
            if list1.val >= list2.val:
                chosen = list2
                list2 = list2.next
            else:
                chosen = list1
                list1 = list1.next
            if not head:
                head = chosen
                temp = chosen
            else:
                temp.next = chosen
                temp = temp.next

        if list1:
            temp.next = list1
        if list2:
            temp.next = list2
        return head