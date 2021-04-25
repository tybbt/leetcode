# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        nodeStack = []

        def midOrder(node: TreeNode):
            if node.left:
                midOrder(node.left)
            nodeStack.append(node.val)
            if node.right:
                midOrder(node.right)

        midOrder(root)

        root = TreeNode(nodeStack[0])
        parent = root
        for i in range(1, len(nodeStack)):
            node = TreeNode(nodeStack[i])
            parent.right = node
            parent = node

        return root




