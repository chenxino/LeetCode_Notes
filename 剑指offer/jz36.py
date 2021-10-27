"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def connect(node_l, head):
            node_l_1 = node_l
            node_l_2 = node_l.left
            head_1 = head
            head_2 = head.left
            node_l_1.left = head_2
            node_l_2.right = head_1
            head_1.left = node_l_2
            head_2.right = node_l
            return node_l

        def my_dl(head):
            if head is None:
                return None
            
            l = my_dl(head.left)
            r = my_dl(head.right)
            head.right = head
            head.left = head
            if l is not None:
                head = connect(l, head)
            if r is not None:
                head = connect(head, r)
            return head
        return my_dl(root)