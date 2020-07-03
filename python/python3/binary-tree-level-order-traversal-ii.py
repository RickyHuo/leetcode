# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.queue = []
        self.res = []

    def levelOrderBottom(self, root: TreeNode) -> [[int]]:
        if root is None:
            return []
        self.queue.append(root)
        self.build_queue()
        return self.res[::-1]

    def build_queue(self):
        while len(self.queue) > 0:
            level = len(self.queue)
            item = []
            for _ in range(level):
                p = self.queue.pop(0)
                item.append(p.val)
                if p.left is not None:
                    self.queue.append(p.left)
                if p.right is not None:
                    self.queue.append(p.right)
            self.res.append(item)
