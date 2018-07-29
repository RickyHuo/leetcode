class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        items = {}
        for i in list1:
            items[i] = 0

        values = []
        for i in list2:
            try:
                item = items[i]
                values.append(i)
            except:
                pass

        return values


if __name__ == '__main__':
    print Solution().findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["KFC", "Shogun", "Burger King"])