# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(p,q)])
        
        while queue:
            nodep, nodeq = queue.popleft()

            if not nodep and not nodeq:
                continue
            
            if not nodeq or not nodep or nodeq.val != nodep.val:
                return False

            queue.append((nodep.left, nodeq.left))
            queue.append((nodep.right, nodeq.right))
        return True