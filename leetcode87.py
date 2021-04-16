class TreeNode:
    def __init__(self, val = ''):
        self.val = val
        self.left = None
        self.right = None
        self.parents = None

    def exchangeLR(self):
        Node = self.left
        self.left = self.right
        self.right = Node

class Solution:
    def makeTree(self, s1: str, s2: str) -> TreeNode:
        rootNode = TreeNode(s2[0])
        length = len(s1)
        index = 1
        node = rootNode
        for i in range(1, length):
            index = i
            while s1.index(s2[index-1]) > s1.index(s2[i]) and index > 0:
                if node is not rootNode:
                    node = node.parents
                    index -= 1
                else:
                    index -= 1
                    break

            newNode = TreeNode(s2[i])
            if index == i:
                node.right = newNode
                newNode.parents = node
                node = newNode
            else:
                changeNode = TreeNode()
                changeNode.parents = node.parents
                if node is rootNode:
                    rootNode = changeNode
                changeNode.left = node
                changeNode.right = newNode
                node.parents = changeNode
                newNode.parents = changeNode
                node = newNode
        return rootNode

    def midOrder(self, node: TreeNode, s: str) -> str:
        if node.left:
            return self.midOrder(node.left, s)
        if node.val != '':
            s = s + node.val
        if node.right:
            return self.midOrder(node.right, s)

    def exchange(self, node: TreeNode):
        if node.val == '':
            node.exchangeLR()
        if node.left:
            self.exchange(node.left)
        if node.right:
            self.exchange(node.right)

    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) == 0 or len(s1) == 1:
            return True
        root = self.makeTree(s1, s2)
        self.exchange(root)

        rs = []
        def midOrder(node: TreeNode, sL: list):
            if node.left:
                midOrder(node.left, sL)
            if node.val != '':
                sL.append(node.val)
            if node.right:
                midOrder(node.right, sL)
        midOrder(root, rs)
        s = "".join(rs)

        return s == s1


class Solution2:
    def isScramble(self, s1: str, s2: str) -> bool:
        @cache
        def dfs(i1: int, i2: int, length: int) -> bool:
            """
            第一个字符串从 i1 开始，第二个字符串从 i2 开始，子串的长度为 length，是否和谐
            """

            # 判断两个子串是否相等
            if s1[i1:i1 + length] == s2[i2:i2 + length]:
                return True

            # 判断是否存在字符 c 在两个子串中出现的次数不同
            if Counter(s1[i1:i1 + length]) != Counter(s2[i2:i2 + length]):
                return False

            # 枚举分割位置
            for i in range(1, length):
                # 不交换的情况
                if dfs(i1, i2, i) and dfs(i1 + i, i2 + i, length - i):
                    return True
                # 交换的情况
                if dfs(i1, i2 + length - i, i) and dfs(i1 + i, i2, length - i):
                    return True

            return False

        ans = dfs(0, 0, len(s1))
        dfs.cache_clear()
        return ans





sv = Solution()
s1 = "great"
s2 = "rgeat"
print(sv.isScramble(s1, s2))