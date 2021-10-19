# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def match(a, b):
            if b == None:
                return True
            if a == None:
                return False
            if a.val != b.val:
                return False
            return match(a.left, b.left) and match(a.right, b.right)

        def my_isSubStructure(a, b):
            result = False
            if b == None:
                return True
            if a == None:
                return False
            if a.val == b.val:
                # print(a.val)
                result = match(a.left, b.left) and match(a.right, b.right)
            if result == False: 
                result = my_isSubStructure(a.left, b) or my_isSubStructure(a.right, b)
            return result
        if B == None:
            return False
        return my_isSubStructure(A, B)
        