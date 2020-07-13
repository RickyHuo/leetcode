class Solution:
    def exist(self, board: [[str]], word: str) -> bool:

        res = []

        def back_track(count, selected: [[]]):
            coordinate = selected[-1]
            x, y = coordinate[0], coordinate[1]

            if x >= len(board) or x < 0:
                return
            if y >= len(board[0]) or y < 0:
                return
            if word[len(selected) - 1] != board[x][y]:
                return

            if selected.count(coordinate) > 1:
                return

            if count == len(word):
                res.append(count)
                return
            count += 1
            selected.append([x+1, y])
            back_track(count, selected)
            selected.pop()

            selected.append([x-1, y])
            back_track(count, selected)
            selected.pop()

            selected.append([x, y+1])
            back_track(count, selected)
            selected.pop()

            selected.append([x, y-1])
            back_track(count, selected)
            selected.pop()

        for i in range(len(board)):
            for j in range(len(board[i])):
                back_track(1, [[i, j]])

        return len(res) >= 1


if __name__ == "__main__":
    res = Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
                           "ABCCED")
    print(res)
    res = Solution().exist([["a", "a"]], "aaa")
    print(res)





