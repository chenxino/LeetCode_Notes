class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def my_vp(postorder):
            print(postorder)
            if len(postorder) < 3:
                return True
            mid = postorder[-1]
            flag_l = True
            l_index = len(postorder)-1
            for i in range(len(postorder)-1):
                if postorder[i]>mid and flag_l:
                    l_index = i
                    flag_l = False
                if flag_l is False and postorder[i] < mid:
                    return False
            result = True
            
            result = result and my_vp(postorder[:l_index])
            result = result and my_vp(postorder[l_index:len(postorder)-1])
            return result
        return my_vp(postorder)