# encoding: utf-8


class Solution(object):

    def mySqrt_1(self, x):
        """
        :type x: int
        :rtype: int
        """

        for i in range((x+1)/2 + 1):
            if i * i == x:
                return i

            if i * i > x:
                return i - 1
            else:
                i += 1

    def mySqrt_2(self, x):
        """
        :type x: int
        :rtype: int
        """

        i = 0
        while i <= (x+1)/2 + 1:
            if i * i == x:
                return i

            if i * i > x:
                return i - 1
            else:
                i += 1

    # 二分查找
    # https://www.cnblogs.com/grandyang/p/4346413.html
    def mySqrt_3(self, x):
        start = 0
        end = x
        while True:
            index = (end + start) / 2
            value1 = index * index
            value2 = (index + 1) * (index + 1)

            if value1 == x:
                return index

            elif value2 == x:
                return index+1

            else:
                if value1 < x < value2:
                    return index
                elif x < value1:
                    end = index
                else:
                    start = index


if __name__ == '__main__':

    # 内存溢出
    # print Solution().mySqrt_1(1780858488)
    # 时间超限
    print Solution().mySqrt_2(1780858488)
    # Pass
    print Solution().mySqrt_3(1780858488)
