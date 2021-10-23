# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        results = []
        def my_level(ll):
            next_l = []
            for i in ll:
                results.append(i.val)
                if i.left is not None:
                    next_l.append(i.left)
                if i.right is not None:
                    next_l.append(i.right)
            return next_l
        if root is None:
            return []
        
        n_list = my_level([root])
        while n_list != []:
            n_list = my_level(n_list)
        return results
                