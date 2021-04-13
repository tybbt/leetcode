# Definition for a binary tree node.
import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        tree = []
        MIN = float('inf')
        def makeTreeList(node: TreeNode):
            if node.left:
                makeTreeList(node.left)
            tree.append(node.val)
            if node.right:
                makeTreeList(node.right)
        makeTreeList(root)
        for i in range(1, len(tree)):
            MIN = min(MIN, tree[i]-tree[i-1])
        return int(MIN)

treeList = [90,69,49,89,52]
root = TreeNode(treeList[0])

def makeTree(node: TreeNode, val):
    if val <= node.val:
        if node.left:
            makeTree(node.left, val)
        else:
            node.left = TreeNode(val)
    else:
        if node.right:
            makeTree(node.right, val)
        else:
            node.right = TreeNode(val)


for i in range(1, len(treeList)):
    makeTree(root, treeList[i])

sv = Solution()
print(sv.minDiffInBST(root))

