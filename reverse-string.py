# encoding: utf-8

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]


if __name__ == '__main__':
    """
    L[n1:n2:n3]
    n1代表开始元素下标
    n2代表结束元素下标
    n3代表切片间隔以及切片方向,默认值是1
    """
    print Solution().reverseString('234')