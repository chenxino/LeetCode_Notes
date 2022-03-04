# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if preorder == None or inorder == None:
            return None
        index = {}
        for i in range(len(inorder)):
            index[inorder[i]] = i 
        def mybuildTree(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None
            pre_root = TreeNode(preorder[pre_left])
            in_root_index = index[preorder[pre_left]]
            size_left_tree =  in_root_index-in_left
            pre_root.left = mybuildTree(pre_left+1, pre_left+size_left_tree, in_left, in_root_index-1)
            pre_root.right = mybuildTree(pre_left+size_left_tree+1, pre_right, in_root_index+1, in_right)
            return pre_root
        return mybuildTree(0,len(preorder)-1, 0, len(preorder)-1)

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def myBuild(pre, ino):
            if not pre:
                return None
            root = TreeNode(pre[0])
            left_len = 0
            for i in range(len(ino)):
                if ino[i] == pre[0]:
                    break
                left_len += 1

            root.left = myBuild(pre[1:left_len+1], ino[:left_len])
            root.right = myBuild(pre[left_len+1:], ino[left_len+1:])
            return root
        return myBuild(preorder, inorder)