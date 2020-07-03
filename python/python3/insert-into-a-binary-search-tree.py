# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:

        p = root
        while p is not None:
            if val > p.val:
                pre = p
                p = p.right
                if p is None:
                    pre.right = TreeNode(val)
            else:
                pre = p
                p = p.left
                if p is None:
                    pre.left = TreeNode(val)

        return root

    # def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
    #     self.buildTree(root)
    #     length = len(self.res)
    #     for i in range(length):
    #         if val > self.res[i]:
    #             self.res = self.res[:i] + [val] + self.res[i:]
    #             break
    #     if len(self.res) == length:
    #         self.res.append(val)
    #     return self.sortedArrayToBST(self.res)
    #
    # def sortedArrayToBST(self, nums: [int]) -> TreeNode:
    #     length = len(nums)
    #     if length >= 2:
    #         index = int(length / 2)
    #         p = TreeNode(nums[index])
    #         p.left = self.sortedArrayToBST(nums[:index])
    #         p.right = self.sortedArrayToBST(nums[index + 1:])
    #         return p
    #     elif length == 1:
    #         return TreeNode(nums[0])
    #     else:
    #         return None
    #
    # def buildTree(self, root: TreeNode):
    #     if root is None:
    #         pass
    #     else:
    #         self.buildTree(root.left)
    #         self.res.append(root.val)
    #         self.buildTree(root.right)
