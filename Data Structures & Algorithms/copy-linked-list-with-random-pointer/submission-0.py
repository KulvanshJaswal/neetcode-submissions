"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        nodes = {}
        nodes[None] = None
        
        current = head
        while current:
            nodes[current] = Node(current.val)
            current = current.next

        current = head
        nHead = None
        nNodes = None

        while current:
            if nHead == None:
                nHead = nodes[current]
                nNodes = nodes[current]
            nNodes.next = nodes[current.next]
            nNodes.random = nodes[current.random]

            current = current.next
            nNodes = nNodes.next

        return nHead




