class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if listNode == None:
            return []
        ll = []
        head = listNode
        while head.next != None:
            ll.insert(0, head.val)
            head = head.next
        ll.insert(0, head.val)
        return ll