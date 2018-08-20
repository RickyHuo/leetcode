# encoding: utf-8


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        height = len(board)
        length = len(board[0])
        x = y = 0

        while True:
            if board[y][x] == word[0]:
                if self.search(x, y, board, height, length, word[1:], [[x, y]]):
                    return True
            if self.has_next(height, length, x, y):
                x, y = self.board_next(length, x, y)
            else:
                break
        return False

    # 判断二维网格是否遍历结束
    def has_next(self, height, length, x, y):
        if x + 1 == length and y + 1 == height:
            return False
        else:
            return True

    def board_next(self, length, x, y):
        if x + 1 == length:
            y = y + 1
            x = 0
        else:
            x = x + 1

        return x, y

    # 获取相邻元素列表
    def link_next(self, x, y, height, length, paths):
        items = []
        if y != 0:
            items.append([x, y - 1])

        if y != height - 1:
            items.append([x, y + 1])

        if x != 0:
            items.append([x - 1, y])

        if x != length - 1:
            items.append([x + 1, y])

        for i in range(len(items))[::-1]:
            if items[i] in paths:
                items.pop(i)

        return items

    def search(self, x, y, board, height, length, word, paths):
        if len(word) == 0:
            return True
        else:
            linked_list = self.link_next(x, y, height, length, paths)
            for i in linked_list:
                if board[i[1]][i[0]] == word[0]:
                    if self.search(i[0], i[1], board, height, length, word[1:], paths + [[i[0], i[1]]]):
                        return True

            return False


if __name__ == '__main__':
    print Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED")
    print Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE")
    print Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB")
    print Solution().exist([["A"]], "A")