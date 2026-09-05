# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node.val == subRoot.val:
                if self.checkSameTree(node, subRoot):
                    return True

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return False
        
    def checkSameTree(self, p, q):
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