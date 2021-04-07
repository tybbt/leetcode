# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.nodeList = [-float('inf')]
        def midOrder(node: TreeNode):
            if not node:
                return
            if node.left:
                midOrder(node.left)
            self.nodeList.append(node.val)
            if node.right:
                midOrder(node.right)
        midOrder(root)
        self.length = len(self.nodeList)
        self.index = 0


    def next(self) -> int:
        self.index += 1
        return self.nodeList[self.index]

    def hasNext(self) -> bool:
        return self.index < self.length


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()