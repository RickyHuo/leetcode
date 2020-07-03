class Solution:
    def __init__(self):
        self.index = []

    def _fetch_matrix(self, matrix, i, j, length):
        if i >= length or j >= length:
            return None
        else:
            return matrix[i][j]

    def kthSmallest(self, matrix: [[int]], k: int) -> int:
        length = len(matrix)
        r = matrix[0][0]
        self.index = [0] * length
        for i in range(k):
            flag = 0
            min_res = self._fetch_matrix(matrix, 0, self.index[0], length)
            for j in range(1, length):
                tmp = self._fetch_matrix(matrix, j, self.index[j], length)

                if tmp is not None and min_res is not None and tmp > min_res:
                    pass
                elif tmp is not None:
                    min_res = tmp
                    flag = j
            self.index[flag] += 1
            r = min_res
        return r


if __name__ == "__main__":
    res = Solution().kthSmallest([[3, 8, 8], [3, 8, 8], [3, 9, 13]], 8)
    print(res)
