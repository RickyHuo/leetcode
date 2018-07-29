# encoding: utf-8

class Solution(object):

    @staticmethod
    def climbStairs(n):
        """
        :type n: int
        :rtype: int
        """
        return steps(n)

    # 递推实现
    @staticmethod
    def climbStairs_1(n):
        """
        :type n: int
        :rtype: int
        """

        nums = [0, 1, 2]
        if n <= 2:
            return nums[n]
        else:
            for i in range(3, n+1):
                nums.append(nums[i-1] + nums[i-2])

        return nums[n]

# 递归实现
def steps(n):

    if n == 1:
        return 1
    elif n == 2:
        return 1 + steps(1)

    return steps(n-1) + steps(n-2)


if __name__ == '__main__':

    # https://blog.csdn.net/imred/article/details/48865359
    # https://blog.csdn.net/gohome520/article/details/6328762
    print Solution.climbStairs(35)
    # print Solution.climbStairs_1(35)
