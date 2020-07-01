class Solution(object):

    @staticmethod
    def is_power_two(n):
        """
        :type n: int
        :rtype: bool
        """
        str = bin(n)

        tmp_str = str[3:]

        if n == 0:
            return False

        if '1' in tmp_str:
            return False

        else:
            return True
