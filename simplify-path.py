class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        items = []

        paths = path.split("/")

        for i in paths:
            if i == '' or i == '.':
                pass
            elif i == '..':
                if len(items) != 0:
                    items.pop()
            else:
                items.append(i)

        return '/' + '/'.join(items)


if __name__ == '__main__':
    print Solution().simplifyPath("/a/./b/../../c/")