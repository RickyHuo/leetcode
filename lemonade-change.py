class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        m5 = m10 = m20 = 0

        for i in bills:
            if i == 5:
                m5 += 1
            elif i == 10:
                if m5 < 1:
                    return False
                else:
                    m5 -= 1
                    m10 += 1
            else:
                m20 += 1
                if m5 >= 1 and m10 >= 1:
                    m5 -= 1
                    m10 -= 1
                elif m10 < 1 and m5 >= 3:
                    m5 -= 3
                else:
                    return False
        return True


if __name__ == '__main__':
    print Solution().lemonadeChange([5,10,20])