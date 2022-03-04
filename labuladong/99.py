class Solution(object):
    def recoverTree(self, root):
        self.x = None
        self.y = None
        self.pre = None
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            if not self.pre:
                self.pre = root
            else:
                if self.pre.val>root.val:
                    self.y = root
                    if not self.x:
                        self.x = self.pre
                self.pre = root
            dfs(root.right)
        dfs(root)
        if self.x and self.y:
            self.x.val, self.y.val = self.y.val, self.x.val
        return root

# 莫里斯遍历
def recoverTree(root):
    x = None
    y = None
    pre = None
    tmp = None
    while root:
        if root.left:
            tmp = root.left
            while tmp.right and tmp.right != root:
                tmp = tmp.right
            if tmp.right is None:
                # 说明不是之后建立起来的
                tmp.right = root
                root = root.left
            else:
                if pre and pre.val>root.val:
                    y=root
                    if not x:
                        x = pre
                pre = root
                tmp.right = None
                root = root.right
        else:
            if pre and pre.val>root.val:
                y = root
                if not x:
                    x = pre
            pre = root
            root = root.right
        if x and y:
            x.val, y.val = y.val, x.val

            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pre = TreeNode(float('-inf'))
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.s = None
        def myrecover(node):
            if node.left:
                myrecover(node.left)
            if self.pre.val > node.val:
                self.s = self.pre if (self.s==None) else self.s
                self.t = node
            self.pre = node
            if node.right:
                myrecover(node.right)
            return node
        if root:
            myrecover(root)
            self.s.val, self.t.val = self.t.val, self.s.val
        return root

