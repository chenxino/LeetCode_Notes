# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.next == None:
            if head.val == val:
                return None
            else:
                return 'error'
        if head.val == val:
            return head.next
        now_node = head
        while now_node.next != None:
            if now_node.next.val ==  val:
                now_node.next = now_node.next.next
                return head
            else:
                now_node = now_node.next
        return head
        


