class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []
        if root is None:
            return []
        nodes = [root]
        while nodes != []:
            new_nodes = []
            for node in nodes:
                if node != None:
                    result.append(node.val)
                    new_nodes.append(node.left)
                    new_nodes.append(node.right)
                else:
                    result.append(None)
            nodes = new_nodes
        while result[-1] == None:
            result.pop()
        print(result)
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == []:
            return None
        root = TreeNode(int(data[0]))
        nodes = collections.deque()
        nodes.append(root)
        # data = data.split(',')[1:-1]
        i = 1
        while i<len(data):
            node = nodes.popleft()
            if data[i] is not None:
                node.left = TreeNode(int(data[i]))
                nodes.append(node.left)
            i += 1
            if i < len(data) and data[i] is not None:
                node.right = TreeNode(int(data[i]))
                nodes.append(node.right)
            i += 1
        print(root)
        return root