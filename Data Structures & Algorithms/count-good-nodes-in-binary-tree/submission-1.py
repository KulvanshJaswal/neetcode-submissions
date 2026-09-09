# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #create a recursive algo where we pass the max of the current ds going down and then return up
        #each part of goign down will  have its own assigned max from above and compare from 
        #itself to the max if its greater than the previous max add else dont just return

        def goodNode(node, prevMax):
            if not node:
                return 0
            currentMax = max(node.val, prevMax)

            left = goodNode(node.left, currentMax)
            right = goodNode(node.right, currentMax)

            if node.val >= prevMax:
                return 1 + left + right

            return left + right

        return  goodNode(root, root.val)