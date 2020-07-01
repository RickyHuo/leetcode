class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        items = list()
        items.append(0)
        items.append(min(cost[0], cost[1]))

        i = 2
        while(i < len(cost)):
            items.append(min(items[i-2] + cost[i-1], items[i-1] + cost[i]))
            i += 1

        return items


if __name__ == '__main__':
    print Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])