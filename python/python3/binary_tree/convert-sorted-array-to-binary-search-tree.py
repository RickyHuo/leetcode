# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def sortedArrayToBST(self, nums: [int]) -> TreeNode:
        length = len(nums)
        if length >= 2:
            index = int(length / 2)
            p = TreeNode(nums[index])
            p.left = self.sortedArrayToBST(nums[:index])
            p.right = self.sortedArrayToBST(nums[index + 1:])
            return p
        elif length == 1:
            return TreeNode(nums[0])
        else:
            return None


if __name__ == '__main__':
    p = Solution().sortedArrayToBST([-10, -3, 0, 5, 9], )
    print(p.val)
