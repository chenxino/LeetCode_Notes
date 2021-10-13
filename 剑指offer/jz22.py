class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if k == 0:
            return None
        a = head
        b = head 
        for i in range(k-1):
            if b.next == None:
                return "error"
            b = b.next
        while b.next != None:
            a = a.next
            b = b.next
        return a