# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
sumN = 0
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)

def maketree(node: TreeNode, num: int):
    if num >= node.val:
        if node.right:
            maketree(node.right, num)
        else:
            newNode = TreeNode(num)
            node.right = newNode
    else:
        if node.left:
            maketree(node.left, num)
        else:
            newNode = TreeNode(num)
            node.left = newNode




nums = [10,5,15,3,7,13,18,1,6]
low = 6
high = 10
root = TreeNode(nums[0])
node = root
for num in nums[1:]:
    maketree(root, num)

sv = Solution()
print(sv.rangeSumBST(root, low, high))

