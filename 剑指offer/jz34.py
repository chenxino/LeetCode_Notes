# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if root is None:
            return []
        sum_path = []
        paths = []
        def my_ps(root, target):
            
            if root.val == target and root.left == None and root.right == None:
                
                sum_path.append(root.val)
                print(sum_path)
                paths.append(sum_path.copy())
                print(paths)
                sum_path.pop()
            # if root.val != target:
            else:
                sum_path.append(root.val)
                # print(target)
                if root.left is not None:
                    my_ps(root.left, target-root.val)
                if root.right is not None:
                    my_ps(root.right, target-root.val)
                sum_path.pop()
            return 
        my_ps(root, target)
        return paths
