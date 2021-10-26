"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        
        h = Node(head.val)
        now = head.next
        n = h
        dic = {}
        dic[head] = h
        while now is not None:
            tmp = Node(now.val)
            dic[now] = tmp
            n.next = tmp
            now = now.next
            n = n.next
        now = head
        n = h
        print(dic)
        while now is not None:
            if now.random is not None:
                n.random = dic[now.random]
            else:
                n.random = None
            now = now.next
            n = n.next
        return h