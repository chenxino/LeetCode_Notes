# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        results_list = []
        def my_level(ll):
            next_l = []
            results = []
            for i in ll:
                results.append(i.val)
                if i.left is not None:
                    next_l.append(i.left)
                if i.right is not None:
                    next_l.append(i.right)
            return next_l, results
        if root is None:
            return results_list
        
        n_list = [root]
        while n_list != []:
            n_list, results = my_level(n_list)
            results_list.append(results)
        return results_list