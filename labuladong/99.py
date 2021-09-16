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

            

