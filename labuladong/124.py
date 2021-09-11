# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxSum = float('-inf')
    def maxPathSum(self, root: TreeNode) -> int:
        def maxGain(node):
            if not node:
                return 0
            left = max(maxGain(node.left), 0)
            right = max(maxGain(node.right), 0)
            self.maxSum = max(self.maxSum, left+right+node.val)
            return max(node.val+left, node.val+right)
        maxGain(root)
        return self.maxSum
