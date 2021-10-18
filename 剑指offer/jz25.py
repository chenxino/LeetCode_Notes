# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        while l1 != None and l2 != None:
            if l1.val > l2.val :
                if head == None:
                    head = l2
                    now = head
                else:
                    now.next = l2
                    now = now.next
                l2 = l2.next
            else:
                if head == None:
                    head = l1
                    now = head
                else:
                    now.next = l1
                    now = now.next
                l1 = l1.next
        if head == None:
            return l1 if l1 != None else l2
        if l1 != None:
            now.next = l1
        else:
            now.next = l2
        return head

# 递归
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        def my_merge(a, b):
            if a == None:
                return b
            if b == None:
                return a
            if a.val < b.val:
                head = a
                head.next = my_merge(a.next, b)
            else:
                head = b
                head.next = my_merge(a, b.next)
            return head
        return my_merge(l1, l2)
            