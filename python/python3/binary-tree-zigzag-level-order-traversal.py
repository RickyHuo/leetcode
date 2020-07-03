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

    def zigzagLevelOrder(self, root: TreeNode) -> [[int]]:
        if root is None:
            return []
        self.queue.append(root)
        self.build_queue()
        return self.res

    def build_queue(self):
        flag = 0
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
            if flag % 2 == 0:
                self.res.append(item)
            else:
                self.res.append(item[::-1])
            flag += 1
