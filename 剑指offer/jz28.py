# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def match(l, r):
            if l == None and r == None:
                return True
            if l == None or r == None:
                return False
            result = False
            if l.val == r.val:
                result = match(l.left, r.right) and match(l.right, r.left)
            return result


        if root == None:
            return True
        result = False
        if root.left == None and root.right == None:
            return True
        if root.left == None or root.right == None:
            return False
        if root.left.val == root.right.val:
            result = match(root.left, root.right)
        return result