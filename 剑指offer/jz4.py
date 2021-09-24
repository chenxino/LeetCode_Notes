class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, vin):

        n = len(pre)
        if n == 0:
            return None
        dic = {}
        for i in range(n):
            dic[vin[i]] = i
        
        def my_reCon(pre_l, pre_r, vin_l, vin_r):
            if pre_l>pre_r or vin_l > vin_r:
                return None
#             print(pre_l)
            root = TreeNode(pre[pre_l])
            vin_index_r = dic[root.val]
            
            if pre_l == pre_r and vin_l == vin_r:
                return root
            
            n_l = vin_index_r - vin_l
            root.left = my_reCon(pre_l+1, pre_l+n_l, vin_l, vin_index_r-1)

            root.right = my_reCon(pre_l+n_l+1, pre_r, vin_index_r+1, vin_r)
            return root
            
        return my_reCon(0, n-1, 0, n-1)