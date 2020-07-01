# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.max_v = 0

    def maxPathSum(self, root: TreeNode) -> int:
        self.max_v = root.val
        def maxP(p):
            if not p:
                return 0

            left_max = max(maxP(p.left), 0)
            right_max = max(maxP(p.right), 0)

            max_p = left_max + right_max + p.val

            self.max_v = max(self.max_v, max_p)

            return max_p

        maxP(root)
        return self.max_v


if __name__ == '__main__':
    p = TreeNode(-3)

    s = Solution()
    print(s.maxPathSum(p))
