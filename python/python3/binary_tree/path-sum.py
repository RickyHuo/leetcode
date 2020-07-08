# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res = []

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root:
            if root.left:
                self.sumNode(root.left, root.val)
            if root.right:
                self.sumNode(root.right, root.val)
            if not root.left and not root.right:
                return sum == root.val
        else:
            return False

        if sum in self.res:
            return True
        return False

    def sumNode(self, root, sum: int):
        if root.left:
            self.sumNode(root.left, root.val + sum)

        if root.right:
            self.sumNode(root.right, root.val + sum)

        if not root.left and not root.right:
            self.res.append(sum + root.val)

