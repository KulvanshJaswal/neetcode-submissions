# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([p])
        vals1= []

        while queue:
            node = queue.popleft()
            vals1.append(None) if not node else vals1.append(node.val)

            if node:
                queue.append(node.left)
                queue.append(node.right)

        queue2 = deque([q])
        vals2 = []
        while queue2:
            node = queue2.popleft()
            vals2.append(None) if not node else vals2.append(node.val)

            if node:
                queue2.append(node.left)
                queue2.append(node.right)

        if vals2 == vals1:
            return True
        return False