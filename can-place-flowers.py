class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flag = 0
        nums = []
        num = 0

        for i in flowerbed:
            if i == 1:

                if flag > 0:
                    nums.append(flag)
                    nums.append(0)
                else:
                    nums.append(0)
                flag = 0
                if flag >= 3 and flag % 2 == 0:
                    nums.append(0)
                elif flag >= 3:
                    num += (flag - 1) / 2

                flag = 0
            else:
                flag += 1

        if flag > 0:
            nums.append(flag)

        print(nums)
        length = len(nums)

        if length == 1 and nums[0] == 1:
            num = 1
        for i in range(length):
            value = nums[i]
            if value >= 2:
                if i == 0 and i == length - 1:
                    num += (value + 1) / 2
                elif i == 0 or i == length - 1:
                    if value % 2 == 0:
                        num += value / 2
                    else:
                        num += (value - 1) / 2
                else:
                    if value % 2 == 0:
                        num += (value / 2 - 1)
                    else:
                        num += (value - 1) / 2

        if num >= n:
            return True
        else:
            return False


if __name__ == '__main__':
    # 这种方法考虑的情况太多了
    print Solution().canPlaceFlowers([0, 0], 2)
