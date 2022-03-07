# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        queue = deque([root])
        step = 1
        if root is None:
            return 0
        while queue != []:
            for i in range(len(queue)):
                now = queue.popleft()
                if now.right is None and now.left is None:
                    return step
                if now.left:
                    queue.append(now.left)
                if now.right:
                    queue.append(now.right)
            step += 1
        return step
            
