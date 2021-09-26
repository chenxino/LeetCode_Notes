# 给定一个二叉树其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的next指针。
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        if pNode == None:
            return None
        if pNode.right != None:
            result = pNode.right
            while result.left != None:
                result = result.left
            return result
        else:
            while pNode.next != None:
                if pNode.next.left == pNode:
                    return pNode.next
                pNode = pNode.next
            return None