# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:

        if not A or not B:
            return False
        stack = [A]

        while len(stack) > 0:
            length = len(stack)
            for _ in range(length):
                p = stack.pop(0)
                if not p:
                    continue

                stack.append(p.left)
                stack.append(p.right)

                if p.val == B.val:
                    if self.isSubTree(p, B):
                        return True
        return False

    def isSubTree(self, A: TreeNode, B: TreeNode):
        if not B:
            return True
        if not A:
            return False

        return self.isSubTree(A.left, B.left) and self.isSubTree(A.right, B.right)
