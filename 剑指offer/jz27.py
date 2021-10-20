# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        def my_mirrorTree(start):
            if start == None:
                return None
            if start.left != None or start.right != None:
                # tmp = start.right
                start.right, start.left = my_mirrorTree(start.left), my_mirrorTree(start.right)
            return start
        return my_mirrorTree(root)
