# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res = []

    def isValidBST(self, root: TreeNode) -> bool:
        self.buildTree(root)

        for i in range(len(self.res) - 1):
            if self.res[i] >= self.res[i+1]:
                return False
        return True

    def buildTree(self, root: TreeNode):
        if root is None:
            pass
        else:
            self.buildTree(root.left)
            self.res.append(root.val)
            self.buildTree(root.right)
