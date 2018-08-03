class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        items = {
            "R": 0,
            "L": 0,
            "U": 0,
            "D": 0
        }

        for i in moves:
            items[i] += 1

        if items["R"] == items["L"] and items["U"] == items["D"]:
            return True
        else:
            return False


if __name__ == '__main__':
    print Solution().judgeCircle("UD")
    print Solution().judgeCircle("URR")
    print Solution().judgeCircle("UD")