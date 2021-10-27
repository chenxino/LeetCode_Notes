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

# 不用哈希表
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        def clone_node(head):
            now = head
            while now is not None:
                tmp = now.next
                now.next = Node(now.val)
                now.next.next = tmp
                now = now.next.next
            return head
        def connect_node_random(head):
            now = head
            while now is not None:
                n = now.next
                if now.random == None:
                    n.random = None
                else:
                    n.random = now.random.next
                now = n.next
            return head
        def reconnect_node(head):
            h = head.next
            n = h
            while n.next is not None:
                n.next = n.next.next
                n = n.next
            return h
        head = clone_node(head)
        head = connect_node_random(head)
        head = reconnect_node(head)
        return head


