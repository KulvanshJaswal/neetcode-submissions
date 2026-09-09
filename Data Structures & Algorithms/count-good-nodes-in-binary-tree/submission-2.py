# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def goodNode(node, prevMax):
            if not node:
                return 0
            currentMax = max(node.val, prevMax)

            left = goodNode(node.left, currentMax)
            right = goodNode(node.right, currentMax)

            sum = left + right

            if node.val >= prevMax:
                return 1 + sum

            return sum

        return goodNode(root, root.val)